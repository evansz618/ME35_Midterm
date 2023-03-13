# Assigns URL from adafruit
ada_name = 
ada_key = 
URL = 

import requests
import time
import serial
from Adafruit_IO import Client

aio = Client(ada_name, ada_key)

s = serial.Serial( 'USB NAME', baudrate=115200)
print(s.read_all())
s.write(b'import Lego_Arm\r\n')

while True:
    data = aio.receive('lego-arm')[3]
    print(data)
    if data == '0':
        pass
    if data == '1':
        s.write(b'Lego_Arm.main()\r\n')
        print("Running")
        break
    time.sleep(2)
    

