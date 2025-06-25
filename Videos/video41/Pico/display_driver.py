# display_driver.py
# Updated:    24 June 2025 to support CTP_ft6x36 driver
# Updated by: KWServices
#
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-2504.g9fe842956 on 2025-04-04; Raspberry Pi Pico with RP2040
# Raspberry Pi Pico (RP2040)
# LVGL 9.3
#
# 
import lvgl as lv
import ili9xxx
#import xpt2046
from ctp_ft6x36 import ft6x36

import machine
from machine import SPI, Pin, reset
import time
#import os
#import sdcard2 as sdcard
#import fs_driver

#####################################
#USE_CTP_DRIVER = False
USE_CTP_DRIVER = True
#####################################

# Initialize LVGL
lv.init()
print("Running LVGL %d.%d" % (lv.version_major(), lv.version_minor() )  )

# Initialize display  ILI9341 SPI=20M T=2M
spi = SPI(0, baudrate=60_000_000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
if USE_CTP_DRIVER == False:
    tspi = SPI(0, baudrate=2_000_000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
#sdspi = SPI(1, baudrate=2_000_000, sck=Pin(10), mosi=Pin(12), miso=Pin(11))

ILI9341_PORTRAIT = 0
ILI9341_LANDSCAPE = 1
ILI9341_INVERTED_PORTRAIT = 2
ILI9341_INVERTED_LANDSCAPE = 3

ST7796_PORTRAIT = 1
ST7796_LANDSCAPE = 0
ST7796_INVERTED_PORTRAIT = 3
ST7796_INVERTED_LANDSCAPE = 2

#### disp object ###################################
#disp = ili9xxx.Ili9341(spi=spi, dc=0, cs=17, rst=1, rot=ILI9341_LANDSCAPE)
#disp.set_model("big")  # uncomment for ILI9341 2.8 and 3.2 inch display
disp = ili9xxx.St7796(spi=spi, dc=0, cs=17, rst=1, rot=ST7796_LANDSCAPE  )
print("Create 'disp' object for Display:",disp.display_type)
print("Pause 1 sec.")
time.sleep(1)

#### screen object ###################################
hres = disp.width   
vres = disp.height

disp_drv = lv.display_create(hres,vres)
scr = lv.screen_active()

# ILI9341
if USE_CTP_DRIVER == False:
    if disp.display_type == 'st7796':
        touch = xpt2046.Xpt2046_hw(spi=tspi,cs=21,width=(320),height=(480),rot=disp.rot)
    else:
        touch = xpt2046.Xpt2046_hw(spi=tspi,cs=21,width=(240),height=(320),rot=disp.rot)

#touch = None
#p = None

# ST7796 CTP_ft6x36 touch
if USE_CTP_DRIVER == True:
    print("Rotation:",disp.rot)
    if   disp.rot==0: touch=ft6x36(0,sda=20,scl=21,reset=7,irq=6,width=480,height=320,inv_x=True,inv_y=False,swap_xy=True)           
    elif disp.rot==1: touch=ft6x36(0,sda=20,scl=21,reset=7,irq=6,width=480,height=320,inv_x=False,inv_y=False,swap_xy=False)  
    elif disp.rot==2: touch=ft6x36(0,sda=20,scl=21,reset=7,irq=6,width=480,height=320,inv_x=False,inv_y=True,swap_xy=True)         
    else: touch=ft6x36(0,sda=20,scl=21,reset=7,irq=6,width=480,height=320,inv_x=True,inv_y=True,swap_xy=False)   
    
coords = None
dim = (hres,vres)

if USE_CTP_DRIVER == False:
    print("dim[0] and dim[1]:",dim[0],dim[1])

    def transform9341(p,rot):
        x, y = p
        if   rot==0: coords = x,dim[1]-y-1       
        elif rot==1: coords = x,y      
        elif rot==2: coords = x,dim[1]-y-1 
        else:        coords = x,y        
        return coords

    def transform9341big(p,rot):
        x, y = p
        if   rot==0: coords = dim[0]-x,dim[1]-y     
        elif rot==1: coords = x,dim[1]-y     
        elif rot==2: coords = dim[0]-x,dim[1]-y 
        else:        coords = x,dim[1]-y        
        return coords

    def transform7796(p,rot):
        x, y = p
        if   rot==0: coords = dim[0]-y,x            
        elif rot==1: coords = y,x
        elif rot==2: coords = dim[0]-y,x         
        else:        coords = y,x       
        return coords

    @micropython.native
    def tsread(indev_drv, data) -> int:
        global coords
        p = touch.getTouchValue()
        if p != None:
            x = p.x
            y = p.y
            coords = (x,y)
            if coords:
                if disp.display_type == "st7796":
                    coords = transform7796(coords,disp.rot)
                else:
                    if disp.model == "big":
                        coords = transform9341big(coords,disp.rot)
                    else:
                        coords = transform9341((x,y),disp.rot)
            data.point.x, data.point.y = coords
            data.state = lv.INDEV_STATE.PRESSED
            return True
        data.state = lv.INDEV_STATE.RELEASED
        return False

#indev for touch screen
indev_drv = lv.indev_create()
indev_drv.set_type(lv.INDEV_TYPE.POINTER)
if USE_CTP_DRIVER == False:
    indev_drv.set_read_cb(tsread)

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
