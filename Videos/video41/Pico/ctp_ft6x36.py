# ctp_ft6x36.py
#
# Created: 24 June 2025 
#
# Copyright (C) 2025 KW Services.
# MIT License
# MicroPython v1.20.0-2504.g9fe842956 on 2025-04-04; Raspberry Pi Pico with RP2040
# LVGL 9.3 
# 
import lvgl as lv
from machine import I2C, Pin, SoftI2C
import time

class ft6x36:
    
    touched = 1  #self.touched set-high (0 = touched)

    def __init__(self, i2c_dev=0, sda=8, scl=9, reset=7, irq=6, freq=400000, addr=0x38, width=480, height=320, 
                 inv_x=False, inv_y=False, swap_xy=False):
        if not lv.is_initialized():
            lv.init()
        if swap_xy == True:
            self.height, self.width = width, height
        else:
            self.width, self.height = width, height
        self.inv_x, self.inv_y, self.swap_xy = inv_x, inv_y, swap_xy
        #self.i2c = I2C(i2c_dev, sda=Pin(sda), scl=Pin(scl), freq=freq)
        self.i2c = SoftI2C(sda=Pin(sda), scl=Pin(scl), freq=freq)
        rst = Pin(reset, mode=Pin.OUT)
        rst.off()
        rst.on()
        ctp = Pin(irq, Pin.IN)
        self.addr = addr
        try:
            print("FT6X36 touch IC ready (fw id 0x{0:X} rel {1:d}, lib {2:X})".format( \
                int.from_bytes(self.i2c.readfrom_mem(self.addr, 0xA6, 1), "big"), \
                int.from_bytes(self.i2c.readfrom_mem(self.addr, 0xAF, 1), "big"), \
                int.from_bytes(self.i2c.readfrom_mem(self.addr, 0xA1, 2), "big") \
            ))
        except:
            print("FT6X36 touch IC not responding")
            return
        self.point = lv.point_t( {'x': 0, 'y': 0} )
        self.state = lv.INDEV_STATE.RELEASED
        self.indev_drv = lv.indev_create()
        self.indev_drv.set_type(lv.INDEV_TYPE.POINTER)
        self.indev_drv.set_read_cb(self.callback)
        
        def fetch(pin):
            self.setTouched()
            # debounce the touch
            time.sleep_ms(20)
        
        ctp.irq(trigger=Pin.IRQ_FALLING, handler=fetch)
        
    def setTouched(self):
        self.touched = 0
   
    def getTouchValue(self):
        if self.touched == 0:
            sensorbytes = self.i2c.readfrom_mem(self.addr, 3, 10)
            x = (sensorbytes[0] << 8 | sensorbytes[1]) & 0x0fff
            y = (sensorbytes[2] << 8 | sensorbytes[3]) & 0x0fff
            pt = lv.point_t()
            pt.x = x
            pt.y = y
            return pt

    def callback(self, driver, data):

        def get_point():
            pt = self.getTouchValue()
            if pt != None:
                x = pt.x
                y = pt.y
                wd = self.width
                ht = self.height
                if self.inv_x == True and self.inv_y == True:
                    wd = self.height
                    ht = self.width
                x = wd - x - 1 if self.inv_x else x
                y = ht - y - 1 if self.inv_y else y
                (x, y) = (y, x) if self.swap_xy else (x, y)
                return { 'x': x, 'y': y }
        
        if self.touched == 0:
            data.point = get_point()
            self.touched = 1
            self.state = lv.INDEV_STATE.PRESSED
            data.state = self.state
        else:
            self.state = lv.INDEV_STATE.RELEASED
            data.state = self.state


