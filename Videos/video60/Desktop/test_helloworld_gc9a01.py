# test_helloworld_gc9a01.py
#
# Created: 17 October 2025
#
# Copyright (C) 2025 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.20.0-724-gbf1107420 on 2025-02-19;
# Raspberry Pi Pico with RP2040
# LVGL 9.1

import lvgl as lv
from machine import reset
import display_driver 
import time
lv.init()

#### UI ####
scr = lv.obj()
lv.screen_load(scr)

lbl = lv.label(scr)
lbl.set_text("Hello World")
lbl.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN)
lbl.center()

#### Run the event loop ####
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)
