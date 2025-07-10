# test_button_display.py
#
# Created: 08 July 2025
#
# Copyright (C) 2025 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.25.0 on 2025-07-08; Raspberry Pi Pico with RP2040
# MicroPython v1.25.0 on 2025-07-08; Raspberry Pi Pico W with RP2040
# MicroPython v1.25.0 on 2025-07-08; Raspberry Pi Pico2 with RP2350
# MicroPython v1.25.0 on 2025-07-08; Raspberry Pi Pico 2 W with RP2350
# LVGL 9.4

import lvgl as lv
from machine import reset
from display_driver import disp
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

#### END UI ###############################################
#subject1.set_int(30)

# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)
