# Assigns URL from adafruit
ada_name = "evansz"
ada_key = "aio_ApJc17qpike9YhU2vjkDP4QEa8db"
URL = "https://io.adafruit.com/api/v2/webhooks/feed/kMdRTuhEjdiVZBgY7uDFHun6ToQ4"

import requests
import time
import serial
from Adafruit_IO import Client

aio = Client(ada_name, ada_key)

s = serial.Serial('/dev/tty.usbmodem1301', baudrate=115200)
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
    

