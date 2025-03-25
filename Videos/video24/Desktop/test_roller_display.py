# test_roller_display.py
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

#### Spinner #########################
spin = lv.spinner(scr)
spin.set_size(150, 150)
spin.center()

#### Label for selected roller value ###########
lblout = lv.label(scr)
lblout.set_text("5")
lblout.set_size(60,50)
lblout.set_style_pad_all(10, lv.PART.MAIN)
lblout.set_style_bg_color(lv.palette_main(lv.PALETTE.CYAN), lv.PART.MAIN )
lblout.set_style_border_width(4, 0)
lblout.set_style_border_color(lv.palette_main(lv.PALETTE.BLUE),lv.PART.MAIN)
lblout.set_style_text_color(lv.color_white(), lv.PART.MAIN)
lblout.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN )

#### Roller #############################
def rollercb(event):
    global selected
    rol = event.get_target_obj()
    if rol:
        opt = " "*5                             # 5 byte buffer
        rol.get_selected_str(opt,len(opt) )
        selected = opt
        lblout.set_text(opt)
        
#### Roller Style  ###################
rollstyle = lv.style_t()
rollstyle.init()
rollstyle.set_width(70)
rollstyle.set_text_color(lv.color_black() )
rollstyle.set_text_font(lv.font_montserrat_24)
rollstyle.set_border_width(6)
rollstyle.set_border_color(lv.palette_main(lv.PALETTE.ORANGE) )
    
roller = lv.roller(scr)
roller.center()
roller.add_style(rollstyle, lv.PART.MAIN )
roller.set_visible_row_count(4)
roller.set_style_bg_color(lv.palette_main(lv.PALETTE.CYAN), lv.PART.SELECTED )
roller.set_style_text_color(lv.palette_main(lv.PALETTE.RED), lv.PART.SELECTED )

roller.add_event_cb(rollercb, lv.EVENT.VALUE_CHANGED, None)

#### Roller Data ###############################
txt = "\n".join(["1","2","3","4","5","6","7","8","9","10"])
roller.set_options(txt, lv.roller.MODE.NORMAL)

#### Select the fifth item as the default ######
roller.set_selected(4, lv.PART.SELECTED )

#### align lblout next to the roller ################
lbly = (scr.get_height() // 2) - 25   # center minus box height
lblx = (scr.get_width() // 2)  + 70   # center plus roller width
lblout.set_pos( lblx, lbly )

###################################################
spin.fade_out(1000,10)
lv.screen_load(scr)
        


# Run the event loop
# while True:
#     lv.timer_handler()
#     time.sleep_ms(10)

