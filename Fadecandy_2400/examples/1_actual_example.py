#!/usr/bin/env python

import opc   #pixel control library, allows to connect and publist to client
import time

led_colour=[(255,0,0)]*10  # {to setup colors} - list of 1 red pixel multiplied by 10

client = opc.Client('localhost:7890') #server and port for client 

print (enumerate(led_colour))  #shows number/location of the led plus the value for that position which gives the color.
for item in enumerate(led_colour): 
    time.sleep(1)
    print (item)
    if item[0]%2 == 0:
        #need to get values out of tuple
        r, g, b = item[1] #unpack tuple item
        r = r-120 #reduces value for r by 120


        #create changed tuple (uses some values from old and some new) 
        new_colour =(r,g,b) #repackage tuple
        led_colour[item[0]]= new_colour  #led color at position 0 will be assigned new color
    client.put_pixels(led_colour)
    client.put_pixels(led_colour)

client.put_pixels(led_colour)
#need to send it twice if not constantly sending values 
#due to interpolation setting on fadecandy
client.put_pixels(led_colour)
print (led_colour)
