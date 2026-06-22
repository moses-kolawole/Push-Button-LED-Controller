from machine import Pin
from time import sleep

butpin = 14
ledpin = 15

mybutton = Pin(butpin, Pin.IN, Pin.PULL_UP)
ledstate = Pin(ledpin, Pin.OUT)

while True:
    butstate = mybutton.value()
    print(butstate)
    
    if (butstate == 0):
        ledstate.value(1)
    else:
        ledstate.value(0)
        
    sleep(.1)
        
    
    