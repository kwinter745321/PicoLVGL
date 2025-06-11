# test_flex_display.py
#
# Updated: 09 June 2025
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.25.0 on 2025-06-08; Raspberry Pi Pico 2 W with RP2350
# LVGL 9.3 
#
# Tested with RPI_PICO2_W USB board


import lvgl as lv
from display_driver import disp, disp_drv, touch
from machine import Pin,reset

import time
import random

lv.init()

###############################################
# UI
###############################################
 
# current screen
scr = lv.obj()
#h = HardReset(scr)

scr.set_style_bg_color(lv.color_hex(0),0)
scr.set_style_border_width(2, 0)
scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),0)

#
# A simple row and a column layout with flexbox
#

# Create a container with ROW flex direction
cont_row = lv.obj(scr)
cont_row.set_size(300, 75)
cont_row.align(lv.ALIGN.TOP_MID, 0, 5)
cont_row.set_flex_flow(lv.FLEX_FLOW.ROW)

# Create a container with COLUMN flex direction
cont_col = lv.obj(scr)
cont_col.set_size(200, 150)
cont_col.align_to(cont_row, lv.ALIGN.OUT_BOTTOM_MID, 0, 5)
cont_col.set_flex_flow(lv.FLEX_FLOW.COLUMN)

option = True

def do_grow(obj):
    if i == 1:
        obj.set_flex_grow(2)
    else:
        obj.set_flex_grow(1)

for i in range(6):
    # Add items to the row
    rowbtn = lv.button(cont_row)
    if option:
        do_grow(rowbtn)

    label = lv.label(rowbtn)
    label.set_text("#{:d}".format(i))
    label.set_style_text_color(lv.color_black(), lv.PART.MAIN )
    label.center()

    # Add items to the column
    colbtn = lv.button(cont_col)
    colbtn.set_height(40)
    colbtn.set_size(lv.pct(100), lv.SIZE_CONTENT)
    if option:
        do_grow(colbtn)
    
    label = lv.label(colbtn)
    label.set_text("Item-{:d}".format(i))
    label.set_style_text_color(lv.color_black(), lv.PART.MAIN )
    label.center()
    
###################################################
lv.screen_load(scr)
        

# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)