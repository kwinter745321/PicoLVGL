# test_colordots_gc9a01.py
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

#### object container ####
cont = lv.obj(scr)
cont.set_size(128, 160)
cont.set_pos(0,0)
cont.set_style_pad_row(0,0)
cont.set_style_pad_column(0,0)
cont.set_flex_flow(lv.FLEX_FLOW.ROW_WRAP)

#### add object balls with color ####
size = 24
for i in range(0,20):
    for cnt in range(0,1):
        obj = lv.obj(cont)
        obj.set_style_pad_all(0,0)
        obj.set_size(size,size)
        obj.set_style_radius(size, 0)
        obj.set_style_bg_color(lv.palette_main(i),0)
        obj.set_style_border_color(lv.palette_main(i),0)
        obj.set_style_border_width(0,0)

#### Run the event loop ####
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)
