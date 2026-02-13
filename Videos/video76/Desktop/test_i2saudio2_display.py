# test_i2saudio2_display.py
#
# Created: 02 February 2026 (custom to the device)
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on: 11 Feb 2026
#
# Waveshare RP2350-Touch-LCD-2.8
# MicroPython v1.20.0-2510.gacfeb7b7e.dirty on 2026-02-11;
# Raspberry Pi Pico2 with RP2350

import lvgl as lv
from machine import reset, Pin
from display_driver import disp, touch
from audio2_driver import send_audio, do_wp
from sdcard_driver import sd
import time
import os
##from lv_utils import task_handler
lv.init()
  
###############################################
# UI
###############################################

# current screen
scr = lv.obj()
lv.screen_load(scr)
scr.remove_flag(lv.obj.FLAG.SCROLLABLE)

# backlight
bl = Pin(16, Pin.OUT)
bl.on()

# songs
# 15 chars per line
songs = ["7thlife-7.wav", "7thlife-14.wav",]


# initial values
lsbtn = None
current_index = 1
lbl2b = None
stat = None

# fonts and colors
n14 = lv.font_montserrat_14
n16 = lv.font_montserrat_16
n24 = lv.font_montserrat_24
red = lv.palette_main(lv.PALETTE.RED)
beige = lv.color_hex(0xf5efeb)
gray = lv.color_hex(0xc0c0c0)

# Create a container for the whole screen
cont = lv.obj(scr)
cont.set_size(320, 240)
cont.set_style_bg_color(beige,lv.PART.MAIN)
cont.center()
cont.set_flex_flow(lv.FLEX_FLOW.ROW_WRAP)
cont.set_flex_align(
    lv.FLEX_ALIGN.START, 
    lv.FLEX_ALIGN.START,
    lv.FLEX_ALIGN.START
)
cont.set_style_pad_all(2, 0)
cont.remove_flag(lv.obj.FLAG.SCROLLABLE)

def selected(idx):
    stat.set_text(songs[idx])

def set_focus(idx):
    obj = name_list.get_child(idx)
    obj.set_style_bg_color(gray, 0)
    
def clear_focus(idx):
    obj = name_list.get_child(idx)
    obj.set_style_bg_color(lv.color_white(), 0)


def find_song(name):
    idx = 0
    for item in songs:
        if name in item:
            current_index = idx
            set_focus(idx)
            selected(idx)
            clear_focus(idx)
            break
        idx += 1
    return idx

def name_list_cb(e):
    global current_name
    code = e.get_code()
    if code == lv.EVENT.CLICKED:
        lsbtn = e.get_target_obj()
        # Get the text of the button
        btn_text = lsbtn.get_child(1).get_text()
        if code == lv.EVENT.CLICKED:
            print(f"List item clicked: {btn_text}")
            idx = find_song(btn_text)
            selected(idx)

name_list = lv.list(cont)
name_list.set_size(296, 122) # Set the size of the list
name_list.add_text("Songs")
name_list.set_style_text_font(n14, 0)
name_list.set_style_width(10,lv.PART.SCROLLBAR)

for name in songs:
    btn = name_list.add_button(lv.SYMBOL.AUDIO, name)
    btn.add_event_cb(name_list_cb, lv.EVENT.ALL, None)

listcnt = name_list.get_child_count() - 1 #ignore header
print("Song count:",listcnt)

def btn1cb(e):
    send_audio( stat.get_text() )

def show_dir(path):
    print()
    for entry in os.ilistdir(path):
        name, type_code, _, size = entry
        if type_code == 0x4000: # Directory
            print(f"Directory: {name}")
            show_dir(f"{path}/{name}") # Recurse into subdirectories
        elif type_code == 0x8000: # File
            print(f"   File: {name:20}, Size: {size:15} Bytes")
        else:
            print(f"   Misc: {name:20}, Type: {type_code:15}")
            
def btn2cb(e):
    stat.set_text("")
    show_dir("/sd")


obj = lv.obj(cont)
obj.set_size(150,100)  
obj.remove_flag(lv.obj.FLAG.SCROLLABLE)
lbl = lv.label(obj)
lbl.set_text("Actions:")
lbl.set_style_text_font(n14, 0)
lblb = lv.label(obj)
lblb.set_text("")
lblb.set_pos(80,0)  #130, 0)
lblb.set_style_text_color(red, 0)
lblb.set_style_text_font(n14, 0)
btn1 = lv.button(obj)
btn1.set_pos(0,30)
btn1lbl = lv.label(btn1)
btn1lbl.set_text(lv.SYMBOL.AUDIO)
btn1lbl.set_style_text_font(n16, 0)
btn2 = lv.button(obj)
btn2.set_pos(58,30)
btn2lbl = lv.label(btn2)
btn2lbl.set_text(lv.SYMBOL.FILE)
btn2lbl.set_style_text_font(n16, 0)


obj2 = lv.obj(cont)
obj2.set_size(150,100)
obj2.remove_flag(lv.obj.FLAG.SCROLLABLE)
lbl2 = lv.label(obj2)
lbl2.set_text("Selected:")
lbl2.set_style_text_font(n14, 0)
stat = lv.label(obj2)
stat.set_size(140,40)
stat.set_pos(0,20)
stat.set_text("")
stat.set_style_text_color(red, 0)
stat.set_style_text_font(n14, 0)

btn1.add_event_cb(btn1cb, lv.EVENT.CLICKED, None)
btn2.add_event_cb(btn2cb, lv.EVENT.CLICKED, None)

