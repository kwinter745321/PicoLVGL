# test_canvas2_display.py
#
# Updated: 30 May 2025
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-2504.g9fe842956 on 2025-04-04; Raspberry Pi Pico with RP2040
# APRIL 2025 Firmware
# LVGL 9.3 
#

import lvgl as lv
import display_driver
import time
import sys
import gc

if sys.platform in ['rp2', 'esp32']:
    print("Running on microcontroller.")
    from machine import reset
else:
    print("Running on simulator.")

scr = lv.obj()

isLVGL93 = False
if lv.version_minor() == 3:
    print("Running on LVGL 9.3")
    isLVGL93 = True

xpos = 110    # start x-coord of color buttons
selected = 255  # selected color
width = 150
height = 100
pick = None

# coords for rect
coords = lv.area_t()
layer1 = lv.layer_t()
coords.set(10,10,50,50)
# coords.set(5,5,25,25)
# 
# # coords for text "hi"
# coords2 = lv.area_t()
# layer2 = lv.layer_t()
# #coords2.set(60,10,80,20)
# coords2.set(30,10,50,20)


#print(gc.mem_free() )
gc.collect()
#print("memory:",gc.mem_free() )

#### Canvas Buffer (half factor)
cbuf = bytearray(width*height*4)

#### UI ######################################################

# Screen background
scr.set_style_bg_color(lv.color_hex(0),lv.PART.MAIN)
scr.set_style_border_width(2, lv.PART.MAIN)
scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),lv.PART.MAIN)

dispp = lv.display_get_default()
theme = lv.theme_default_init(dispp, lv.palette_main(lv.PALETTE.BLUE), lv.palette_main(lv.PALETTE.RED), True, lv.font_montserrat_24)
dispp.set_theme(theme)

# Define color selection button
colorbtn = lv.button(scr)
colorbtn.set_size(40,40)
colorbtn.set_pos(25,30)
colorbtn.set_style_bg_color(lv.color_white(),lv.PART.MAIN)
colorbtn.set_style_border_color(lv.color_white(),lv.PART.MAIN)
colorbtn.set_style_border_width(2,lv.PART.MAIN)

# color chooser buttons and callback
def getColor(event):
    global selected
    btn = event.get_target_obj()
    gc.collect()
    if btn:
        lbl = btn.get_child(0)
        txt = lbl.get_text()
        if txt == "b":
            colorbtn.set_style_bg_color(lv.color_black(),0)
            selected = 255
        if txt == "r":
            colorbtn.set_style_bg_color(lv.palette_main(lv.PALETTE.RED),0)
            selected = lv.PALETTE.RED
        if txt == "g":
            colorbtn.set_style_bg_color(lv.palette_main(lv.PALETTE.GREEN),0)
            selected = lv.PALETTE.GREEN
        if txt == "c":
            colorbtn.set_style_bg_color(lv.palette_main(lv.PALETTE.CYAN),0)
            selected = lv.PALETTE.CYAN


#print("memory:",gc.mem_free())
gc.collect()
#print("memory:",gc.mem_free())

wbtn = lv.button(scr)
wbtn.set_size(40,40)
wbtn.set_pos(xpos,20)
wbtn.set_style_bg_color(lv.color_white(),lv.PART.MAIN)
wlbl = lv.label(wbtn)
wlbl.set_text("b")
wlbl.set_style_text_color(lv.color_black(),lv.PART.MAIN)
wlbl.center()
wbtn.add_event_cb(getColor, lv.EVENT.CLICKED, None)

rbtn = lv.button(scr)
rbtn.set_size(40,40)
rbtn.set_pos(xpos+50,20)
rbtn.set_style_bg_color(lv.palette_main(lv.PALETTE.RED),lv.PART.MAIN)
rlbl = lv.label(rbtn)
rlbl.set_text("r")
rlbl.set_style_text_color(lv.color_black(),lv.PART.MAIN)
rlbl.center()
rbtn.add_event_cb(getColor, lv.EVENT.CLICKED, None)

gbtn = lv.button(scr)
gbtn.set_size(40,40)
gbtn.set_pos(xpos+100,20)
gbtn.set_style_bg_color(lv.palette_main(lv.PALETTE.GREEN),lv.PART.MAIN)
glbl = lv.label(gbtn)
glbl.set_text("g")
glbl.set_style_text_color(lv.color_black(),lv.PART.MAIN)
glbl.center()
gbtn.add_event_cb(getColor, lv.EVENT.CLICKED, None)

bbtn = lv.button(scr)
bbtn.set_size(40,40)
bbtn.set_pos(xpos+150,20)
bbtn.set_style_bg_color(lv.palette_main(lv.PALETTE.CYAN),lv.PART.MAIN)
blbl = lv.label(bbtn)
blbl.set_text("c")
blbl.set_style_text_color(lv.color_black(),lv.PART.MAIN)
blbl.center()
bbtn.add_event_cb(getColor, lv.EVENT.CLICKED, None)

# primitive graphic object buttons

