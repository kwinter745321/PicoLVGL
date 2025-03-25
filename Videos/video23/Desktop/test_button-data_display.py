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

#### Button ##################
btn = lv.button(scr)
btn.set_size(100,50)
btn.center()
btn.add_style(btnstyle, 0)

lbl = lv.label(btn)
lbl.set_text("OFF")
lbl.center()
lbl.set_style_text_color(lv.color_hex(0),0)
lbl.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN | lv.STATE.DEFAULT)

# data we want to pass to the callback
data = "OPEN"

# callback
def btn_cb(event, data):
    btn =  event.get_target_obj()
    if btn:
        lbl = btn.get_child(0)
        lbl.set_text(data)
        print("Clicked button")

#  Explanation for this syntax:
#  https://forum.lvgl.io/t/how-to-pass-an-python-array-as-event-user-data/8641
btn.add_event_cb(lambda e:btn_cb(e, data), lv.EVENT.CLICKED, None)

###################################################
lv.screen_load(scr)
        
# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)

