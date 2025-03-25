# aclock.py Test/demo program for nanogui
#
# Modified 28 January 2025
# By 2025 KW Services to support SSD1963 800X480 LCD Display.
# MIT License
# MicroPython v1.20.0 on 2023-04-26; Raspberry Pi Pico with RP2040
#
# Originally for ssd1351-based OLED displays but runs on most displays
# Adafruit 1.5" 128*128 OLED display: https://www.adafruit.com/product/1431
# Adafruit 1.27" 128*96 display https://www.adafruit.com/product/1673

# Released under the MIT License (MIT). See LICENSE.
# Copyright (c) 2018-2020 Peter Hinch

# Initialise hardware and framebuf before importing modules.
from color_setup import ssd  # Create a display instance


from gui.core.nanogui import refresh  # Color LUT is updated now.
from gui.widgets.label import Label
from gui.widgets.dial import Dial, Pointer
refresh(ssd, True)  # Initialise and clear display.

# Now import other modules
import cmath
import utime
#import TFTfont
from gui.core.writer import CWriter

# Font for CWriter
import gui.fonts.arial10 as arial10
import gui.fonts.font10 as font10

#added
from gui.core.colors import BLACK, GREEN, RED, YELLOW

def aclock():
    uv = lambda phi : cmath.rect(1, phi)  # Return a unit vector of phase phi
    pi = cmath.pi
    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
            'Sunday')
    months = ('Jan', 'Feb', 'March', 'April', 'May', 'June', 'July',
              'Aug', 'Sept', 'Oct', 'Nov', 'Dec')
    # Instantiate CWriter
    CWriter.set_textpos(ssd, 0, 0)  # In case previous tests have altered it
    wri = CWriter(ssd, font10, GREEN, BLACK )  # Report on fast mode. Or use verbose=False
    wri.set_clip(True, True, False)

    # Instantiate displayable objects
    dial = Dial(wri, 2, 2, height = 75, ticks = 12, bdcolor=None, label=120, pip=False)  # Border in fg color
    lbltim = Label(wri, 5, 85, 35)
    hrs = Pointer(dial)
    mins = Pointer(dial)
    secs = Pointer(dial)

    hstart =  0 + 0.7j  # Pointer lengths and position at top
    mstart = 0 + 0.92j
    sstart = 0 + 0.92j 
    while True:
        t = utime.localtime()
        
        #print(t)  # debug: 2025-01-23
        
        hrs.value(hstart * uv(-t[3]*pi/6 - t[4]*pi/360), YELLOW)
        mins.value(mstart * uv(-t[4] * pi/30), YELLOW)
        secs.value(sstart * uv(-t[5] * pi/30), RED)
        #
        # lbltim.value is using writer.setcolor() is setting fg=1,bg=0
        #  but the above setTextStyle is correcting it
        #
        lbltim.value('{:02d}.{:02d}.{:02d}'.format(t[3], t[4], t[5]))
        dial.text('{} {} {} {}'.format(days[t[6]], t[2], months[t[1] - 1], t[0]))
        refresh(ssd)
        utime.sleep(1)

aclock()