rectbtn = lv.button(scr)
rectbtn.set_size(60,40)
rectbtn.set_pos(15,90)
rectbtn.set_style_bg_color(lv.color_white(),lv.PART.MAIN)
rectlbl = lv.label(rectbtn)
rectlbl.set_text("Rect")
rectlbl.set_style_text_color(lv.color_black(),lv.PART.MAIN)
rectlbl.center()

txtbtn = lv.button(scr)
txtbtn.set_size(60,40)
txtbtn.set_pos(15,140)
txtbtn.set_style_bg_color(lv.color_white(),lv.PART.MAIN)
txtlbl = lv.label(txtbtn)
txtlbl.set_text("Text")
txtlbl.set_style_text_color(lv.color_black(),lv.PART.MAIN)
txtlbl.center()

clearbtn = lv.button(scr)
clearbtn.set_size(180,40)
clearbtn.set_pos(15,190)
clearbtn.set_style_bg_color(lv.palette_main(lv.PALETTE.YELLOW),lv.PART.MAIN)
clrlbl = lv.label(clearbtn)
clrlbl.set_text("CLEAR")
clrlbl.set_style_text_color(lv.color_black(),lv.PART.MAIN)
clrlbl.center()

# Define Canvas
canvas1 = lv.canvas(scr)
canvas1.set_buffer(cbuf, width,height, lv.COLOR_FORMAT.RGB565)
canvas1.set_pos(100,80)
canvas1.fill_bg(lv.palette_lighten(lv.PALETTE.GREY,1),lv.OPA.COVER)


# Define primitive objects
rect_dsc = lv.draw_rect_dsc_t()
rect_dsc.init()
rect_dsc.bg_opa = lv.OPA.TRANSP
rect_dsc.border_width = 2
rect_dsc.border_color = lv.color_black()

lbl_dsc = lv.draw_label_dsc_t()
lbl_dsc.init()
lbl_dsc.font = lv.font_montserrat_16
lbl_dsc.color = lv.palette_main(lv.PALETTE.RED)
lbl_dsc.text = "hi"

# Define area, point
area = lv.area_t()
area.set_width(width)
area.set_height(height)

#initialize indev
touchpoint = lv.point_t()
indev = None
once = 0

#initialize canvas
canvas1.init_layer(layer1)

# Define "draw" callbacks and drawing routines

def do_place(event):
    global touchpoint, pick, indev
    # populate p (point_t)
    indev.get_point(touchpoint)
    # transform to coordinates inside canvas1
    cx = touchpoint.x-canvas1.get_x()
    cy = touchpoint.y-canvas1.get_y()
    if cx > -1 and cy > -1:
        if pick == "Rect":
            if isLVGL93 == True:
                coords.set_pos(cx-10,cy-20)                  #LVGL9.3
            else:
                coords.set(cx-10,cy-20,cx+40,cy+30)
            draw_rect()
        if pick == "Text":
            if isLVGL93 == True:
                coords.set_pos(cx-10,cy-20)                   #LVGL9.3
            else:
                coords.set(cx-10,cy-20,cx+40,cy+30) 
            draw_text()
        time.sleep_ms(50)

def draw_rect():
    time.sleep_ms(100)
    #canvas1.init_layer(layer1)
    if selected == 255:
        rect_dsc.border_color = lv.color_black()
    else:
        rect_dsc.border_color = lv.palette_main(selected)
    lv.draw_rect(layer1, rect_dsc, coords)
    if isLVGL93 == False:
        lv.obj.invalidate(scr)
    lv.canvas.finish_layer(canvas1, layer1)
    
def draw_text():
    time.sleep_ms(100)
    if selected == 255:
        lbl_dsc.color = lv.color_black()
    else:
        lbl_dsc.color = lv.palette_main(selected)
    lv.draw_label(layer1, lbl_dsc, coords)
    if isLVGL93 == False:
        lv.obj.invalidate(scr)
    lv.canvas.finish_layer(canvas1, layer1)

def clear_colors():
    for btn in [rectbtn, txtbtn]:
        btn.set_style_bg_color(lv.color_white(),lv.PART.MAIN)

def do_pick(event):
    global pick, once, indev
    btn = event.get_target_obj()
    time.sleep_ms(50)
    gc.collect()
    clear_colors()
    if btn:
        lbl = btn.get_child(0)
        txt = lbl.get_text()
        pick = txt
        if once == 0:
            once = 1
            indev = lv.indev_active()
            indev.add_event_cb(do_place, lv.EVENT.CLICKED, None)
        btn.set_style_bg_color(lv.palette_main(lv.PALETTE.LIME),lv.PART.MAIN)
        if txt == "CLEAR":
            print("Pick is 'cleared'. Choose Rect or Text.")
            canvas1.fill_bg(lv.palette_lighten(lv.PALETTE.GREY,1),lv.OPA.COVER)
        #print("memory:",gc.mem_free() )
        
gc.collect()

rectbtn.add_event_cb(do_pick, lv.EVENT.CLICKED, None)
clearbtn.add_event_cb(do_pick, lv.EVENT.CLICKED, None)
txtbtn.add_event_cb(do_pick, lv.EVENT.CLICKED, None)

print("Canvas is ready.")
lv.screen_load(scr)
     