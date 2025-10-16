# test_blue_display.py
#
# Created: 14 October 2025
#
# Copyright (C) 2025 KW Services.
# MIT License
#
# Verified on: 14 October 2025
# MicroPython v1.26.0 on 2025-08-15; Raspberry Pi Pico 2 W with RP2350
# LVGL 9.3

import lvgl as lv
from machine import reset
import display_driver 
import time, gc
lv.init()
from my_styles import *

##### UI #####

#### current screen ####
scr = lv.obj()
lv.screen_load(scr)
top_layer = lv.layer_top()

content = None
status = None
status_state = [0,0,0]
cnt = 1

def page_header(title):
    header = lv.obj(scr)
    header.set_size(lv.pct(100), 30)
    header.align(lv.ALIGN.TOP_MID, 0, 0)
    header.add_style(header_footer, lv.PART.MAIN)
    hlabel = lv.label(header)
    hlabel.set_size(lv.SIZE_CONTENT,30)
    hlabel.set_style_text_color(white, 0)
    hlabel.set_text(title)
    hlabel.set_style_text_font(tf_font, lv.PART.MAIN)
    hlabel.center()
    return header

def screen_status():
    global status
    #### Bell, Save, Wifi ####
    #sym_map = ["\uF0F3", "\uF0C7", "\uF1EB"]
    sym_map = [ "\uF0F3"]
    status = lv.buttonmatrix(scr)
    status.set_size(lv.pct(30), 30)
    status.set_map(sym_map)
    status.align(lv.ALIGN.TOP_RIGHT, 0,0)
    status.add_style(header_footer, lv.PART.ITEMS)
    status.add_style(header_footer, lv.PART.MAIN)
    #status.set_style_text_font(tf_font, lv.PART.ITEMS)
    status.set_style_text_color(black, lv.PART.ITEMS)
    status.add_style(togstyle, lv.PART.ITEMS | lv.STATE.CHECKED)

def pager_handler(event):
    global content
    if event:
        code = event.get_code
        if event.get_code() == lv.EVENT.VALUE_CHANGED:
            obj = event.get_target_obj()
            btn_id = obj.get_selected_button()
            btn_text = obj.get_button_text(btn_id)
            #print(f"Button  (ID: {btn_id}) pressed!")
            if btn_id == 0:
                pageone()
            if btn_id == 1:
                pagehome()
            if btn_id == 2:
                pagetwo()
            
def screen_footer():
    #### Prev, Home, Next ####
    pager_map = ["\uF053", "\uF015", "\uF054"]
    footer = lv.buttonmatrix(top_layer)
    footer.set_size(lv.pct(100), 30)
    footer.set_map(pager_map)
    footer.align(lv.ALIGN.BOTTOM_MID, 0,0)
    footer.add_style(header_footer, lv.PART.ITEMS)
    footer.add_style(header_footer, lv.PART.MAIN)
    footer.set_style_text_font(tf_font, lv.PART.ITEMS)
    footer.add_event_cb(pager_handler, lv.EVENT.ALL, None)

def set_status(state, id):
    global status_state, status
    if state == "on":
        status.set_button_ctrl(id, lv.buttonmatrix.CTRL.CHECKED)
        status_state[id] = 1
    else:
        status.clear_button_ctrl(id, lv.buttonmatrix.CTRL.CHECKED)
    
def status_cb(e, id):
    global status_state
    if status_state[id] == 0:
        set_status("on",id)
    else:
        set_status("off",id)
        status_state[id] = 0
        
def btn_cb(event):
    global cnt
    print("Clicked button:",cnt)
    cnt = cnt + 1
        
def pagehome():
    global content
    if content:
        content.delete()
        gc.collect()
    header = page_header("Home")
    content = lv.obj(scr)
    content.set_size(lv.pct(100), lv.pct(100)  )
    content.set_style_pad_top(30, 0)
    content.set_style_pad_bottom(30, 0)
    content.move_background()
    #### content ####
    label = lv.label(content)
    msg = "Press < for Page 1\nPress > for Page 2"
    label.set_text(msg)
    label.set_style_text_font(tf_font, 0)
    label.center()

def pageone():
    global content
    if content:
        content.delete()
        gc.collect()
    header = page_header("Page One")
    content = lv.obj(scr)
    content.set_size(lv.pct(100), lv.pct(100)  )
    content.set_style_pad_top(30, 0)
    content.set_style_pad_bottom(30, 0)
    content.move_background()
    screen_status()
    #### content ####
    btn = lv.button(content)
    btn.set_size(100,50)
    btn.set_style_bg_color(lv.palette_main(lv.PALETTE.GREEN),lv.PART.MAIN)
    btn.center()
    btn.add_style(btnstyle, lv.PART.MAIN)
    btn.add_style(pressedstyle, lv.STATE.PRESSED)
    label = lv.label(btn)
    label.set_text('Button')
    btn.add_event_cb(btn_cb, lv.EVENT.CLICKED, None)
    
    bell = lv.button(content)
    bell.set_size(50,50)
    bell.align_to(btn, lv.ALIGN.OUT_LEFT_MID, -40, 0)
    bell.set_style_radius(50,0)
    bell_lbl = lv.label(bell)
    bell_lbl.set_text("Bell")
    bell_lbl.set_style_text_color(black, lv.PART.MAIN)
    bell_lbl.center()
    bell.add_event_cb(lambda e:status_cb(e,0), lv.EVENT.CLICKED, None)
    
def pagetwo():
    global content
    if content:
        content.delete()
        gc.collect()
    header = page_header("Page Two")
    content = lv.obj(scr)
    content.set_size(lv.pct(100), lv.pct(100)  )
    content.set_style_pad_top(30, 0)
    content.set_style_pad_bottom(30, 0)
    content.move_background()
    #### content ####
    btn2 = lv.button(content)
    btn2.set_size(100,50)
    btn2.center()
    btn2.add_style(btnstyle, lv.PART.MAIN)
    btn2.add_style(pressedstyle, lv.STATE.PRESSED)
    label2 = lv.label(btn2)
    label2.set_text('Button2')
    btn2.add_event_cb(btn_cb, lv.EVENT.CLICKED, None)
    
def swipe(event):
    indev = lv.indev_active()
    ges_dir = indev.get_gesture_dir()
    if ges_dir:
        if ges_dir == lv.DIR.TOP:
            pagehome()
        if ges_dir == lv.DIR.LEFT:
            pageone()
        if ges_dir == lv.DIR.RIGHT:
            pagetwo()    

scr.add_event_cb(swipe, lv.EVENT.GESTURE, None)

#### Show Initial Content on Startup ####
pagehome()
screen_footer()

# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)
