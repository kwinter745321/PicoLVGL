import sys
sys.path.append('.')
import lvgl as lv
import lv_utils
import gc
import time



class lv_port(object):
    def __init__(self, display, touch):
        self.display = display
        self.touch = touch
        color_format = lv.COLOR_FORMAT.RGB565
        self.pixel_size = lv.color_format_get_size(color_format)
        self.rgb565_swap_func = lv.draw_sw_rgb565_swap
        if lv.is_initialized(): 
            lv.deinit()
            time.sleep(0.1)
        lv.init()
        
        if lv_utils.event_loop.is_running(): 
            lv_utils.event_loop().deinit()
            time.sleep(0.1)    
        lv_utils.event_loop()
        
        self.buf1 = lv.draw_buf_create(self.display.width, self.display.height // 3, color_format, 0)
        self.buf2 = lv.draw_buf_create(self.display.width, self.display.height // 3, color_format, 0) 
        self.disp_drv = lv.display_create(self.display.width, self.display.height) 
        self.disp_drv.set_color_format(color_format)
        self.disp_drv.set_draw_buffers(self.buf1, self.buf2)
        self.disp_drv.set_render_mode(lv.DISPLAY_RENDER_MODE.PARTIAL)
        self.disp_drv.set_flush_cb(self.disp_drv_flush_cb)
    
        self.indev_drv = lv.indev_create()
        self.indev_drv.set_type(lv.INDEV_TYPE.POINTER)
        self.indev_drv.set_read_cb(self.indev_drv_read_cb)
    def indev_drv_read_cb(self, indev_drv, data):
        data.state = 0
        if self.touch.read_touch():
            coords =  self.touch.get_coords()
            if coords != None:
                data.point.x = coords[0]["x"]
                data.point.y = coords[0]["y"]
                data.state = 1
        gc.collect()
    def disp_drv_flush_cb(self, disp_drv, area, color_p):
        x1, y1, x2, y2 = area.x1, area.y1, area.x2, area.y2
        w = area.x2 - area.x1 + 1
        h = area.y2 - area.y1 + 1
        size = w * h
        data_view = color_p.__dereference__(size * self.pixel_size)
        self.rgb565_swap_func(data_view, size)
        self.display.set_windows(x1, y1, x2, y2)
        self.display.flush(data_view)
        disp_drv.flush_ready()
        gc.collect()