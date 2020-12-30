# tinyprints
This is a collection of scripts for my Raspberry Pi driven thermal printer.


## print_a_pokemon.py
Is designed to print a Pokemon once a day.
Data is retrieved via pokeapi.co.

Example of a print:
![bulbasaur scan](https://github.com/StefanAvra/tinyprints/blob/main/bulbasaur.jpeg?raw=true)

### Usage
```print_a_pokemon.py``` depends on [ImageMagick](https://imagemagick.org/script/download.php). Install that first and check if it can be executed via ```convert``` in terminal.

Clone this repo and cd into ./tinyprints.

Create and activate virtual env
```sh
python3 -m venv venv
source venv/bin/activate
```

Install dependencies
```sh
pip install -r requirements.txt
```

To create a cron job that runs ```print_pokemon.sh``` everyday at 20:00 you can run
```sh
crontab -e
```
and add
```sh
0 20 * * * /path/to/directory/tinyprints/print_pokemon.sh
```
