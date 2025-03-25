# test_ili9xxx_demo.py
#
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-724-gbf1107420 on 2025-02-19; Raspberry Pi Pico with RP2040
# Raspberry Pi Pico (RP2040)
# LVGL 9.1                    https://docs.lvgl.io/9.1/
#
# 
import lvgl as lv
import ili9xxx
import xpt2046
from machine import SPI, Pin
import time

# Initialize LVGL
lv.init()
print("Running LVGL %d.%d" % (lv.version_major(), lv.version_minor() )  )

# Initialize display
spi = SPI(0, baudrate=20_000_000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
tspi = SPI(0, baudrate=2_000_000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
print("Init SPI")
disp = ili9xxx.Ili9341(spi=spi, dc=0, cs=17, rst=1, rot=1)

print("Init disp")
disp.clear(0x000000)
print("Pause 1 sec.")
time.sleep(1)

# Create screen object
hres = 320
vres = 240
disp_drv = lv.display_create(hres,vres)
print("Screen config")
scr = lv.screen_active()
#scr = lv.obj()

# Initialize touch screen
touch = xpt2046.Xpt2046_hw(spi=tspi,cs=21,rot=1)
print("Using Touch setup")

# @micropython.native
def tsread(indev_drv, data) -> int:
    coords = touch.pos()
    if coords:
        data.point.x, data.point.y = coords
        data.state = lv.INDEV_STATE.PRESSED
        return True
    data.state = lv.INDEV_STATE.RELEASED
    return False

# indev for touch screen
indev_drv = lv.indev_create()
indev_drv.set_type(lv.INDEV_TYPE.POINTER)
indev_drv.set_read_cb(tsread)

###############################################
# UI
###############################################
    
#### tabview ##################
    
tv = lv.tabview(scr)
tv.set_style_border_width(2, 0)
tv.set_style_border_color(lv.palette_main(lv.PALETTE.CYAN),0)

ft = tv.add_tab("Switch")
st = tv.add_tab("Slider")
tt = tv.add_tab("Checkbox")


###### Switch TAB ###############################

ft_sw = lv.switch(ft)
ft_sw.set_pos(100, 50)
ft_sw.set_state(lv.STATE.CHECKED, True)

ft_lbl = lv.label(ft)
ft_lbl.set_pos(170, 50)


def check_sw():
    state = ft_sw.has_state(lv.STATE.CHECKED)
    if state == True:
        ft_lbl.set_text("ON")
    else:
        ft_lbl.set_text("OFF")


###### Slider TAB ###############################

def slider_event_cb(event):
    val = slider.get_value()
    label.set_text(str(val))

st_lbl = lv.label(st)
st_lbl.set_text("20")
st_lbl.set_pos(142,35)

st_slider = lv.slider(st)
st_slider.set_value(20,0)
st_slider.set_pos(10,120)


st_arc = lv.arc(st)
st_arc.set_pos(100,10)
st_arc.set_size(110,110)
st_arc.set_value(20)


st_arc_status = lv.label(st_arc)
st_arc_status.center()
st_arc_status.set_text("Low")
st_arc.set_style_arc_color(lv.palette_main(lv.PALETTE.YELLOW),0)

def filter_val(v):
    val = v
    if v > 90:
        val = 90
    if v < 20:
        val = 20
    return val

def st_slider_event_cb(event):
    v = st_slider.get_value()
    val = filter_val(v)
    st_arc.set_value(val)
    st_lbl.set_text(str(val))
    if val > 70:
        st_arc_status.set_text("High")
        st_arc.set_style_arc_color(lv.palette_main(lv.PALETTE.RED),0)
    elif val < 30:
        st_arc_status.set_text("Low")
        st_arc.set_style_arc_color(lv.palette_main(lv.PALETTE.YELLOW),0)
    else:
        st_arc_status.set_text("Normal")
        st_arc.set_style_arc_color(lv.palette_main(lv.PALETTE.GREEN),0)
        
st_slider.add_event_cb(st_slider_event_cb, lv.EVENT.VALUE_CHANGED, None)

######## Checkbox TAB ###########################
tt_chk1 = lv.checkbox(tt)
tt_chk1.set_pos(10,10)
tt_chk1.set_text("Apple")

tt_chk2 = lv.checkbox(tt)
tt_chk2.set_pos(10,50)
tt_chk2.set_text("Banana")

tt_chk3 = lv.checkbox(tt)
tt_chk3.set_pos(10,90)
tt_chk3.set_text("Cherry")

tt_ta = lv.textarea(tt)
tt_ta.set_pos(140,10)
tt_ta.set_size(160,110)
#tt_ta.set_style_bg_color(lv.palette_main(lv.PALETTE.GREY),0)
tt_ta.set_style_bg_color(lv.color_hex(0xC0C0C0), lv.PART.MAIN)
tt_ta.set_style_text_color(lv.color_hex(0x000000),0)

tt_text = ""

chk1 = ""
chk2 = ""
chk3 = ""
        
def update_tt_ta():
    global chk1, chk2, chk3
    txt = "List: \n"
    if len(chk1) > 0:
        txt += chk1 + ", \n"
    if len(chk2) > 0:
        txt += chk2 + ", \n"
    if len(chk3) > 0:
        txt += chk3 + ", \n"
    tt_ta.set_text(txt)

def chk1_event_cb(event):
    global chk1, chk2, chk3
    state = tt_chk1.get_state()
    item = tt_chk1.get_text() 
    if state == 3:
        chk1 = item
    else:
        chk1 = ""
    update_tt_ta()

def chk2_event_cb(event):
    global chk1, chk2, chk3
    state = tt_chk2.get_state()
    item = tt_chk2.get_text() 
    if state == 3:
        chk2 = item
    else:
        chk2 = ""
    update_tt_ta()

def chk3_event_cb(event):
    global chk1, chk2, chk3
    state = tt_chk3.get_state()
    item = tt_chk3.get_text() 
    if state == 3:
        chk3 = item
    else:
        chk3 = ""
    update_tt_ta()


tt_chk1.add_event_cb(chk1_event_cb, lv.EVENT.VALUE_CHANGED, None)
tt_chk2.add_event_cb(chk2_event_cb, lv.EVENT.VALUE_CHANGED, None)
tt_chk3.add_event_cb(chk3_event_cb, lv.EVENT.VALUE_CHANGED, None)




lv.screen_load(scr)
        
#theme for current screen
dispp = lv.display_get_default()
theme = lv.theme_default_init(dispp, lv.palette_main(lv.PALETTE.BLUE), lv.palette_main(lv.PALETTE.RED), True, lv.font_default())
dispp.set_theme(theme)


# Run the event loop
while True:
    lv.timer_handler()
    check_sw()
    time.sleep_ms(10)




