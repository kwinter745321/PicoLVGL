# test_button_display.py
#
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-724-gbf1107420 on 2025-02-19; Raspberry Pi Pico with RP2040
# Raspberry Pi Pico (RP2040)
# LVGL 9.1                    https://docs.lvgl.io/9.1/
#
#

import display_driver
import lvgl as lv
from display_driver import HardReset

import time

###############################################
# UI
###############################################
 
# current screen
scr = lv.obj()

#scr.set_style_bg_color(lv.color_hex(0),0)
scr.set_style_border_width(2, 0)
scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),0)
h = HardReset(scr)

### Style  ###################
btnstyle = lv.style_t()
btnstyle.init()
btnstyle.set_radius(5)
btnstyle.set_bg_opa(lv.OPA.COVER)
btnstyle.set_bg_color(lv.palette_main(lv.PALETTE.BLUE))
btnstyle.set_outline_width(2)
btnstyle.set_outline_color(lv.palette_main(lv.PALETTE.BLUE))
btnstyle.set_outline_pad(8)
 
#### Buttons ##################
btn1 = lv.button(scr)
btn1.set_size(100,50)
btn1.set_pos(80,60)
btn1.add_style(btnstyle, 0)
lbl1 = lv.label(btn1)
lbl1.set_text("One")
lbl1.center()
lbl1.set_style_text_color(lv.color_hex(0),0)
lbl1.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN | lv.STATE.DEFAULT)

btn2 = lv.button(scr)
btn2.set_size(100,50)
btn2.set_pos(80,150)
btn2.add_style(btnstyle, 0)
lbl2 = lv.label(btn2)
lbl2.set_text("Two")
lbl2.center()
lbl2.set_style_text_color(lv.color_hex(0),0)
lbl2.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN | lv.STATE.DEFAULT)

def btn_cb(event):
    btn =  event.get_target_obj()
    if btn:
        lbl = btn.get_child(0)
        print("Clicked button; named: ",lbl.get_text())
        
btn1.add_event_cb(btn_cb, lv.EVENT.CLICKED, None)
btn2.add_event_cb(btn_cb, lv.EVENT.CLICKED, None)

###################################################
lv.screen_load(scr)
        
# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)

