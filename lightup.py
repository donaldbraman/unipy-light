# this is run on boot to change colors for my kids room. 

import time
import itertools as it
import maya
import unicornhat as uh
uh.set_layout(uh.PHAT)

def light(color):
    [r,g,b] = color.rgb
    uh.brightness(color.brightness)
    for x,y in it.product(range(8), range(4)):
        uh.set_pixel(x,y,r,g,b)
    uh.show()

class red:
    brightness = 0.25
    rgb = [255,0,0]

class green:
    brightness = 0.25
    rgb = [0,255,0]

while True:
    now = maya.now()
    if now > maya.when("T07:00:00 EDT") and now < maya.when("T19:00:00 EDT"):
        light(green)
    else: 
        light(red)
    time.sleep(10)
uh.clear()
uh.show()


