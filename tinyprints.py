import serial
import cups
import os
from datetime import datetime

conn = cups.Connection()
ser = serial.Serial('/dev/serial0')

QUEUE_PATH = './queue/'


def reset():
    ser.write(b'\x1b\x21\x00')


def print_png(filename):
    ser.write('{}\n{}\n'.format(datetime.now().isoformat(), filename).encode())
    job_id = conn.printFile('ZJ-58', QUEUE_PATH + filename, '', {})


def delete_from_queue(filename):
    os.remove(QUEUE_PATH + filename)


reset()
print_png('test.png')
delete_from_queue('test.png')
