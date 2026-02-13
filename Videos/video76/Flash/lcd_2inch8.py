from machine import Pin, SPI, PWM, I2C
import framebuf
import time

LCD_SCLK = 10
LCD_MOSI = 11
LCD_MISO = 12
LCD_CS = 13
LCD_DC = 14
LCD_RST = 15
LCD_BL = 16

TP_SCL = 7
TP_SDA = 6
TP_RST = 17
TP_INT = 18

class ST7789(framebuf.FrameBuffer):
    def __init__(self, width, height, rotation = 0, offset_x = 0, offset_y = 0):
        self.spi = SPI(1, 80_000_000, polarity = 0, phase = 0, bits = 8, sck = Pin(LCD_SCLK), mosi = Pin(LCD_MOSI), miso = None)
        self.cs = Pin(LCD_CS, Pin.OUT)
        self.dc = Pin(LCD_DC, Pin.OUT)
        self.rst = Pin(LCD_RST, Pin.OUT)
        self.bl = PWM(Pin(LCD_BL))
        self.bl.freq(5000)
        self.width = width
        self.height = height
        self.rotation = rotation
        self.offset_x = offset_x
        self.offset_y = offset_y
        # Define color, Micropython fixed to BRG format  定义颜色，Micropython固定为BRG格式
        self.red   =   0x07E0
        self.green =   0x001f
        self.blue  =   0xf800
        self.white =   0xffff
        self.black =   0x0000
        self.brown =   0X8430
        
        self.buffer = bytearray(self.height * self.width * 2)
        super().__init__(self.buffer, self.width, self.height, framebuf.RGB565)
        self.reset()
        self.config()
        self.fill(self.white) #Clear screen  清屏
        self.show()#Show  显示
    
    def write_cmd(self, cmd):
        self.cs(0)
        self.dc(0)
        self.spi.write(bytearray([cmd]))
        self.cs(1)
    
    def write_data(self, data):
        self.cs(0)
        self.dc(1)
        self.spi.write(bytearray([data]))
        self.cs(1)
    def set_brightness(self, brightness):
        if brightness > 100:
            brightness = 100
        duty = int(65535 / 100 * brightness)
        self.bl.duty_u16(duty)
    def reset(self):
        self.rst(1)
        time.sleep(0.01)
        self.rst(0)
        time.sleep(0.01)
        self.rst(1)
    def set_windows(self, x0, y0, x1, y1):
        x0 = x0 + self.offset_x
        y0 = y0 + self.offset_y
        x1 = x1 + self.offset_x
        y1 = y1 + self.offset_y
        
        self.write_cmd(0x2a)
        self.write_data(x0 >> 8)
        self.write_data(x0 & 0xff)
        self.write_data(x1 >> 8)
        self.write_data(x1 & 0xff)
        self.write_cmd(0x2b)
        self.write_data(y0 >> 8)
        self.write_data(y0 & 0xff)
        self.write_data(y1 >> 8)
        self.write_data(y1 & 0xff)
        self.write_cmd(0x2c)
    def flush(self, color):
        self.dc(1)
        self.cs(0)
        self.spi.write(color)
        self.cs(1)
        
    def show(self): 
        self.set_windows(0,0,self.width,self.height)
        self.dc(1)
        self.cs(0)
        self.spi.write(self.buffer)
        self.cs(1)
    def write_text(self, text, x, y, size, color):
        ''' Method to write Text on OLED/LCD Displays
            with a variable font size

            Args:
                text: the string of chars to be displayed
                x: x co-ordinate of starting position
                y: y co-ordinate of starting position
                size: font size of text
                color: color of text to be displayed
        '''
        background = self.pixel(x,y)
        info = []
        # Creating reference charaters to read their values
        self.text(text,x,y,color)
        for i in range(x,x+(8*len(text))):
            for j in range(y,y+8):
                # Fetching amd saving details of pixels, such as
                # x co-ordinate, y co-ordinate, and color of the pixel
                px_color = self.pixel(i,j)
                info.append((i,j,px_color)) if px_color == color else None
        # Clearing the reference characters from the screen
        self.text(text,x,y,background)
        # Writing the custom-sized font characters on screen
        for px_info in info:
            self.fill_rect(size*px_info[0] - (size-1)*x , size*px_info[1] - (size-1)*y, size, size, px_info[2]) 
    def config(self):
        self.write_cmd(0x36)
        self.write_data(0x00)

        self.write_cmd(0x3A)
        self.write_data(0x05)

        self.write_cmd(0xB2)
        self.write_data(0x0B)
        self.write_data(0x0B)
        self.write_data(0x00)
        self.write_data(0x33)
        self.write_data(0x35)

        self.write_cmd(0xB7)
        self.write_data(0x11)

        self.write_cmd(0xBB)
        self.write_data(0x35)

        self.write_cmd(0xC0)
        self.write_data(0x2C)

        self.write_cmd(0xC2)
        self.write_data(0x01)

        self.write_cmd(0xC3)
        self.write_data(0x0D)

        self.write_cmd(0xC4)
        self.write_data(0x20)

        self.write_cmd(0xC6)
        self.write_data(0x13)

        self.write_cmd(0xD0)
        self.write_data(0xA4)
        self.write_data(0xA1)

        self.write_cmd(0xD6)
        self.write_data(0xA1)

        self.write_cmd(0xE0)
        self.write_data(0xF0)
        self.write_data(0x06)
        self.write_data(0x0B)
        self.write_data(0x0A)
        self.write_data(0x09)
        self.write_data(0x26)
        self.write_data(0x29)
        self.write_data(0x33)
        self.write_data(0x41)
        self.write_data(0x18)
        self.write_data(0x16)
        self.write_data(0x15)
        self.write_data(0x29)
        self.write_data(0x2D)

        self.write_cmd(0xE1)
        self.write_data(0xF0)
        self.write_data(0x04)
        self.write_data(0x08)
        self.write_data(0x08)
        self.write_data(0x07)
        self.write_data(0x03)
        self.write_data(0x28)
        self.write_data(0x32)
        self.write_data(0x40)
        self.write_data(0x3B)
        self.write_data(0x19)
        self.write_data(0x18)
        self.write_data(0x2A)
        self.write_data(0x2E)

        self.write_cmd(0x21)

        self.write_cmd(0x11)
        time.sleep(0.12)
        self.write_cmd(0x29)


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
        self.int = Pin(18, Pin.IN, Pin.PULL_UP)
        self.int.irq(handler = self.int_callback, trigger = Pin.IRQ_FALLING)
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
        print("TouchPad_ID:" + hex(buf[0]) + "," + hex(buf[1]) + "," + hex(buf[2]) + "," + hex(buf[3]))
        buf = self.read_reg(HYN_REG_MUT_DEBUG_INFO_RES_X, 4)
        print("TouchPad_X_MAX:" + str(buf[1]*256+buf[0]))
        print("TouchPad_Y_MAX:" + str(buf[3]*256+buf[2]))
        buf = self.read_reg(HYN_REG_MUT_DEBUG_INFO_TP_NTX, 24)
        print("D1F4:" + hex(buf[0]) + "," + hex(buf[1]) + "," + hex(buf[2]) + "," + hex(buf[3]))
        print("D1F8:" + hex(buf[4]) + "," + hex(buf[5]) + "," + hex(buf[6]) + "," + hex(buf[7]))
        print("D1FC:" + hex(buf[8]) + "," + hex(buf[9]) + "," + hex(buf[10]) + "," + hex(buf[11]))
        print("D200:" + hex(buf[12]) + "," + hex(buf[13]) + "," + hex(buf[14]) + "," + hex(buf[15]))
        print("D204:" + hex(buf[16]) + "," + hex(buf[17]) + "," + hex(buf[18]) + "," + hex(buf[19]))
        print("D208:" + hex(buf[20]) + "," + hex(buf[21]) + "," + hex(buf[22]) + "," + hex(buf[23]))
        print("CACA Read:" + hex((buf[11]<< 8) | buf[10]))
        
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
        
    def read_touch(self):
        self.points = 0
        if self.read_flag == False:
            return False
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
            
