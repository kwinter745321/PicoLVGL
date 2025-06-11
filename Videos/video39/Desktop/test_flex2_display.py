# test_flex2_display.py
#
# Updated: 09 June 2025
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.25.0 on 2025-06-08; Raspberry Pi Pico 2 W with RP2350
# LVGL 9.3 
#
# Tested with RPI_PICO2_W USB board

import lvgl as lv
from display_driver import disp
from machine import Pin, reset

import time
import random

lv.init()

###############################################
# UI
###############################################
 
# current screen
scr = lv.obj()
#h = HardReset(scr)

scr.set_style_bg_color(lv.color_hex(0),0)
scr.set_style_border_width(2, 0)
scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),0)

selected = None

#
# A simple row and a column layout with flexbox
#
contstyle = lv.style_t()
contstyle.set_bg_opa(lv.OPA.TRANSP)

btnstyle = lv.style_t()
btnstyle.set_bg_color(lv.palette_main(lv.PALETTE.CYAN))
btnstyle.set_height(30)

btnstyle2 = lv.style_t()
btnstyle2.set_bg_color(lv.color_hex(0xE0FFFF) )
#btnstyle2.set_height(30)

lblstyle = lv.style_t()
lblstyle.set_text_color(lv.color_black() )
lblstyle.set_text_font(lv.font_montserrat_14)

# Create a container with COLUMN flex direction
cont_col = lv.obj(scr)
cont_col.set_size(120, 130)
cont_col.add_style(contstyle, lv.PART.MAIN)
cont_col.align(lv.ALIGN.TOP_LEFT, 5, 5)
cont_col.set_flex_flow(lv.FLEX_FLOW.COLUMN)

# Create a container with ROW flex direction
cont_col2 = lv.obj(scr)
cont_col2.set_size(170, 220)
cont_col2.add_style(contstyle, lv.PART.MAIN)
cont_col2.align_to(cont_col, lv.ALIGN.OUT_RIGHT_TOP, 10, 0)
cont_col2.set_flex_flow(lv.FLEX_FLOW.COLUMN)

# Labels for count and amount
cntlbl = lv.label(scr)
cntlbl.set_style_text_color(lv.color_white(), lv.PART.MAIN)
cntlbl.align_to(cont_col, lv.ALIGN.OUT_BOTTOM_LEFT, 20, 20)
cntlbl.set_text("Count")
amtlbl = lv.label(scr)
amtlbl.set_style_text_color(lv.color_white(), lv.PART.MAIN)
amtlbl.align_to(cntlbl, lv.ALIGN.OUT_BOTTOM_LEFT, 0, 10)
amtlbl.set_text("Amount")
#### END UI ########################################################################

topiclist = ["World", "National", "Local"]
wrdlist = ["Canada", "Germany", "Mexico", "United Kingdom", "United States", "Thailand"]
natlist = ["Alabama", "Kansas", "Mississippi", "Ohio",]
lcllist = ["Dover", "Newark", "Rehoboth"]

option = True

def getcount(event):
    amt = random.randint(0,10)
    if amt > 0:
        amtlbl.set_text("Amount: "+str(amt))
    else:
        amtlbl.set_text("Amount: None")
        
def drawchild(clist):
    global option
    cont_col2.clean()
    amtlbl.set_text("Amount")
    cnt = len(clist)
    cntlbl.set_text("Count: "+str(cnt))
    for item in clist:
        btn = lv.button(cont_col2)
        #### FLEX GROW ######################################
        if option:
            if cnt < 4:
                btn.set_flex_grow(2)
            else:
                btn.set_flex_grow(1)
        #####################################################
        btn.add_style(btnstyle2, lv.PART.MAIN)
        btn.add_event_cb(getcount, lv.EVENT.CLICKED, None)
        label = lv.label(btn)
        label.add_style(lblstyle, lv.PART.MAIN)
        label.set_text("{:s}".format(item))
        label.center()
    
def readitem(e):
    global selected
    btn = e.get_target_obj()
    if btn:
        lbl = btn.get_child(0)
        txt = lbl.get_text()
        if txt == "World":
            drawchild(wrdlist)
        if txt == "National":
            drawchild(natlist)        
        if txt == "Local":
            drawchild(lcllist)        

for item in topiclist:
    btn = lv.button(cont_col)
    btn.add_style(btnstyle, lv.PART.MAIN)
    btn.add_event_cb(readitem, lv.EVENT.PRESSED, None)

    label = lv.label(btn)
    label.add_style(lblstyle, lv.PART.MAIN)
    label.set_text("{:s}".format(item))
    label.center()


    
###################################################
lv.screen_load(scr)
        

# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)