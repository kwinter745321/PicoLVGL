# test_font-demo_fs.py
#
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-724-gbf1107420 on 2025-02-19; Raspberry Pi Pico with RP2040
# Raspberry Pi Pico (RP2040)
# LVGL 9.1                    https://docs.lvgl.io/9.1/
# LVGL 9.3                    https://docs.lvgl.io/master/
#

import display_driver
import lvgl as lv
import machine
from machine import SPI, Pin,
import sdcard2 as sdcard
import fs_driver
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

#### Mound SDCard as /sd ################
vfs = os.VfsFat(sd)
os.mount(vfs, "/sd")

#### List files/directories on /sd ################
print("SDCard drive:")
os.chdir('/sd')
print(os.listdir())
# ----when done try doing this command in REPL or program
#os.umount('/sd')

#### Register the SDCard as LVGL file system device 'S:' ##############
fs_drv = lv.fs_drv_t()
fs_driver.fs_register(fs_drv,'S')

###############################################
# UI
###############################################
 
# current screen
scr = lv.obj()
try:
    from display_driver import HardReset
    h = HardReset(scr)
except ImportError:
    pass

scr.set_style_bg_color(lv.color_hex(0),0)
scr.set_style_border_width(2, 0)
scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),0)

#### Label1 using embedded font montserrat-24 #####################
label1 = lv.label(scr)
label1.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN)
label1.set_pos(10,60)
label1.set_text("montserrat_24")
label1.set_style_text_color(lv.palette_main(lv.PALETTE.RED), lv.PART.MAIN)

#### Label2 using external font alexbrush-reg-36-2 #########
label2 = lv.label(scr)
alexbrush_reg_36 = lv.binfont_create("S:font/alexbrush-reg-36-2.bin" )
label2.set_style_text_font(alexbrush_reg_36, lv.PART.MAIN)
label2.set_pos(10,100)
label2.set_text("alexbrush-reg-36-2")
label2.set_style_text_color(lv.color_white(), lv.PART.MAIN)

#### Label3 using external font chunkfive-reg-24-2 #########
label3 = lv.label(scr)
chunkfive_reg_24 = lv.binfont_create("S:font/chunkfive-reg-24-2.bin" )
label3.set_style_text_font(chunkfive_reg_24, lv.PART.MAIN)
label3.set_pos(10,160)
label3.set_text(" chunkfive-reg-24-2")
label3.set_style_text_color(lv.palette_main(lv.PALETTE.BLUE), lv.PART.MAIN)

###################################################
lv.screen_load(scr)
        
# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)
