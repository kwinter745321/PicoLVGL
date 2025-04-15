# test_slider_encoder.py
#
# MIT License
# MicroPython v1.20.0-724-gbf1107420 on 2025-02-19; Raspberry Pi Pico with RP2040
# Raspberry Pi Pico (RP2040)
# LVGL 9.1/LVGL 9.3
#
import display_driver
import lvgl as lv
import machine
from machine import Pin
from rotary_irq_rp2 import RotaryIRQ
import time

#### Define Rotary Encoder ###########
CLK = 7
DT = 8
SW = 9

button = Pin(SW, Pin.IN, Pin.PULL_UP)

#range_mode: RANGE_WRAP, RANGE_BOUNDED, RANGE_UNBOUNDED
r = RotaryIRQ(
       pin_num_clk = CLK, 
       pin_num_dt = DT, 
       min_val=0, 
       max_val=100, 
       incr=20,
       reverse=True, 
       range_mode=RotaryIRQ.RANGE_WRAP,
       pull_up=False,
       half_step=False,
       invert=False)

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
scr.set_style_bg_color(lv.color_hex(0),0)
scr.set_style_border_width(2, 0)
scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),0)

#### Encoder read callback ################
old_val = 0

def updateEditLabel():
    if encgrp.editing == True:
        lblm.set_text("Nav")
    else:
        lblm.set_text("Edit")
            
def read_encoder(indev, data):
    global old_val
    ##### Handle encoder ###########
    val = r.value()
    data.enc_diff = val - old_val
    if val != old_val:
        old_val = val
    ##### Handle SW ############
    pressed = button.value()
    if pressed == 0:
        data.state = lv.INDEV_STATE.PRESSED
        updateEditLabel()
        time.sleep_ms(300)
    else:
        data.state = lv.INDEV_STATE.RELEASED
    return False   
    
encoder_drv = lv.indev_create()
encoder_drv.set_type(lv.INDEV_TYPE.ENCODER)
encoder_drv.set_read_cb(read_encoder)

#### bar and slider #####################
def slidercb(event):
    val = slider.get_value()
    lbl.set_text(str(val))
    
slider = lv.slider(scr)
slider.center()
# callback needed for the label text
slider.add_event_cb(slidercb, lv.EVENT.VALUE_CHANGED, None )

lbl = lv.label(scr)
lbl.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN)
lbl.align_to(slider, lv.ALIGN.OUT_BOTTOM_MID, 0, 10)
lbl.set_style_text_color(lv.palette_main(lv.PALETTE.RED), lv.PART.MAIN )
lbl.set_text("0")

lblm = lv.label(scr)
lblm.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN)
lblm.align_to(scr, lv.ALIGN.OUT_TOP_MID, -20, 30)
lblm.set_style_text_color(lv.palette_main(lv.PALETTE.ORANGE), lv.PART.MAIN )
lblm.set_text("Edit")

#### Encoder Group #####################
encgrp = lv.group_create()
encgrp.add_obj(slider)          
encoder_drv.set_group(encgrp)
encgrp.editing = True

###################################################
lv.screen_load(scr)
        
# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)