# test_scalecircle_display.py
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
import gc
import time
#import random

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

#### Scale ##############
scale = lv.scale(scr)
scale.set_range(10, 40)
scale.set_pos(100,10)
scale.set_size(150, 150)
scale.set_mode(lv.scale.MODE.ROUND_INNER)
scale.set_style_bg_opa(lv.OPA.COVER, lv.PART.MAIN)
scale.set_style_bg_color(lv.color_white(), lv.PART.MAIN)
#scale.set_style_bg_color(lv.color_black(), lv.PART.MAIN)

scale.set_total_tick_count(31)
scale.set_major_tick_every(5)
scale.set_style_line_width(1, lv.PART.ITEMS)
scale.set_style_line_width(1, lv.PART.INDICATOR)
scale.set_style_length(5, lv.PART.ITEMS)
scale.set_style_length(10, lv.PART.INDICATOR)

#### Line (Dial for the Scale) ##############
needle_line = lv.line(scale)
needle_line.set_style_line_width(6, lv.PART.MAIN)

# length of the needle is 40 pixels
scale.set_line_needle_value( needle_line, 40, 22)

# #### Change colors for black background ########################
# scale.set_style_arc_color(lv.palette_main(lv.PALETTE.BLUE),lv.PART.MAIN)
# scale.set_style_arc_width(3,lv.PART.MAIN)
# scale.set_style_line_color(lv.palette_main(lv.PALETTE.RED),lv.PART.ITEMS)
# scale.set_style_line_width(3,lv.PART.ITEMS)
# scale.set_style_line_color(lv.palette_main(lv.PALETTE.GREEN),lv.PART.INDICATOR)
# scale.set_style_line_width(3,lv.PART.INDICATOR)
# scale.set_style_text_color(lv.palette_main(lv.PALETTE.ORANGE),lv.PART.INDICATOR)
# scale.set_style_text_font(lv.font_montserrat_16,lv.PART.INDICATOR)
# needle_line.set_style_line_color(lv.palette_main(lv.PALETTE.RED), lv.PART.MAIN)

###################################################
lv.screen_load(scr)
        
import time
import gc

# gc.collect()
# pos = 10
# done = False
# while not done:
#     lv.timer_handler()
#     time.sleep_ms(140)
#     gc.collect()
#     scale.set_line_needle_value(needle_line ,40 ,pos )
#     pos += 1
#     if pos > 40:
#         done = True