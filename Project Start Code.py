import opc
from time import sleep
import colorsys
import time
import random



leds = [(255,255,255)]*360   # list of 360 tuples, each containing R,G,B values.

client = opc.Client('localhost:7890')
client.put_pixels(leds)

def func1 (val):
    for led in range(60): #pick out indeces: led = 0,1,2,3...
        leds[led] = (255,0,0)
        time.sleep(.1)
        client.put_pixels(leds)
    led = 0
    while led<60: #scroll all rows at the same time
        leds[led] = (0,0,255) #row 1 - 0-60
        leds[led+60] = (0,0,255) #row 2 - 0+60 - 59+60 (60-119)
        leds[led+120] = (0,0,255)
        leds[led+180] = (0,0,255) #this can be done in 2 lines instead of 6
        leds[led+240] = (0,0,255)
        leds[led+300] = (0,0,255)
        client.put_pixels(leds)
        time.sleep(.1)
        led = led + 1
    led = 0
    while led<60: #scroll all rows at the same time
        leds[led] = (0,0,255) #row 1 - 0-60
        leds[led+60] = (0,0,255) #row 2 - 0+60 - 59+60 (60-119)
        leds[led+120] = (0,0,255)
        leds[led+180] = (0,0,255) #this can be done in 2 lines instead of 6
        leds[led+240] = (0,0,255)
        leds[led+300] = (0,0,255)
        client.put_pixels(leds)
        time.sleep(.1)
        led = led + 1
def func2 (val) :
        led = 0
        while led<60: #scroll all rows at the same time
            leds[led] = (0,0,255) #row 1 - 0-60
            leds[led+60] = (0,0,255) #row 2 - 0+60 - 59+60 (60-119)
            leds[led+120] = (0,0,255)
            leds[led+180] = (0,0,255) #this can be done in 2 lines instead of 6
            leds[led+240] = (0,0,255)
            leds[led+300] = (0,0,255)
            client.put_pixels(leds)
            time.sleep(.1)
            led = led + 1
def func3 (val):
        led = 0
        while led<60: #scroll all rows at the same time
            leds[led] = (0,0,255) #row 1 - 0-60
            leds[led+60] = (0,0,255) #row 2 - 0+60 - 59+60 (60-119)
            leds[led+120] = (0,0,255)
            leds[led+180] = (0,0,255) #this can be done in 2 lines instead of 6
            leds[led+240] = (0,0,255)
            leds[led+300] = (0,0,255)
            client.put_pixels(leds)
            time.sleep(.1)
            led = led + 1

value = input ( ''' Welcome to The Car Showroom. Pick a car option below: 
                \t Type the number of your choice and press Enter.
                \t 1. Mercedes
                \t 2. Lexus
                \t 3. Chevrolet
                 ''')
    
while True:
    if value.isdigit() == True: # .isdigit() 
        value = int(value)
        if value >3 or value <1 : #if the value is outside our parameters
             value = input (" Please input a number which corresponds with your cars option :  ")
             continue # skip the rest of the loop, start from isdigit() check again
        else:
            break # on correct value datatype: exit the loop
    else:
        value=input("Invalid input, please provide an number from the list of cars above:")
if value == 1 :
    print (func1)
elif value ==2 :
    print (func2)
elif value ==3 :
    print (func3)
