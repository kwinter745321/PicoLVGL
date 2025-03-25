# display_driver.py
#
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-724-gbf1107420 on 2025-02-19; Raspberry Pi Pico with RP2040
# Raspberry Pi Pico (RP2040)
# LVGL 9.1                    https://docs.lvgl.io/9.1/
#
# 
import lvgl as lv
import ili9xxx
import xpt2046
from machine import SPI, Pin, reset
import time


# Initialize LVGL
lv.init()
print("Running LVGL %d.%d" % (lv.version_major(), lv.version_minor() )  )

# Initialize display
spi = SPI(0, baudrate=20_000_000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
tspi = SPI(0, baudrate=2_000_000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
print("Init SPI")
disp = ili9xxx.Ili9341(spi=spi, dc=0, cs=17, rst=1, rot=1)


print("Init disp")
disp.clear(0x000000)
print("Pause 1 sec.")
time.sleep(1)

# Create screen object
hres = 320
vres = 240
disp_drv = lv.display_create(hres,vres)
print("Screen config")
scr = lv.screen_active()
#scr = lv.obj()

# Initialize touch screen
touch = xpt2046.Xpt2046_hw(spi=tspi,cs=21,rot=1)
print("Using Touch setup")

# @micropython.native
def tsread(indev_drv, data) -> int:
    coords = touch.pos()
    if coords:
        data.point.x, data.point.y = coords
        data.state = lv.INDEV_STATE.PRESSED
        return True
    data.state = lv.INDEV_STATE.RELEASED
    return False

#indev for touch screen
indev_drv = lv.indev_create()
indev_drv.set_type(lv.INDEV_TYPE.POINTER)
indev_drv.set_read_cb(tsread)

###############################################
# Reset Thonny
###############################################
    
#### Reset Button #####################
class HardReset():
    
    def __init__(self, scr):
        self.rbtn = None
        self.rlbl = None
        self.rbtn = lv.button(scr)
        self.rbtn.set_pos(240,200)
        self.rbtn.set_style_bg_color(lv.palette_main(lv.PALETTE.RED),0)
        self.rlbl = lv.label(self.rbtn)
        self.rlbl.set_text("Reset")
        self.rlbl.center()
        self.rbtn.add_event_cb(self.reset_cb, lv.EVENT.CLICKED, None)

    def reset_cb(self, event):
        reset()
        
    def reset(self):
        reset()
        



