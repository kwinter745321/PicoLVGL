import lvgl as lv
from machine import reset
import display_driver
from display_driver import disp
import time
lv.init()

#### Set backlight ####
disp.set_backlight(50)

#### UI ####
scr = lv.obj()
lv.screen_load(scr)

red = lv.PALETTE.RED

points = [{"x": 0, "y": 0},{"x": 0, "y": 25}]
line0 = lv.line(scr)
line0.set_style_line_color(lv.palette_main(red),0)
line0.set_style_line_width(1,0)
line0.set_points(points,2)

points = [{"x": 5, "y": 0},{"x": 5, "y": 25}]
line5 = lv.line(scr)
line5.set_style_line_color(lv.palette_main(red),0)
line5.set_style_line_width(1,0)
line5.set_points(points,2)

points = [{"x": 125, "y": 0},{"x": 125, "y": 25}]
line125 = lv.line(scr)
line125.set_style_line_color(lv.palette_main(red),0)
line125.set_style_line_width(1,0)
line125.set_points(points,2)

points = [{"x": 127, "y": 0},{"x": 127, "y": 25}]
line127 = lv.line(scr)
line127.set_style_line_color(lv.palette_main(red),0)
line127.set_style_line_width(1,0)
line127.set_points(points,2)

