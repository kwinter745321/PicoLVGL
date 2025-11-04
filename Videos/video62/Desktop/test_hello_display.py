import lvgl as lv
from machine import reset
import display_driver
from display_driver import disp
import time
lv.init()

#### Set backlight ####
disp.set_backlight(50)
#disp.set_backlight(100)
#### UI ####
scr = lv.obj()
lv.screen_load(scr)

red = lv.PALETTE.RED
blue = lv.PALETTE.BLUE
yellow = lv.PALETTE.YELLOW
green = lv.PALETTE.GREEN

color = blue

btn = lv.button(scr)
btn.set_style_bg_color(lv.palette_main(color),0)
btn.center()

lbl = lv.label(btn)
lbl.set_text("Hello")

