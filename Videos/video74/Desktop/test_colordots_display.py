# test_colordots_display.py
#
# Created: 17 October 2025
# Revised: 22 January 2026
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.20.0-2510.gacfeb7b7e (1.24) on 2026-01-16;
# Raspberry Pi Pico with RP2040
# MicroPython v1.27.0-dirty on 2026-01-22;
# Raspberry Pi Pico W with RP2040
# MicroPython v1.28.0-preview.80.gb14d129a16.dirty on 2026-01-22;
# Raspberry Pi Pico2 with RP2350
# MicroPython v1.28.0-preview.80.gb14d129a16.dirty on 2026-01-22;
# Raspberry Pi Pico 2 W with RP2350
# LVGL 9.3

import lvgl as lv
from machine import reset, Pin
from display_driver import disp
import time
lv.init()

backlight = Pin(13,Pin.OUT)
backlight.on()

#### UI ####
scr = lv.obj()
scr.set_style_bg_color(lv.color_black(),0)
#scr.set_style_border_width(2, lv.PART.MAIN)
#scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),lv.PART.MAIN)
lv.screen_load(scr)
wd = disp.width - 2
ht = disp.height - 2
#### object container ####
cont = lv.obj(scr)
cont.set_style_bg_color(lv.color_black(), lv.PART.MAIN)
cont.set_style_border_width(0, lv.PART.MAIN)
cont.set_style_border_color(lv.color_black(), lv.PART.MAIN)
cont.set_size(wd, ht)
#cont.set_pos(0,0)
cont.set_style_pad_row(0,0)
cont.set_style_pad_column(0,0)
#cont.set_style_pad_all(0, lv.PART.MAIN)
cont.set_flex_flow(lv.FLEX_FLOW.ROW_WRAP)
cont.center()

#### add object balls with color ####
size = 40
col = wd // size
row = ht // size
print("Drawing objs: col:{} row:{}".format(col,row))
for i in range(0,col*row):
    obj = lv.obj(cont)
    obj.set_style_pad_all(0,0)
    obj.set_size(size,size)
    obj.set_style_radius(size, 0)
    obj.set_style_bg_color(lv.palette_main(i%19),0)
    #obj.set_style_bg_color(lv.color_hex(i),0)
    obj.set_style_border_color(lv.palette_main(i%19),0)
    obj.set_style_border_width(0,0)

#### Run the event loop ####
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)
