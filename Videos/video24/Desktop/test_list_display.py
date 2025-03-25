# test_list_display.py
#
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-724-gbf1107420 on 2025-02-19; Raspberry Pi Pico with RP2040
# Raspberry Pi Pico (RP2040)
# LVGL 9.1                    https://docs.lvgl.io/9.1/
#
#

import display_driver
import lvgl as lv

import time

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

#### Label ###########
lblout = lv.label(scr)
lblout.set_text("None")
lblout.set_pos(200,80)
lblout.set_size(90,40)
lblout.set_style_pad_all(5, 0 )
lblout.set_style_bg_color(lv.palette_main(lv.PALETTE.CYAN), 0 )
lblout.set_style_border_width(2, 0)
lblout.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),0)
lblout.set_style_text_color(lv.color_white(), 0)
lblout.set_style_text_font(lv.font_montserrat_24, 0)

#### List Style  ###################
lststyle = lv.style_t()
lststyle.init()
lststyle.set_bg_color(lv.color_black() )
lststyle.set_text_color(lv.color_white())
lststyle.set_text_font(lv.font_montserrat_24)

##### List ###########
def lst_cb(event):
    obj =  event.get_target_obj()
    txt = lst.get_button_text(obj)
    print("Clicked button: ", txt)
    lblout.set_text(txt)
    
lst = lv.list(scr)
lst.set_pos(5,5)
lst.set_size(150,200)
lst.add_style(lststyle,0)

lst.add_text("FILE")
btn_new = lst.add_button(lv.SYMBOL.FILE, "New")
btn_new.add_event_cb(lst_cb, lv.EVENT.CLICKED, None)
btn_new.add_style(lststyle, 0)
btn_opn = lst.add_button(lv.SYMBOL.DIRECTORY, "Open")
btn_opn.add_event_cb(lst_cb, lv.EVENT.CLICKED, None)
btn_opn.add_style(lststyle, 0)

lst.add_text("EXIT")
btn_cls = lst.add_button(lv.SYMBOL.CLOSE, "Close")
btn_cls.add_event_cb(lst_cb, lv.EVENT.CLICKED, None)
btn_cls.add_style(lststyle, 0)
btn_cls.set_style_text_color(lv.palette_main(lv.PALETTE.RED),0)

###################################################
lv.screen_load(scr)
        
# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)

