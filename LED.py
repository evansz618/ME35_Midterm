from machine import Pin, I2C
import time

p1 = Pin(25, Pin.OUT)
p2 = Pin(15, Pin.OUT)
p3 = Pin(16, Pin.OUT)
p4 = Pin(17, Pin.OUT)

def turn_on(number):
    if number == 1:
        p1.value(1)
    if number == 2:
        p2.value(1)
    if number == 3:
        p3.value(1)
    if number == 4:
        p4.value(1)
            
def turn_off(number):
    if number == 1:
        p1.value(0)
    if number == 2:
        p2.value(0)
    if number == 3:
        p3.value(0)
    if number == 4:
        p4.value(0)
    
def wave_on():
    for j in range(5):
        turn_on(j)
        time.sleep(.08)
        
def wave_off():
    for q in range(5):
        turn_off(q)
        time.sleep(.08)