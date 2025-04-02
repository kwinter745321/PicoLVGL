# test_imsage_sdcard.py
#
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-724-gbf1107420 on 2025-02-19; Raspberry Pi Pico with RP2040
# Raspberry Pi Pico (RP2040) or Pico2 (RP2350)
# LVGL 9.1                    https://docs.lvgl.io/9.1/
# LVGL 9.3                    https://docs.lvgl.io/master/
#

import display_driver
import lvgl as lv
import machine
from machine import SPI, Pin,
import sdcard2 as sdcard
import os
import time

#### Define SDCard on SPI-1 ###########
cs = machine.Pin(13, Pin.OUT)
miso = machine.Pin(12, Pin.IN)
mosi = machine.Pin(11, Pin.OUT)
sck = machine.Pin(10, Pin.OUT)
cs = 1

spi = SPI(1, baudrate=1_320_000, sck=sck, mosi=mosi, miso=miso)
sd = sdcard.SDCard(spi, machine.Pin(4, Pin.OUT), '/sd')

# Discussion on power
# Based on: https://github.com/micropython/micropython/issues/12105
#### Mound SDCard as /sd ################
vfs = os.VfsFat(sd)
os.mount(vfs, "/sd")

#### List files/directories on /sd ################
print("SDCard drive:")
os.chdir('/sd')
print(os.listdir())

###############################################
# UI
###############################################
print()
print("UI Begin")
# current screen
scr = lv.obj()
try:
    from display_driver import HardReset
    h = HardReset(scr)
except ImportError:
    pass

#### Image Routines #####################
import gc
gc.collect()
print(gc.mem_free())

def getImage(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    return data
                  
img1 = None
def showImage(filename):
    global img1
    try:
        png_data = getImage(filename)
        
        img = lv.image_dsc_t({
        'data_size': len(png_data),
        'data': png_data })

        img1 = lv.image(scr)
        img1.set_src(img)
        img1.align(lv.ALIGN.CENTER, 0, 0)
    except:
        print("could not find image file")
        #h.reset()
    
def scaleImage(obj,factor):
    amount = int(256 * factor)
    obj.set_scale(amount)
    
def rotateImage(obj, angle):
    obj.set_rotation(10 * angle)

def turnImage(obj):
    for a in range(0,375,15):
        rotateImage(obj, a)
        gc.collect()
        time.sleep(0.1)
        
def removeImage(obj):
    lv.image.delete(obj)
    gc.collect()
    
#### Main ###############################################
filename = "/sd/dir1/cog1.png"

showImage(filename)
print(gc.mem_free())

lv.screen_load(scr)

if img1 != None:
#     scaleImage(img1, 2)
#     turnImage(img1)
#     # 
#     time.sleep(2)
    removeImage(img1)
    print(gc.mem_free())
    filename = "/sd/dir1/R5.png"
    showImage(filename)
    gc.collect()
    scaleImage(img1, 1.5)
    gc.collect()
#     time.sleep(4)
#     removeImage(img1)

# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)

#filename = "/sd/dir1/R5.png"
#showImage(filename)
#removeImage(img1)
