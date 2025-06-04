# test_update_simulator.py
#
# Updated: 03 June 2025
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-2504.g9fe842956 on 2025-04-04; Raspberry Pi Pico with RP2040
# APRIL 2025 Firmware
# LVGL 9.0 
#
import lvgl as lv
import display_driver

import time
import gc

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
canvas1 = lv.canvas(scr)
canvas1.set_buffer(cbuf, width,height, lv.COLOR_FORMAT.RGB565)
canvas1.set_pos(100,80)
canvas1.fill_bg(lv.palette_lighten(lv.PALETTE.GREY,1),lv.OPA.COVER)

#### 2. Define Primitive graphic object(s) (that we put on a layer)
rect_dsc = lv.draw_rect_dsc_t()
rect_dsc.init()
rect_dsc.bg_opa = lv.OPA.TRANSP
rect_dsc.border_width = 2
rect_dsc.border_color = lv.color_black()

#### 3. Define a Layer
layer1 = lv.layer_t()
coords = lv.area_t()
canvas1.init_layer(layer1)

#### Button to display rect object
rectbtn = lv.button(scr)
rectbtn.set_size(60,40)
rectbtn.set_pos(15,90)
rectbtn.set_style_bg_color(lv.color_white(),lv.PART.MAIN)
rectlbl = lv.label(rectbtn)
rectlbl.set_text("Rect")
rectlbl.set_style_text_color(lv.color_black(),lv.PART.MAIN)
rectlbl.center()

#### Initialize variables
#cnt = 0
indev = None
once = 0
touchpoint = lv.point_t()

def do_place(event):
    global touchpoint, indev
    indev.get_point(touchpoint)
    print("Touch at: ",(touchpoint.x,touchpoint.y) )

def do_pick(event):
    global once, indev
    btn = event.get_target_obj()
    time.sleep_ms(50)
    gc.collect()
    if btn:
        lbl = btn.get_child(0)
        txt = lbl.get_text()
        if once == 0:
            once = 1
            indev = lv.indev_active()
            if indev:
                print("indev ready")
                indev.add_event_cb(do_place, lv.EVENT.CLICKED, None)
        if txt == "Rect":
            print("Draw Rect disabled")
            #### 4. Draw primitive object
            #coords.set(10+s,10+s,50+s,50+s)
            #lv.draw_rect(layer1, rect_dsc, coords)
            #lv.canvas.finish_layer(canvas1, layer1)
        if txt == "Text":
            print("Draw Text")

rectbtn.add_event_cb(do_pick, lv.EVENT.CLICKED, None)

#### UI done ###################################
lv.screen_load(scr)
     
