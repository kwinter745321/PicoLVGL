# sdcard_driver.py
# Created:    10 February 2026
#
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-2504.g9fe842956 on 2025-04-04; Raspberry Pi Pico2 with RP2350
# Raspberry Pi Pico (RP2040)
# LVGL 9.3
#
#
from machine import Pin, SoftSPI
from sdcard import SDCard
import time
import os
#### filesystem (sdcard) object ###################################
sdspi = SoftSPI(baudrate=1_320_000, polarity=0, phase=0, sck=Pin(19), mosi=Pin(20), miso=Pin(21))
# Configuration
cs = Pin(24, Pin.OUT)
sd = SDCard(sdspi, cs)
try:
    print(os.listdir("/sd"))
except OSError: 
    os.mount(sd, "/sd")
    #print(os.listdir("/sd"))