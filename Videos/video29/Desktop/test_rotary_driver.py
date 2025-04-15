# test_rotary_driver.py
#
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-724-gbf1107420 on 2025-02-19; Raspberry Pi Pico with RP2040
# Raspberry Pi Pico (RP2040)
# LVGL 9.1/LVGL 9.3
#
#import display_driver
#import lvgl as lv
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
       max_val=5, 
       incr=1,
       reverse=True, 
       range_mode=RotaryIRQ.RANGE_WRAP,
       pull_up=False,
       half_step=False,
       invert=False)

val_old = 0
print("Start turning the knob or press the Switch (or button2).")
while True:
    val_new = r.value()
    switch = button.value()
  
    if val_old != val_new:
        val_old = val_new
        print('result =', val_new)
        
    if switch == 0:
        print("Switch pressed")
        time.sleep(0.5)
        
        
    time.sleep_ms(50)


