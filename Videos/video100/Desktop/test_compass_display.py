# test_compass_display.py
#
# Created: 27 July 2026
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.27.0 on 2026-03-01;
# Raspberry Pi Pico 2 with RP2350
# LVGL 9.5

import lvgl as lv
from machine import reset, Pin
from display_driver import disp, touch
from gy271_qmc5833p_driver import Magnetometer
import gc
import math
from machine import I2C, Pin
import time

# https://www.ngdc.noaa.gov/geomag/calculators/magcalc.shtml?
# 11 deg 25 min W ---->  -11 + (25/60)  
declin = -11.4167  #0.6087 rad

#### Sensor ##############################################
I2C_SDA = 2
I2C_SCL = 3
FIRSTRUN = False
# replace below with your calibrated values
offset_data = [0.295, 0.307, 0.223533332]                         #[0, 0, 0]
iron_hardcal = [0.04543805, 0.06994691, 0.20503778]  #[0, 0, 0]
iron_softcal = [0.5360119, 5.0399356, 1.0684279]           #[1, 1, 1]

#https://github.com/Turbofan3360/ESP32-Micropython-GY-271-QMC5883P-Driver
magneto = Magnetometer(I2C_SCL,I2C_SDA)

#### Message during sensor calibration ###############
def message():
    scr = lv.screen_active()
    scr.clean()
    scr.set_style_bg_color(lv.color_hex(0x0),lv.PART.MAIN)
    lbl_text = lv.label(scr)
    lbl_text.center()
    lbl_text.set_text("Calibrating...")
    lbl_text.set_style_text_font(lv.font_montserrat_24,lv.PART.MAIN)
    lbl_text.set_style_text_color(lv.color_white(), lv.PART.MAIN)

if FIRSTRUN:
    message()
    gc.collect()
    magneto.calibrate(0)
    offset_data = magneto.data
    iron_hardcal = magneto.hardcal
    iron_softcal = magneto.softcal
else:
    print("Loading previous calibrated data.")
    magneto.data = offset_data
    magneto.hardcal = iron_hardcal
    magneto.softcal = iron_softcal
    
text = f"Data:\noffset: {offset_data}\nhardcal: {iron_hardcal}\nsoftcal: {iron_softcal}"
print(text)
time.sleep(2)
print("Ready for compass display.")

#### Color ######################################################
blue = lv.palette_main(lv.PALETTE.BLUE)
yellow = lv.palette_main(lv.PALETTE.YELLOW)
red = lv.palette_main(lv.PALETTE.RED)
green = lv.palette_main(lv.PALETTE.GREEN)
grey = lv.color_hex(0x898989)
white = lv.color_white()
black = lv.color_black()

#### UI #################################################
scr = lv.screen_active()
scr.clean()
scr.set_style_bg_color(lv.color_hex(0x0),lv.PART.MAIN)

gc.collect()
lv.screen_load(scr)

# Create a style for the pointer
style_pointer = lv.style_t()
style_pointer.init()
style_pointer.set_line_width(9)
style_pointer.set_line_color(red)
style_pointer.set_line_rounded(True)

# Create the compass pointer
pointer = lv.line(scr)
points = [
    {"x": 120, "y": 110},
    {"x": 120, "y": 50}
]
pointer.set_points(points, 2)
pointer.add_style(style_pointer, 0)

# Compass digital heading value
lbl_text = lv.label(scr)
lbl_text.set_size(50,30)
lbl_text.set_pos(110,120)
lbl_text.set_text("0")
lbl_text.set_style_text_font(lv.font_montserrat_24,lv.PART.MAIN)
lbl_text.set_style_text_color(lv.color_white(), lv.PART.MAIN)

# Compass 360 degree scale
scale = lv.scale(scr)
scale.set_range(0, 360)
scale.set_angle_range(360)   # draw scale as a circle
scale.set_size(150, 150)
scale.set_rotation(270)
scale.center()
scale.set_mode(lv.scale.MODE.ROUND_OUTER)
scale.set_label_show(True)

# Set compass tick intervals and labels
scale.set_total_tick_count(61)
scale.set_major_tick_every(5)
scale.set_style_line_width(1, lv.PART.ITEMS)
scale.set_style_line_width(4, lv.PART.INDICATOR)
scale.set_style_length(5, lv.PART.ITEMS)
scale.set_style_length(9, lv.PART.INDICATOR)
scale.set_style_text_font(lv.font_montserrat_16,lv.PART.MAIN)
scale.set_style_text_color(lv.color_white(), lv.PART.INDICATOR) # numbers
scale.set_style_line_color(lv.color_white(), lv.PART.ITEMS) # ticks
scale.set_style_line_color(lv.color_white(), lv.PART.INDICATOR)  #major tick
labels = ["0","30","60","90","120","150","180","210","240","270","300","330", ""] 
scale.set_text_src(labels)

# Direction labels in 360 degree 
scale2 = lv.scale(scr)
scale2.set_size(85, 85)
scale2.set_range(0, 360)
scale2.set_angle_range(360)   # draw scale2 as a circle
scale2.set_rotation(270)
scale2.center()
scale2.set_mode(lv.scale.MODE.ROUND_OUTER)
scale2.set_label_show(True)

# Set Direction tick intervals and labels
scale2.set_total_tick_count(5)
scale2.set_major_tick_every(1)
scale2.set_style_arc_width(0, lv.PART.MAIN)
scale.set_style_text_font(lv.font_montserrat_14,lv.PART.MAIN)
#scale2.set_style_line_color(green, lv.PART.INDICATOR)
scale2.set_style_text_color(green, lv.PART.INDICATOR) # numbers
#labels = ["N","NE","E","SE","S","SW","W","NW",""]
labels = ["N","E","S","W",""] 
scale2.set_text_src(labels)

# Loop to display latest heading and rotate compass scales
while True:
    gc.collect()
    heading = magneto.compass_2d(0)  # 0=magnetic heading, or your declination.
    lbl_text.set_text(str(heading))
    rot = 270 - heading  #widget's origin is 270
    scale.set_rotation(rot)
    scale2.set_rotation(rot)
    #time.sleep(.1)
    
# requires hard reset to stop
print("done")

