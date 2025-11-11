# test_button_display.py
#
# Created: 08 July 2025
# Updated: 10 November 2025
#
# Copyright (C) 2025 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.20.0-2510.gacfeb7b7e on 2025-11-09; linux [GCC 14.2.0] version
# LVGL 9.3

import lvgl as lv
import display_driver
from display_driver import display as disp
import time
lv.init()

###############################################
# UI
###############################################

# current screen
scr = lv.obj()
lv.screen_load(scr)

scr.set_style_bg_color(lv.color_hex(0),lv.PART.MAIN)
scr.set_style_border_width(2, lv.PART.MAIN)
scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),lv.PART.MAIN)

#### Subject #############################
subject1 = lv.subject_t()
subject1.init_int(10)

#### Slider ###############################
slider1 = lv.slider(scr)
slider1.center()

# Send slider1's value to subject1
slider1.bind_value(subject1)

#### Label ###############################      
label1 = lv.label(scr)
label1.align(lv.ALIGN.TOP_MID, 0,50)
label1.set_text("Progress")
label1.set_style_text_color(lv.color_white(), lv.PART.MAIN)
label1.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN)

#### Observer and Callback ###################################
def label_observer_cb(observer, subject):
    # subject is subject1
    if observer != None:
        lbl = observer.get_target_obj()
        lbl.set_text("Progress: {}".format( subject.get_int() ) )

# observer
observer = subject1.add_observer_obj(label_observer_cb, label1, None)

###################################################

def screen_exit(event):
    code = event.get_code()
    # display closed event
    if code == 41:
        import os
        os.system("stty echo")

disp.add_event_cb(screen_exit, lv.EVENT.ALL, None)
