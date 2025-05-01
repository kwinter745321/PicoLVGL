# display_driver.py
# Updated: 28 April 2025 for ST7796 display
#
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-724-gbf1107420 on 2025-02-19; Raspberry Pi Pico with RP2040
# Raspberry Pi Pico (RP2040)
# LVGL 9.3
#
# 
import lvgl as lv
import ili9xxx
import xpt2046_b

import machine
from machine import SPI, Pin, reset
import time
import os
import sdcard2 as sdcard
import fs_driver

# Initialize LVGL
lv.init()
print("Running LVGL %d.%d" % (lv.version_major(), lv.version_minor() )  )

# Initialize display  ILI9341 SPI=20M T=2M
spi = SPI(0, baudrate=20_000_000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
tspi = SPI(0, baudrate=2_000_000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
#sdspi = SPI(1, baudrate=2_000_000, sck=Pin(10), mosi=Pin(12), miso=Pin(11))

print("Init disp")
#disp = ili9xxx.Ili9341(spi=spi, dc=0, cs=17, rst=1, rot=1)
#disp = ili9xxx.Ili9488(spi=spi, dc=0, cs=17, rst=1, rot=0)
disp = ili9xxx.St7796(spi=spi, dc=0, cs=17, rst=1, rot=0)

disp.clear(0x000000)
print("Pause 1 sec.")
time.sleep(1)

#https://forum.lvgl.io/t/inconsistency-between-display-rotation-and-touchscreen-coordinate-rotation/20242/6

# screen
hres = 320
vres = 480
#Portrait
#disp_drv = lv.display_create(hres,vres)
# Landscape
disp_drv = lv.display_create(vres,hres)

scr = lv.screen_active()
#scr = lv.obj()
coords = None

###touch = xpt2046.Xpt2046_hw(spi=tspi,cs=21,rot=1)
touch = xpt2046_b.Xpt2046_hw(spi=tspi,cs=21,rot=0)

def scale_value(value, in_min, in_max, out_min, out_max):
  scaled_value = (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
  return scaled_value

@micropython.native
def tsread(indev_drv, data) -> int:
    global coords
    coords = touch.pos()
    if coords:
        x, y = coords
        #y = int(scale_value( y, 480, 1, 1, 480))
        #y = 480 - 1 - y
        #x = 320 - 1 - x
        coords = (y, x)    # Note: changed x,y
        print(coords)
        data.point.x, data.point.y = coords
        data.state = lv.INDEV_STATE.PRESSED
        return True
    data.state = lv.INDEV_STATE.RELEASED
    return False

# #indev for touch screen
indev_drv = lv.indev_create()
indev_drv.set_type(lv.INDEV_TYPE.POINTER)
indev_drv.set_read_cb(tsread)


# cs = machine.Pin(4, Pin.OUT)
# mi = machine.Pin(12, Pin.IN)
# mo = machine.Pin(11, Pin.OUT)
# sk = machine.Pin(10, Pin.OUT)
# cs = 1
# time.sleep(1)
# spi = SPI(1, baudrate=1_320_000, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
# time.sleep(1)
# sd = sdcard.SDCard(spi, machine.Pin(4, Pin.OUT), '/sd')
# 
# time.sleep(1)
# vfs = os.VfsFat(sd)
# os.mount(vfs, "/sd")
# print("SDCard drive:")
# os.chdir('/sd')
# print(os.listdir())
# # MUST----------------------- umount()
# 
# fs_drv = lv.fs_drv_t()
# fs_driver.fs_register(fs_drv,'S')

###############################################
# Reset Thonny
###############################################
    
#### Reset Button #####################
class HardReset():
    
    def __init__(self, scr):
        self.rbtn = None
        self.rlbl = None
        self.quitbtn = None
        self.scr = scr
        self.rbtn = lv.button(scr)
        #self.rbtn.set_pos(240,200)
        self.rbtn.set_style_bg_color(lv.palette_main(lv.PALETTE.RED),0)
        self.rlbl = lv.label(self.rbtn)
        self.rlbl.set_text("Reset")
        self.rlbl.center()
        self.rbtn.align_to(scr, lv.ALIGN.BOTTOM_RIGHT,-15,-15)
        self.rbtn.add_event_cb(self.reset_cb, lv.EVENT.CLICKED, None)

    def reset_cb(self, event):
        print("Clicked reset")
        self.startmb()
        
    def reset(self):
        reset()
        
    def show(self):
        global coords
        return coords
        
    def quitcb(self, event):
        print("quitting...")
        reset()

    def startmb(self):
        self.mb = lv.msgbox(self.scr)
        self.mb.add_title("Resets PICO")
        self.mb.add_text("Really reset the program?")
        self.mb.add_close_button()
        self.quitbtn = self.mb.add_footer_button("Reset")
        self.mb.set_style_border_width(5, 0)
        self.mb.set_style_border_color(lv.palette_main(lv.PALETTE.RED),0)
        self.quitbtn.add_event_cb(self.quitcb, lv.EVENT.CLICKED, None)

