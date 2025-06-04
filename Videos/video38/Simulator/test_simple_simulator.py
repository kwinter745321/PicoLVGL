# test_simple_simulator.py
#
# Updated: 30 May 2025
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-2504.g9fe842956 on 2025-04-04; Raspberry Pi Pico with RP2040
# APRIL 2025 Firmware
# LVGL 9.0 
#
import lvgl as lv
import display_driver

import sys
if sys.platform in ['rp2', 'esp32']:
    print("Running on microcontroller.")
    from machine import reset
else:
    print("Running on simulator.")
    
scr = lv.obj()

#### Screen background #########################
scr.set_style_bg_color(lv.color_hex(0),lv.PART.MAIN)
scr.set_style_border_width(2, lv.PART.MAIN)
scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),lv.PART.MAIN)

#### Canvas Objects ############################
width = 150
height = 100

#### CANVAS BUFFER
cbuf = bytearray(width*height*4)

#### 1. Define Canvas
canv = lv.canvas(scr)
canv.set_buffer(cbuf, width,height, lv.COLOR_FORMAT.RGB565)
canv.set_pos(100,80)
canv.fill_bg(lv.palette_lighten(lv.PALETTE.GREY,1),lv.OPA.COVER)

#### 2. Define Primitive graphic object(s) (that we put on a layer)
rect_dsc = lv.draw_rect_dsc_t()
rect_dsc.init()
rect_dsc.bg_opa = lv.OPA.TRANSP
#rect_dsc.bg_color = lv.palette_main(lv.PALETTE.YELLOW)
rect_dsc.border_width = 2
rect_dsc.border_color = lv.color_black()

#### 3. Define a Layer
layer1 = lv.layer_t()
coords = lv.area_t()
coords.set(10,10,50,50)

#### 4. Draw primitive object
canv.init_layer(layer1)
lv.draw_rect(layer1, rect_dsc, coords)
lv.canvas.finish_layer(canv, layer1)

#### UI done ###################################
lv.screen_load(scr)
    
