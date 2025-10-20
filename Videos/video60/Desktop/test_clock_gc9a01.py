# test_clock_gc9a01.py
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
#
import lvgl as lv
from machine import SPI, Pin
import display_driver
from display_driver import disp
import time
from machine import reset

import utime
import math

#### UI ####
scr = lv.obj()
lv.screen_load(scr)

custom_labels = ["","1","2","3","4","5","6","7","8","9","10","11","12"]

# #### Scale ##############
scale = lv.scale(scr)
scale.set_text_src(custom_labels)
scale.set_range(0, 60)
scale.set_angle_range(360)   # draw scale as a circle
scale.center()
scale.set_size(240, 240)
scale.set_mode(lv.scale.MODE.ROUND_INNER)
scale.set_rotation(270)      # rotate scale so it looks like a clock
scale.set_style_bg_opa(lv.OPA.COVER, lv.PART.MAIN)
scale.set_style_bg_color(lv.color_white(), lv.PART.MAIN)
scale.set_label_show(True)

scale.set_total_tick_count(61)
scale.set_major_tick_every(5)
scale.set_style_line_width(1, lv.PART.ITEMS)
scale.set_style_line_width(4, lv.PART.INDICATOR)
scale.set_style_length(5, lv.PART.ITEMS)
scale.set_style_length(9, lv.PART.INDICATOR)
scale.set_style_text_font(lv.font_montserrat_24,lv.PART.MAIN)

# # Create a style for the clock face
style_face = lv.style_t()
style_face.init()
style_face.set_radius(lv.RADIUS_CIRCLE)
style_face.set_border_width(0)

# Create the clock face object
clock_face = lv.obj(scr)
clock_face.set_size(140, 140)
clock_face.align(lv.ALIGN.CENTER, 0, 0)
clock_face.add_style(style_face, lv.PART.MAIN)
clock_face.center()

# Create a style for the clock hands
style_hand = lv.style_t()
style_hand.init()
style_hand.set_line_width(4)
style_hand.set_line_color(lv.color_black())
style_hand.set_line_rounded(True)

# clock_face code suggested by google upon search on 17 October 2025
# Define the center of the clock face
center_x, center_y = 110, 110
hand_length_h = 50
hand_length_m = 75
hand_length_s = 85

# Create a parent object for the hands to handle rotation
hand_parent = lv.obj(clock_face)
hand_parent.set_size(240, 240)
hand_parent.align(lv.ALIGN.CENTER, 0, 0)
hand_parent.add_flag(lv.obj.FLAG.FLOATING) # Prevents parent style from affecting hands

# Create the hour hand
hour_hand = lv.line(hand_parent)
hour_points = [
    {"x": center_x, "y": center_y},
    {"x": center_x, "y": center_y - hand_length_h}
]
hour_hand.set_points(hour_points, 2)
hour_hand.add_style(style_hand, 0)

# Create the minute hand
minute_hand = lv.line(hand_parent)
minute_points = [
    {"x": center_x, "y": center_y},
    {"x": center_x, "y": center_y - hand_length_m}
]
minute_hand.set_points(minute_points, 2)
minute_hand.add_style(style_hand, 0)

# Create the second hand (make it a different color)
style_sec_hand = lv.style_t()
style_sec_hand.init()
style_sec_hand.set_line_width(2)
style_sec_hand.set_line_color(lv.palette_main(lv.PALETTE.RED))
style_sec_hand.set_line_rounded(True)

second_hand = lv.line(hand_parent)
second_points = [
    {"x": center_x, "y": center_y},
    {"x": center_x, "y": center_y - hand_length_s}
]
second_hand.set_points(second_points, 2)
second_hand.add_style(style_sec_hand, 0)

def update_clock_cb(timer):
    """Callback function to update the clock hands every second."""
    # Get the current time from utime.localtime()
    #
    current_time = utime.localtime()
    #print(current_time)
    hours = current_time[3]
    minutes = current_time[4]
    seconds = current_time[5]

    # Convert hours to 12-hour format
    if hours >= 12:
        hours -= 12

    # Calculate the angle for each hand in degrees, where 0 degrees is at the 12 o'clock position
    # The `set_rotation` function on the parent rotates all child hands together,
    # so we update the hand positions manually relative to the center
    #
    angle_h = (hours * 30) + (minutes * 0.5) - 90  # -90 for 12 o'clock start position
    angle_m = (minutes * 6) - 90
    angle_s = (seconds * 6) - 90

    # Convert angles to radians for mathematical calculations
    rad_h = math.radians(angle_h)
    rad_m = math.radians(angle_m)
    rad_s = math.radians(angle_s)

    # Calculate the new end-point coordinates for each hand
    h_x_end = int(center_x + hand_length_h * math.cos(rad_h))
    h_y_end = int(center_y + hand_length_h * math.sin(rad_h))
    m_x_end = int(center_x + hand_length_m * math.cos(rad_m))
    m_y_end = int(center_y + hand_length_m * math.sin(rad_m))
    s_x_end = int(center_x + hand_length_s * math.cos(rad_s))
    s_y_end = int(center_y + hand_length_s * math.sin(rad_s))
    
    # Update the hands' points
    new_h_points = [
        {"x": center_x, "y": center_y},
        {"x": h_x_end, "y": h_y_end}
    ]
    hour_hand.set_points(new_h_points, 2)
    
    new_m_points = [
        {"x": center_x, "y": center_y},
        {"x": m_x_end, "y": m_y_end}
    ]
    minute_hand.set_points(new_m_points, 2)

    new_s_points = [
        {"x": center_x, "y": center_y},
        {"x": s_x_end, "y": s_y_end}
    ]
    second_hand.set_points(new_s_points, 2)

# Create an LVGL timer that calls the update_clock_cb function every 1000ms
timer = lv.timer_create(update_clock_cb, 1000, None)

# Set the screen as the active one

