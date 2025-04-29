# test_xpt2046_b.py
#
# Created:    28 April 2025 for 320x480 displays
#
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-2504.g9fe842956 on 2025-04-04; Raspberry Pi Pico2 with RP2350
# Raspberry Pi Pico (RP2040)
# LVGL 9.3

import sys
sys.path.append('.')

import lvgl as lv
import ili9xxx
import machine
from machine import SPI, Pin, reset
import time

from xpt2046_b import *

TP_CLK_PIN=18
TP_MOSI_PIN=19
TP_MISO_PIN=16

TP_CS_PIN=21  # Make sure this is the T_CS for Touch

# make sure the SPI is same as used for Display
spi=machine.SPI(
    0,
    baudrate=2_000_000, # the chip does not handle more than 2MHz (!)
    polarity=0,
    phase=0,
    sck=machine.Pin(TP_CLK_PIN, machine.Pin.OUT),
    mosi=machine.Pin(TP_MOSI_PIN, machine.Pin.OUT),
    miso=machine.Pin(TP_MISO_PIN, machine.Pin.OUT),
)

tsc=Xpt2046_hw(spi=spi,cs=TP_CS_PIN,rot=0)

for i in range(100000):
    if p:=tsc.pos(): print(p)

print("done")