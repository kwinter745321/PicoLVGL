import lvgl as lv
lv.init()

# Create an event loop and Register SDL display/mouse/keyboard drivers.
from lv_utils import event_loop

WIDTH = 480
HEIGHT = 320

event_loop = event_loop()
disp_drv = lv.sdl_window_create(WIDTH, HEIGHT)
disp_drv.set_default()
display = lv.display_get_default()

group = lv.group_create()
group.set_default()

mouse = lv.sdl_mouse_create()
mouse.set_display(display)
mouse.set_group(group)

keyboard = lv.sdl_keyboard_create()
keyboard.set_display(display)
keyboard.set_group(group)
