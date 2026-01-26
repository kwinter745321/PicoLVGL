# test_hello_display.py
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
#import display_driver
from display_driver import disp
import time
lv.init()

backlight = Pin(13,Pin.OUT)
backlight.on()

#### UI ####
scr = lv.obj()
lv.screen_load(scr)

scr.set_style_bg_color(lv.color_hex(0),lv.PART.MAIN)

red = lv.palette_main(lv.PALETTE.RED)
blue = lv.palette_main(lv.PALETTE.BLUE)
yellow = lv.palette_main(lv.PALETTE.YELLOW)
green = lv.palette_main(lv.PALETTE.GREEN)

btn = lv.button(scr)
btn.set_size(120,40)
btn.set_style_bg_color(blue,0)
btn.center()

lbl = lv.label(btn)
lbl.set_text("Hello")
lbl.set_style_text_color(lv.color_black(),0)
lbl.set_style_text_font(lv.font_montserrat_24,0)
lbl.center()

#### Border
scr.set_style_border_width(2, lv.PART.MAIN)
scr.set_style_border_color(green,lv.PART.MAIN)

#### Rounded Border for 172x320 display
# container = lv.obj(scr)
# container.set_size(disp.width,disp.height)
# container.center()
# 
# style = lv.style_t()
# style.init()
# style.set_bg_opa(lv.OPA.TRANSP) # Transparent background
# style.set_border_color(green) 
# style.set_border_width(3)
# style.set_radius(20) 
# 
# container.add_style(style, lv.PART.MAIN)
