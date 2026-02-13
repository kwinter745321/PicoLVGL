# display_driver.py
# Updated:    08 May 2025 to support the four Orientation modes
# Updated:    17 October 2025 include GC9A01 driver
# Updated:    02 November 2025 include ST7735 display from ST77xx driver
# Updated by: KWServices
#
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-2504.g9fe842956 on 2025-04-04; Raspberry Pi Pico2 with RP2350
# Raspberry Pi Pico (RP2040)
# LVGL 9.3
#
# 
import lvgl as lv
#import ili9xxx
import st77xx
#import xpt2046
import machine
from machine import SPI, Pin, reset, SoftSPI, SoftI2C, I2C
from cst328 import CST328

import time
import sys

#import fs_driver

# Initialize LVGL
lv.init()
print("Running LVGL %d.%d" % (lv.version_major(), lv.version_minor() )  )

LCD_SCLK = 10
LCD_MOSI = 11
LCD_MISO = 12


# Initialize display  ILI9341 SPI=20M T=2M
spi = SoftSPI(baudrate=60_000_000, sck=Pin(10), mosi=Pin(11), miso=Pin(12) )
#spi = SPI(0, baudrate=20_000_000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
#tspi = SPI(0, baudrate=2_000_000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
#sdspi = SPI(1, baudrate=2_000_000, sck=Pin(10), mosi=Pin(12), miso=Pin(11))

PORTRAIT = const(0)
LANDSCAPE = const(1)
INV_PORTRAIT = const(2)
INV_LANDSCAPE = const(3)

#### disp object ###################################
backlight = Pin(16,Pin.OUT)
backlight.on()

LCD_CS = 13
LCD_DC = 14
LCD_RST = 15
LCD_BL = 16

time.sleep_ms(255)
# Waveshare 1.44 128x128
#disp = st77xx.St7735( spi=spi, dc=8, cs=9, rst=12, bl=13, rot=0, res=(128,128), model="1.44",bgr=False )
# Waveshare 1.8
#disp = st77xx.St7735( spi=spi, dc=8, cs=9, rst=12, bl=13, rot=0, res=(128,160), model="greentab", bgr=False)
# HiLetgo 1.8 (Must use HW SPI)
#disp = st77xx.St7735( spi=spi, dc=0, cs=17, rst=1, bl=2, rot=0, res=(128,160), model="redtab", bgr=False)
# WeAct 1.8
#disp = st77xx.St7735( spi=spi, dc=8, cs=9, rst=12, bl=13, rot=0, res=(128,160), model="greentab", bgr=False)
# Xiia 2.4
#disp = ili9xxx.Ili9341(spi=spi, dc=8, cs=9, rst=12, rot=ILI9341_LANDSCAPE)
# 1.3
#disp = st77xx.St7789( spi=spi, dc=8, cs=9, rst=12, bl=13, rot=ST77XX_PORTRAIT, res=(240,320), model=None)
disp = st77xx.St7789( spi=spi, dc=14, cs=13, rst=15, bl=16, rot=1, res=(240,320), model='big')

#disp = ili9xxx.Gc9a01(spi=spi, dc=0, cs=17, rst=1, rot=ILI9341_PORTRAIT)
#disp = ili9xxx.Ili9341(spi=spi, dc=0, cs=17, rst=1, rot=ILI9341_LANDSCAPE)
#disp.set_model("big")  # uncomment for ILI9341 2.8 and 3.2 inch display
#disp = ili9xxx.St7796(spi=spi, dc=0, cs=17, rst=1, rot=ST7796_PORTRAIT)
#print("Create 'disp' object for Display:",disp.display_type)
#print("Pause 1 sec.")
#time.sleep(1)

#### screen object ###################################
hres = disp.width   
vres = disp.height

disp_drv = lv.display_create(hres,vres)
scr = lv.screen_active()


#### touchscreen object ###################################
I2C_SCL = 7
I2C_SDA = 6
i2c = I2C(1,scl = Pin(7), sda = Pin(6), freq = 400_000)
touch = CST328(i2c, disp.width, disp.height, rotation=disp.rot)

def indev_drv_read_cb(indev_drv, data):
    data.state = 0
    if touch.read_touch() == True:
        coords =  touch.get_coords()
        if coords != None:
            x, y = coords[0]["x"],coords[0]["y"]
            #print(x,y,touch.raw2px(x,y) )
            x,y = touch.raw2px(x,y)
            data.point.x = x
            data.point.y = y
            data.state = 1
            
# #indev for touch screen
indev_drv = lv.indev_create()
indev_drv.set_type(lv.INDEV_TYPE.POINTER)
indev_drv.set_read_cb(indev_drv_read_cb)

