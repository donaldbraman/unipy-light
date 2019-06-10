# this is run on a crontab to change colors for my kids room. 
# the crontab calls this script at 7 PM, turning it red. 
# again at 6:30 AM, turning it yellow. 
# and again at 7 AM, turning it green. 
# for fun, it also runs it in rainbow colors for an hour at 8 AM. 

import time
import maya
import colorsys
import itertools as it
import unicornhat as uh
uh.set_layout(uh.PHAT)


def light_time(start=maya.now(), duration=0.1):
    end =  start.add(minutes=duration)
    return  maya.now() >= start and maya.now() <= end


def rainbow(start_time=maya.now(), duration_min=1):
    uh.brightness(1.0)
    spacing = 360.0 / 16.0
    hue = 0
    while light_time(start=start_time, duration=duration_min):
        hue = int(time.time() * 100) % 360
        for x,y in it.product(range(8), range(4)):
            offset = x * spacing
            h = ((hue + offset) % 360) / 360.0
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
            uh.set_pixel(x, y, r, g, b)
        uh.show()
        uh.clear()


def light(start_time=maya.now(), duration_min=0.5, rgb=[255,0,0]):
    [r,g,b] = rgb
    print("light started", rgb)
    uh.brightness(1.0)
    for x,y in it.product(range(8), range(4)):
        uh.set_pixel(x,y,r,g,b)
    while light_time(start=start_time, duration=duration_min):
        uh.show()
    uh.clear()
    uh.show()


redstart = maya.when('T19:00:00 EST')
redduration = (60*11)+29.5

yellowstart = maya.when('T06:30:00 EST')
yellowduration = 29.5

greenstart = maya.when('T07:00:00 EST')
greenduration = 59.5

rainbowstart = maya.when('T08:00:00 EST')
rainbowduration = 9*60

if maya.now() >= redstart and maya.now() <= yellowstart.add(hours=12):
    light(start_time=maya.now(), duration_min=redduration, rgb=[255,0,0])
elif maya.now() >= yellowstart and maya.now() <= greenstart:
    light(start_time=maya.now(), duration_min=yellowduration, rgb=[255,255,0])
elif maya.now() >= greenstart and maya.now() <= rainbowstart:
    light(start_time=maya.now(), duration_min=greenduration, rgb=[0,255,0])
else:
    rainbow(duration_min=60)


uh.clear()
uh.show()
