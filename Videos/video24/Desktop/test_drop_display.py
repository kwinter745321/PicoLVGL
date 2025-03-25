# test_dropdown_display.py
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
scr.set_style_bg_color(lv.color_hex(0),lv.PART.MAIN)
scr.set_style_border_width(2, lv.PART.MAIN)
scr.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),lv.PART.MAIN)

#### Label ###########
lblout = lv.label(scr)
lblout.set_text("None")
lblout.set_pos(160,20)
lblout.set_size(140,40)
lblout.set_style_pad_all(5, lv.PART.MAIN)
lblout.set_style_bg_color(lv.palette_main(lv.PALETTE.CYAN), lv.PART.MAIN )
lblout.set_style_border_width(2, lv.PART.MAIN)
lblout.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE), lv.PART.MAIN)
lblout.set_style_text_color(lv.color_white(), lv.PART.MAIN)
lblout.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN )

##### Dropdown ###########
ddbtnstyle = lv.style_t()
ddbtnstyle.init()
ddbtnstyle.set_bg_color(lv.color_black() )
ddbtnstyle.set_text_color(lv.color_white())
ddbtnstyle.set_text_font(lv.font_montserrat_16)

ddlststyle = lv.style_t()
ddlststyle.init()
ddlststyle.set_bg_color(lv.color_black() )
ddlststyle.set_text_color(lv.palette_main(lv.PALETTE.YELLOW) )

ddselstyle = lv.style_t()
ddselstyle.init()
ddselstyle.set_bg_color(lv.color_black() )
ddselstyle.set_text_color(lv.palette_main(lv.PALETTE.CYAN) )

def dropcb(e):
    code = e.get_code()
    ddobj = e.get_target_obj()
    if code == lv.EVENT.VALUE_CHANGED:
        option = " "*10                             # buffer to store the option
        ddobj.get_selected_str(option, len(option))
        #                                           # .strip() removes trailing spaces
        print("Option selected: \"%s\"" % option.strip())
        lblout.set_text(option.strip() )

# dropdown and its button
dd = lv.dropdown(scr)
dd.set_size(140,40)
dd.add_style( ddbtnstyle, lv.PART.MAIN )

# dropdown list
ddlist = dd.get_list()
ddlist.add_style( ddlststyle, lv.PART.MAIN )
ddlist.set_style_size( 20, 50, lv.PART.SCROLLBAR )

# dropdown list selected
ddlist.add_style( ddselstyle, lv.PART.SELECTED )

# dropdown data
dd.set_options("\n".join([
    "",
    "Apple",
    "Banana",
    "Orange",
    "Cherry",
    "Grape",
    "Raspberry",
    "Melon",
    "Orange",
    "Lemon",
    "Nuts"]))

dd.align(lv.ALIGN.TOP_LEFT, 10, 20)
dd.add_event_cb(dropcb, lv.EVENT.ALL, None)
###################################################
lv.screen_load(scr)
        
# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)

