# test_scale_display.py
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

import time

###############################################
# UI
###############################################
 
# current screen
scr = lv.obj()
try:
    from display_driver import HardReset
    h = HardReset(scr)
except ImportError:
    pass

#### Frame the screen #####################
#scr.set_style_bg_color(lv.color_hex(0),0)
scr.set_style_border_width(2, 0)
scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),0)

#### Scale ###########
# style = lv.style_t()
# style.init()
# style.set_line_color(lv.palette_main(lv.PALETTE.RED))

scale = lv.scale(scr)
#scale.add_style(style, lv.PART.ITEMS)
scale.set_range(10, 40)
scale.set_size(200, 60)
scale.center()
#scale.set_pos(50,50)

scale.set_total_tick_count(31)
scale.set_major_tick_every(10)
scale.set_style_length(5, lv.PART.ITEMS)
scale.set_style_length(10, lv.PART.INDICATOR)

#### Change colors for black background ########################
# scale.set_style_line_color(lv.palette_main(lv.PALETTE.BLUE),lv.PART.MAIN)
# scale.set_style_line_color(lv.palette_main(lv.PALETTE.RED),lv.PART.ITEMS)
# scale.set_style_line_color(lv.palette_main(lv.PALETTE.GREEN),lv.PART.INDICATOR)
# scale.set_style_text_color(lv.palette_main(lv.PALETTE.ORANGE),lv.PART.INDICATOR)
# scale.set_style_text_font(lv.font_montserrat_24,lv.PART.INDICATOR)

###################################################
lv.screen_load(scr)
        
# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)

