# test_sdcard_spi.py
#
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-724-gbf1107420 on 2025-02-19; Raspberry Pi Pico with RP2040
# Raspberry Pi Pico (RP2040) or Pico2 (RP2350)
#
import sdcard2 as sdcard
import os
from machine import Pin, SPI
import time


cs = machine.Pin(13, Pin.OUT)
mi = machine.Pin(12, Pin.IN)
mo = machine.Pin(11, Pin.OUT)
sk = machine.Pin(10, Pin.OUT)
cs = 1

spi = SPI(1, baudrate=1_320_000, sck=Pin(10), mosi=Pin(11), miso=Pin(12))
sd = sdcard.SDCard(spi, machine.Pin(13, Pin.OUT), '/sd')

vfs = os.VfsFat(sd)
os.mount(vfs, "/sd")
print()
print("Virtual flash drive:")
print(os.listdir('/'))
print()
print("SDCard drive:")
os.chdir("/sd")
print(os.listdir())
#os.mkdir('testdir')
#
#os.umount("/sd")


                     
                     