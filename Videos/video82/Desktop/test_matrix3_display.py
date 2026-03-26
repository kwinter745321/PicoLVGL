# test_matrix3_display.py
#
# Created: 28 April 2025 for 320x480 displays
# Update:  23 March 2026 
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# Verified on:
# Waveshare 1.28inch Round Touch LCD
# MicroPython v1.27.0 on 2026-03-01;
# Raspberry Pi Pico W with RP2040
# Raspberry Pi Pico 2 W with RP2350
# 
import lvgl as lv
from machine import reset, Pin, SPI
import time

from display_driver import disp, touch

bl = Pin(15, Pin.OUT)
bl.on()

scr = lv.obj()

scr.set_style_bg_color(lv.color_hex(0),0)
#scr.set_style_border_width(2, 0)
#scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),0)

### Button  ###################
btnlst = []
lbllst = []

def btn_cb(event):
    obj = event.get_target_obj()
    child = obj.get_child(0)
    txt = child.get_text()
    print(3*"#",txt,3*"#")

size = 50
jcnt = 1
icnt = 0
for j in range(10,disp.height-30,size):
    for i in range(10,disp.width-30,size):
        btn = lv.button(scr)
        #btn.set_style_bg_color(lv.palette_main(lv.PALETTE.CYAN),lv.PART.MAIN)
        btn.set_style_bg_color(lv.palette_main(6+jcnt),lv.PART.MAIN)
        btn.set_size(size-2,size-8)
        btn.set_pos(i, j)
        lbl = lv.label(btn)
        lbl.center()
        txt = str(i)+"-"+str(jcnt)
        lbl.set_text(txt)
        lbl.set_style_text_color(lv.color_black(),0)
        #lbl.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN )
        btn.add_event_cb(btn_cb, lv.EVENT.PRESSED, None)
        btnlst.append(btn)
        lbllst.append(lbl)
        icnt += 1
    jcnt += 2
    
###################################################
lv.screen_load(scr)

 