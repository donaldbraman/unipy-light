import colorsys
import time
import itertools as it
import unicornhat as uh
uh.set_layout(uh.PHAT)

def light(color):
    [r,g,b] = color.rgb
    uh.brightness(color.brightness)
    for x,y in it.product(range(8), range(4)):
        uh.set_pixel(x,y,r,g,b)
    uh.show()

class red:
    brightness = 0.2
    rgb = [255,0,0]

class green:
    brightness = 0.2
    rgb = [0,255,0]

class blue:
    brightness = 0.2
    rgb = [0,0,255]

def rainbow():
    uh.brightness(1.0)
    spacing = 360.0 / 16.0
    hue = 0
    t_end = time.time() + 60 * 1 
    while time.time() < t_end:
        hue = int(time.time() * 100) % 360
        for x,y in it.product(range(8), range(4)):
            offset = x * spacing
            h = ((hue + offset) % 360) / 360.0
            r, g, b = [int(c * 255) for c in colorsys.hsv_to_rgb(h, 1.0, 1.0)]
            uh.set_pixel(x, y, r, g, b)
        uh.show()
        uh.clear()

while True:
    now = time.localtime()
    hour = now[3]
    if hour > 6 and hour < 19:
        if time.strftime('%A') == "Saturday":
            rainbow()
        elif time.strftime('%A') == "Sunday":
            rainbowt()
        elif time.strftime('%A') == "Friday":
            light(blue)
        else:
            light(green)
    else:
        light(red)
    time.sleep(10)
uh.clear()
uh.show()
