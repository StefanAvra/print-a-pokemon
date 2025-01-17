import requests
import cups
import wget
import os
import time
import subprocess
import serial

conn = cups.Connection()
ser = serial.Serial('/dev/serial0')

os.chdir(os.path.dirname(os.path.abspath(__file__)))


API_URL = 'https://pokeapi.co/api/v2/'
SPRITES_PATH = './pokemon_sprites/'

if not os.path.exists(SPRITES_PATH):
    os.mkdir(SPRITES_PATH)
if not os.path.exists('./pkmn_no'):
    with open('./pkmn_no', 'w') as f:
        f.write('1')

with open('./pkmn_no') as f:
    pkmn_no = f.readline()

r = requests.get(f'{API_URL}pokemon/{pkmn_no}/')

if not r.ok:
    raise Exception(f'GET {r.url} {r.status_code}')

pokemon = r.json()

# download sprite and convert
sprite_url = pokemon.get('sprites').get('front_default')
wget.download(sprite_url, f'{SPRITES_PATH}{pkmn_no}.png')
subprocess.run(['convert', f'{SPRITES_PATH}{pkmn_no}.png', '-flatten', '-resize', '384x384', '-monochrome', f'{SPRITES_PATH}{pkmn_no}_mono.png'])

# print sprite via cups
job_id = conn.printFile('ZJ-58', f'{SPRITES_PATH}{pkmn_no}_mono.png','',{})
while conn.getJobs().get(job_id, None) is not None:
    time.sleep(1)

# index
ser.write(b'\x1b\x21\x00') # reset
ser.write('#{}\n'.format(pkmn_no).encode())

# name
ser.write(b'\x1b\x21\x32') # double width
ser.write('{}\n'.format(pokemon.get('name').capitalize()).encode())
ser.write(b'\x1b\x21\x00')

# type
ser.write('Type: '.encode())
type_count = 0
for slot in pokemon.get('types'):
    type_count += 1
    if type_count > 1:
        ser.write(', '.encode())
    ser.write('{}'.format(slot.get('type').get('name')).encode())
ser.write('\n'.encode())

# weight
ser.write('Weight: {} kg\n'.format(pokemon.get('weight')/10).encode())

# base xp
ser.write('Base XP: {}\n'.format(pokemon.get('base_experience')).encode())

# stats
for stat in pokemon.get('stats'):
    ser.write('{} {}\n'.format(stat.get('base_stat'), stat.get('stat').get('name')).encode())

ser.write('\n\n'.encode())


# increase pkmn no
with open('./pkmn_no', 'w') as f:
    f.write(str(int(pkmn_no) + 1))

