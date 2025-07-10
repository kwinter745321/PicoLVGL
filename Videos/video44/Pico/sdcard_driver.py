# sdcard_driver.py
#
# Updated:  08 July 2025
#
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.25.0 on 2025-07-08; Raspberry Pi Pico with RP2040
# LVGL 9.4
#

from machine import Pin, SPI
import sdcard2 as sdcard
import os
import vfs

cs = Pin(13, Pin.OUT)
mi = Pin(12, Pin.IN)
mo = Pin(11, Pin.OUT)
sk = Pin(10, Pin.OUT)
cs = 1
time.sleep(1)
spi = SPI(1, baudrate=1_320_000, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
time.sleep(1)
sd = sdcard.SDCard(spi, Pin(13, Pin.OUT), '/sd')

try:
    vfs.mount(sd, "/sd")
    os.chdir('/sd')
    print(os.listdir("/"))
    print("Mounted /sd")
except ValueError:
    print("SDCard error:")
