# test_hello_display.py
#
# Created: 17 October 2025
# Revised: 06 February 2026
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.28.0-preview.80.gb14d129a16.dirty on 2026-01-22;
# Raspberry Pi Pico 2 W with RP2350
# LVGL 9.3
import _thread

from machine import reset, Pin
#import display_driver

import time
import gc

spLock = _thread.allocate_lock()

print("core0: GC free:",gc.mem_free() )

def core_one_task():
    print("Core1 task")
    with spLock:
        import lvgl as lv
        from display_driver import disp
        lv.init()
        backlight = Pin(13,Pin.OUT)
        backlight.on()

        #### UI ####
        scr = lv.obj()
        lv.screen_load(scr)

        scr.set_style_bg_color(lv.color_hex(0),lv.PART.MAIN)

        red = lv.palette_main(lv.PALETTE.RED)
        blue = lv.palette_main(lv.PALETTE.BLUE)
        yellow = lv.palette_main(lv.PALETTE.YELLOW)
        green = lv.palette_main(lv.PALETTE.GREEN)

        btn = lv.button(scr)
        btn.set_size(120,40)
        btn.set_style_bg_color(blue,0)
        btn.center()

        lbl = lv.label(btn)
        lbl.set_text("Hello")
        lbl.set_style_text_color(lv.color_black(),0)
        lbl.set_style_text_font(lv.font_montserrat_24,0)
        lbl.center()

        #### Border
        scr.set_style_border_width(2, lv.PART.MAIN)
        scr.set_style_border_color(green,lv.PART.MAIN)
        #############################################
        print("core1: GC free:",gc.mem_free() )
        gc.collect()
        print("core1: GC free:",gc.mem_free() )
    
    while True:
        lv.task_handler()
        lv.indev_t()

def do_connect():
    print("do_connect routine")
    import network
    sta_if = network.WLAN(network.WLAN.IF_STA)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('ssid', 'pwd')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ipconfig('addr4'))

def do_core0_task():
    print("core0 task")

_thread.start_new_thread(core_one_task, () )

time.sleep(1)

m = Pin(21, Pin.IN, Pin.PULL_UP)
cnt = 0

print("Press Momentary Button1 to start Core0 code.")
while m.value() == 1:
    time.sleep_ms(50)

print("Core0 code continues")
m.value(1)
time.sleep(1)
print("Core0 code continues m:",m.value())
print("Run do_connect using Lock")


while True:
    with spLock:
        do_core0_task()
        if m.value() == 0:
            do_connect()
        time.sleep(1)
