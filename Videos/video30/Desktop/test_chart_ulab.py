# test_chart_ulab.py
#
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-2504.g9fe842956 on 2025-04-04; Raspberry Pi Pico2 with RP2350
# Raspberry Pi Pico (RP2040)
# LVGL 9.3
# 
# Initialize

import display_driver
import lvgl as lv

# not available in simulator
from ulab import numpy as np

# Create a button with a label

import random

scr = lv.obj()
try:
    from display_driver import HardReset
    h = HardReset(scr)
except ImportError:
    pass

scr.set_style_bg_color(lv.color_hex(0),0)
scr.set_style_border_width(2, 0)
scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),0)

#### UI ##################################################

# number of data points
datacount = 10


#### Chart ########################################
#
chrt_wd = 240
chrt_ht = 140

chrtstyle = lv.style_t()
chrtstyle.init()
chrtstyle.set_bg_opa(lv.OPA.COVER)
chrtstyle.set_bg_color(lv.color_black() )

chrt = lv.chart(scr)
chrt.set_pos(50,5)
chrt.set_size( chrt_wd, chrt_ht)
chrt.add_style(chrtstyle, 0)
chrt.add_flag(lv.obj.FLAG.OVERFLOW_VISIBLE)
chrt.set_type(lv.chart.TYPE.SCATTER)
#### provide area for the axis values
chrt.set_style_outline_pad(max(50, 50, 50), lv.PART.MAIN )
chrt.set_style_outline_width(-1, lv.PART.MAIN )
# LVGL 9.3
chrt.set_axis_range(lv.chart.AXIS.PRIMARY_X, 0, 10)
chrt.set_axis_range(lv.chart.AXIS.PRIMARY_Y, 0, 100)
# LVGL 9.0
#chrt.set_range(lv.chart.AXIS.PRIMARY_X, 0, 10)
#chrt.set_range(lv.chart.AXIS.PRIMARY_Y, 0, 100)

#### AXIS #############################################
# Add ticks and label to every axis
xaxis = lv.scale(chrt)
xaxis.set_size( chrt_wd, lv.pct(100) )
xaxis.set_style_line_width(0, lv.PART.MAIN)
xaxis.set_mode(lv.scale.MODE.HORIZONTAL_BOTTOM)
xaxis.set_align(lv.ALIGN.BOTTOM_MID)
xaxis.set_y(130)
xaxis.set_range(0,datacount)
xaxis.set_total_tick_count(10)
xaxis.set_major_tick_every(3)
xaxis.set_style_text_color(lv.palette_main(lv.PALETTE.YELLOW), lv.PART.INDICATOR)
xaxis.set_style_text_font(lv.font_montserrat_24, lv.PART.INDICATOR)

yaxis = lv.scale(chrt)
yaxis.set_size( chrt_ht, lv.pct(100))
yaxis.set_style_line_width(0, lv.PART.MAIN)
yaxis.set_mode(lv.scale.MODE.VERTICAL_LEFT)
yaxis.set_align(lv.ALIGN.LEFT_MID)
yaxis.set_x(-150)
yaxis.set_total_tick_count(7)
yaxis.set_major_tick_every(2)
yaxis.set_style_text_color(lv.palette_main(lv.PALETTE.YELLOW), lv.PART.INDICATOR)
yaxis.set_style_text_font(lv.font_montserrat_24, lv.PART.INDICATOR)

#### Data Series objects and set the color
ser1 = chrt.add_series(lv.palette_main(lv.PALETTE.RED), lv.chart.AXIS.PRIMARY_Y)
ser2 = chrt.add_series(lv.palette_main(lv.PALETTE.GREEN), lv.chart.AXIS.PRIMARY_Y)

#### We do not want the screen to scroll
chrt.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)

#### Update Mode
chrt.set_update_mode(lv.chart.UPDATE_MODE.SHIFT)

#### Button Action #######################################################

xarr = []
yarr1 = []
yarr2 = []
a = None

# LVGL 9.3 code
def update_data():
    xarr.clear()
    yarr1.clear()
    yarr2.clear()
    for i in range(datacount):
        d1 = 70 + random.randint(-20,20)
        #d1 = int(70 + i)
        d2 = 50 + random.randint(-10,10)
        xarr.append(i)
        yarr1.append(d1)
        yarr2.append(d2)
    ########################################
    y_min = 40
    y_max = 90
    #### ULAB ####################################
    ny1 = np.array(yarr1, dtype=np.uint8)
    ny2 = np.array(yarr2, dtype=np.uint8)
    print("ny1:",ny1)
    miny = np.minimum(ny1, ny2)
    maxy = np.maximum(ny1, ny2)
    print("miny:",miny)
    y_min = np.min(miny)
    y_max = np.max(maxy)
    ##########################################
    print("y_min,y_max:",y_min,y_max)
    chrt.set_axis_range(lv.chart.AXIS.PRIMARY_Y, y_min, y_max)
    yaxis.set_range(y_min,y_max)
    chrt.set_series_ext_x_array(ser1, xarr)
    chrt.set_series_ext_y_array(ser1, yarr1)
    chrt.set_series_ext_x_array(ser2, xarr)
    chrt.set_series_ext_y_array(ser2, yarr2)
    chrt.refresh()
    print()

# use this if you are running LVGL 9.0 or 9.1
# def update_data():
#     xarr.clear()
#     yarr1.clear()
#     yarr2.clear()
#     for i in range(datacount):
#         d1 = 70 + random.randint(-20,20)
#         #d1 = int(70 + i)
#         d2 = 50 + random.randint(-10,10)
#         xarr.append(i)
#         yarr1.append(d1)
#         yarr2.append(d2)
#     ########################################
#     y_min = 40
#     y_max = 90
#     #### ULAB ####################################
#     ##########################################
#     print("y_min,y_max:",y_min,y_max)
#     chrt.set_range(lv.chart.AXIS.PRIMARY_Y, y_min, y_max)
#     yaxis.set_range(y_min,y_max)
#     chrt.set_ext_x_array(ser1, xarr)
#     chrt.set_ext_y_array(ser1, yarr1)
#     chrt.set_ext_x_array(ser2, xarr)
#     chrt.set_ext_y_array(ser2, yarr2)
#     chrt.refresh()
#     print()

### Button  ###################
btnstyle = lv.style_t()
btnstyle.init()
btnstyle.set_radius(5)
btnstyle.set_bg_opa(lv.OPA.COVER)
btnstyle.set_bg_color(lv.palette_main(lv.PALETTE.BLUE))
btnstyle.set_outline_width(2)
btnstyle.set_outline_color(lv.color_white())
btnstyle.set_outline_pad(4)

btn = lv.button(scr)
btn.set_pos(10,190)
btn.add_style(btnstyle, 0)
lbl = lv.label(btn)
lbl.set_text("Update")
lbl.set_style_text_color(lv.color_black(),0)
lbl.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN )

def btn_cb(event):
    print("Update data in the chart")
    update_data()      
        
btn.add_event_cb(btn_cb, lv.EVENT.CLICKED, None)
###################################################
lv.screen_load(scr)