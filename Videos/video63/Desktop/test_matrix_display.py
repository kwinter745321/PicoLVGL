# test_matrix_display.py
#
# Created: 28 April 2025
# Modified:  10 November 2025
#
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-2510.gacfeb7b7e on 2025-11-09; linux [GCC 14.2.0] version
# LVGL 9.3
# 
import lvgl as lv
import display_driver
from display_driver import display as disp
import time

width = disp.hor_res
height = disp.ver_res
scr = lv.obj()
lv.screen_load(scr)

#### UI ##########################
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
    
jcnt = 1
icnt = 0
for j in range(10,(height-20),40):
    for i in range(10,(width-20),50):
        btn = lv.button(scr)
        #btn.set_style_bg_color(lv.palette_main(lv.PALETTE.CYAN),lv.PART.MAIN)
        btn.set_style_bg_color(lv.palette_main(6+jcnt),lv.PART.MAIN)
        btn.set_size(48,30)
        btn.set_pos(i, j)
        lbl = lv.label(btn)
        lbl.center()
        txt = str(i)+"-"+str(jcnt)
        lbl.set_text(txt)
        lbl.set_style_text_color(lv.color_black(),0)
        lbl.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN )
        btn.add_event_cb(btn_cb, lv.EVENT.CLICKED, None)
        btnlst.append(btn)
        lbllst.append(lbl)
        icnt += 1
    jcnt += 1
###################################################
def screen_exit(event):
    code = event.get_code()
    # display closed event
    if code == 41:
        import os
        os.system("stty echo")

disp.add_event_cb(screen_exit, lv.EVENT.ALL, None)

 
