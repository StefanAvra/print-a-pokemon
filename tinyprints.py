import serial
import cups
from datetime import datetime

conn = cups.Connection()
ser = serial.Serial('/dev/serial0')


def reset():
    ser.write(b'\x1b\x21\x00')


def print_png(filename):
    ser.write('{}\n{}\n'.format(datetime.now().isoformat(), filename).encode())
    job_id = conn.printFile('ZJ-58', filename, '', {})

