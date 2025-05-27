# test_buttonslider_display.py
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
from display_driver import disp
from micropython import const
from machine import Pin, reset
import time

SW1 = const(2)
SW2 = const(3)
SW3 = const(4)
SW4 = const(5)

pb1 = Pin(SW1, Pin.IN, Pin.PULL_UP)
pb2 = Pin(SW2, Pin.IN, Pin.PULL_UP)
pb3 = Pin(SW3, Pin.IN, Pin.PULL_UP)
pb4 = Pin(SW4, Pin.IN, Pin.PULL_UP)

###############################################
# UI
###############################################
 
# current screen
scr = lv.obj()
#h = HardReset(scr)

#scr.set_style_bg_color(lv.color_hex(0),0)
scr.set_style_border_width(2, 0)
scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),0)

### Style  ###################
btnstyle = lv.style_t()
btnstyle.init()
btnstyle.set_radius(5)
btnstyle.set_bg_opa(lv.OPA.COVER)
btnstyle.set_bg_color(lv.palette_main(lv.PALETTE.BLUE))
btnstyle.set_outline_width(2)
btnstyle.set_outline_color(lv.palette_main(lv.PALETTE.BLUE))
btnstyle.set_outline_pad(8)
 
#### btn callback ########### 
def btn_cb(event):
    btn = event.get_target_obj()
    if btn:
        lbl = btn.get_child(0)
        print("Clicked btn:",lbl.get_text() ) 
 
#### Button1 ##################
btn1 = lv.button(scr)
btn1.set_size(80,40)
btn1.set_pos(100,20)

lbl1 = lv.label(btn1)
lbl1.set_text("One")
lbl1.center()
lbl1.set_style_text_color(lv.color_hex(0),0)
lbl1.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN | lv.STATE.DEFAULT)

btn1.add_event_cb(btn_cb, lv.EVENT.CLICKED, None)

#### Button ##################
btn2 = lv.button(scr)
btn2.set_size(80,40)
btn2.set_pos(100,80)

lbl2 = lv.label(btn2)
lbl2.set_text("Two")
lbl2.center()
lbl2.set_style_text_color(lv.color_hex(0),0)
lbl2.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN | lv.STATE.DEFAULT)

btn2.add_event_cb(btn_cb, lv.EVENT.CLICKED, None)
#### Slider ##################
slider = lv.slider(scr)
slider.set_size(150,20)
slider.set_pos(100,150)
slider.set_style_bg_opa(200,lv.PART.MAIN)
slider.set_style_bg_color(lv.palette_main(lv.PALETTE.YELLOW), lv.PART.MAIN )
slider.set_style_bg_color(lv.palette_main(lv.PALETTE.PURPLE), lv.PART.INDICATOR | lv.STATE.FOCUSED )

lbl = lv.label(scr)
lbl.set_text("0")
lbl.align_to(slider, lv.ALIGN.BOTTOM_RIGHT, 20, 0)

#### pushbutton INDEV #####################
def update_label():
    val = slider.get_value()
    lbl.set_text(str(val))

def pb_read(indev, data):
    pb1pressed = pb1.value()
    pb2pressed = pb2.value()
    pb3pressed = pb3.value()
    pb4pressed = pb4.value()
    time.sleep_ms(50)
    if pb1pressed == 0:
        data.key = lv.KEY.RIGHT
        data.enc_diff = 1
    if pb2pressed == 0:
        data.key = lv.KEY.LEFT
        data.enc_diff = -1
    if pb4pressed == 0:
        data.key = lv.KEY.ENTER
        data.enc_diff = 0
    if pb3pressed == 0:
        data.state = lv.INDEV_STATE.PRESSED
    else:
        data.state = lv.INDEV_STATE.RELEASED
    update_label()

pb_drv = lv.indev_create()
pb_drv.set_type(lv.INDEV_TYPE.ENCODER)
pb_drv.set_read_cb(pb_read)
pb_drv.long_press_repeat_time = 50

btngrp = lv.group_create()
btngrp.add_obj(slider)
btngrp.add_obj(btn1)
btngrp.add_obj(btn2)
pb_drv.set_group(btngrp)
btngrp.editing = True  # Nav mode

###################################################
lv.screen_load(scr)
        

# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)