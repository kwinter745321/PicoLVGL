# test_areabtn_display.py
# Updated: 27 May 2025
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-2504.g9fe842956 on 2025-04-04; Raspberry Pi Pico with RP2040
# Raspberry Pi Pico (RP2040)
# LVGL 9.3
#
#

#import display_driver
import lvgl as lv
from display_driver import disp, disp_drv, touch, HardReset
from micropython import const
from machine import Pin, reset
import time

SW1 = const(2)
SW2 = const(3)

pb1 = Pin(SW1, Pin.IN, Pin.PULL_UP)
pb2 = Pin(SW2, Pin.IN, Pin.PULL_UP)
###############################################
# UI
###############################################
 
# current screen
scr = lv.obj()
#h = HardReset(scr)

scr.set_style_bg_color(lv.color_hex(0),0)
scr.set_style_border_width(2, 0)
scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),0)

#### UI  ####################################
def btn1cb(event):
    print("btn1 pressed")

btn1 = lv.button(scr)
btn1.set_size(40,40)
btn1.set_pos(5,5)
btn1.add_event_cb(btn1cb, lv.EVENT.CLICKED, None)

def btn2cb(event):
    print("btn2 pressed")

btn2 = lv.button(scr)
btn2.set_size(40,40)
btn2.set_pos(75,75)
btn2.add_event_cb(btn2cb, lv.EVENT.CLICKED, None)
     
#### pb1 Momentary button #####################
lastbtn = 0

def pb_read(indev, data):
    global lastbtn
    pb1pressed = pb1.value()
    pb2pressed = pb2.value()
    data.btn_id = -1
    if pb1pressed == 0:
        # zeroth item in array
        data.btn_id = 0
    if pb2pressed == 0:
        # second item in array
        data.btn_id = 1
    if data.btn_id == -1:
        time.sleep_ms(100)
        return
    if pb1pressed == 0 or pb2pressed == 0:
        data.state = lv.INDEV_STATE.PRESSED
        lastbtn = data.btn_id
        #print("pb pressed:",lastbtn)
        time.sleep_ms(100)
    else:
        data.state = lv.INDEV_STATE.RELEASED    

pb_drv = lv.indev_create()
pb_drv.set_type(lv.INDEV_TYPE.BUTTON)
pb_drv.set_read_cb(pb_read)

# point array
# {15,20}, {75,80}
pa1 = lv.point_t()
pa1.x,pa1.y = (15,20)
pa2 = lv.point_t()
pa2.x,pa2.y = (85,85)
# pa1 is zeroth item in array
pb_drv.set_button_points([pa1,pa2])

###################################################
lv.screen_load(scr)
        

# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)