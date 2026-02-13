from machine import Pin, SoftI2C
import time


class CST328(object):
    def __init__(self, i2c, width, height, device_addr = 0x1A, rotation = 0, offset_x = 0, offset_y = 0):
        self.i2c = i2c
        self.width = width
        self.height = height
        self.device_addr = device_addr
        self.rotation = rotation
        self.offset_x = offset_x
        self.offset_y = offset_y
        self.read_flag = False
        self.rst = Pin(17, Pin.OUT)
        #self.int = Pin(18, Pin.IN, Pin.PULL_UP)
        #self.int.irq(handler = self.int_callback, trigger = Pin.IRQ_FALLING)
        self.coords = [{"x": 0, "y": 0, "pressure": 0} for _ in range(5)]
        self.points = 0
        self.reset()
        id = self.read_id()
        if id :
            print("0xCACA is OK!")
        else:
            print("0xCACA is not OK!")
    
    def int_callback(self, pin):
        self.read_flag = True
        return
    
    def reset(self):
        self.rst(1)
        time.sleep(0.01)
        self.rst(0)
        time.sleep(0.01)
        self.rst(1)
        time.sleep(0.1)
        return
    
    def write(self, buf):
        buf_high = (buf >> 8) & 0xFF
        buf_low = buf & 0xFF
        self.i2c.writeto_mem(self.device_addr, buf_high, bytes([buf_low]), addrsize = 8)
        
    def write_reg(self, reg, value):
        self.i2c.writeto_mem(self.device_addr, reg, value, addrsize = 16)
    
    def read_reg(self, reg, len):
        data = self.i2c.readfrom_mem(self.device_addr, reg, len, addrsize = 16)
        return data

    def read_id(self):
        buf = bytearray(24)
        HYN_REG_MUT_DEBUG_INFO_MODE         = 0xD101
        HYN_REG_MUT_NORMAL_MODE             = 0xD109
        HYN_REG_MUT_DEBUG_INFO_TP_NTX       = 0xD1F4
        HYN_REG_MUT_DEBUG_INFO_RES_X        = 0xD1F8
        HYN_REG_MUT_DEBUG_INFO_BOOT_TIME    = 0xD1FC
        self.write(HYN_REG_MUT_DEBUG_INFO_MODE)
        buf = self.read_reg(HYN_REG_MUT_DEBUG_INFO_BOOT_TIME, 4)
        #print("TouchPad_ID:" + hex(buf[0]) + "," + hex(buf[1]) + "," + hex(buf[2]) + "," + hex(buf[3]))
        buf = self.read_reg(HYN_REG_MUT_DEBUG_INFO_RES_X, 4)
        #print("TouchPad_X_MAX:" + str(buf[1]*256+buf[0]))
        #print("TouchPad_Y_MAX:" + str(buf[3]*256+buf[2]))
        buf = self.read_reg(HYN_REG_MUT_DEBUG_INFO_TP_NTX, 24)
        #print("D1F4:" + hex(buf[0]) + "," + hex(buf[1]) + "," + hex(buf[2]) + "," + hex(buf[3]))
        #print("D1F8:" + hex(buf[4]) + "," + hex(buf[5]) + "," + hex(buf[6]) + "," + hex(buf[7]))
        #print("D1FC:" + hex(buf[8]) + "," + hex(buf[9]) + "," + hex(buf[10]) + "," + hex(buf[11]))
        #print("D200:" + hex(buf[12]) + "," + hex(buf[13]) + "," + hex(buf[14]) + "," + hex(buf[15]))
        #print("D204:" + hex(buf[16]) + "," + hex(buf[17]) + "," + hex(buf[18]) + "," + hex(buf[19]))
        #print("D208:" + hex(buf[20]) + "," + hex(buf[21]) + "," + hex(buf[22]) + "," + hex(buf[23]))
        #print("CACA Read:" + hex((buf[11]<< 8) | buf[10]))
        
        self.write(HYN_REG_MUT_NORMAL_MODE)
        if (((buf[11] << 8) | buf[10]) != 0xCACA):
            return False
        return True
        
    def get_coords(self):
        if self.points == 0:
            return None
        else:
            coords = [{"x": self.coords[i]["x"], "y": self.coords[i]["y"], "pressure": self.coords[i]["pressure"]} for i in range(self.points)]
            return coords
        
    def raw2px(self,x,y):
        #print("raw2px wd,ht,rot:",self.width,self.height,self.rotation)
        if   self.rotation==0: return x,y
        elif self.rotation==1: return y,self.width-x-80
        elif self.rotation==2: return self.width-x,self.height-y
        else:             return self.width-y,x
        
    def read_touch(self):
        self.points = 0
        #if self.read_flag == False:
        #    return False
        CST328_TOUCH_FLAG_AND_NUM_REG = 0xD005
        CST328_coords_REG = 0xD000
        buf = bytearray(28)
        buf = self.read_reg(CST328_TOUCH_FLAG_AND_NUM_REG, 1)
        
        if ((buf[0] & 0x0F) == 0x00):
            return False
        self.points = buf[0] & 0x0F;
        
        buf = self.read_reg(CST328_coords_REG, 27)
        if ((buf[0] & 0x0F) != 0x06):
            return False
        num = 0
        for i in range(self.points):
            if i > 0:
                num = 2
            self.coords[i]["x"] = ((buf[(i * 5) + 1 + num] << 4) + ((buf[(i * 5) + 3 + num] & 0xF0)>> 4))   
            self.coords[i]["y"] = ((buf[(i * 5) + 2 + num] << 4) + ( buf[(i * 5) + 3 + num] & 0x0F))
            self.coords[i]["pressure"] = (buf[(i * 5) + 4 + num])
        return True
 