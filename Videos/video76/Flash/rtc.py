
class RTC(object):
    def __init__(self, i2c, device_addr = 0x68):
        self.i2c = i2c
        self.device_addr = device_addr
    def read_reg(self, reg, len):
        data = self.i2c.readfrom_mem(self.device_addr, reg, len, addrsize = 8)
        return data
    def write_reg(self, reg, value):
        self.i2c.writeto_mem(self.device_addr, reg, value)
    def __bcd2dec(self, bcd):
        return (((bcd & 0xF0) >> 4) * 10 + (bcd & 0x0F))
    def __dec2bcd(self, dec):
        return (((dec // 10) << 4) | (dec % 10))

class PCF85063(RTC):
    def __init__(self, i2c, device_addr = 0x51):
        self.i2c = i2c
        self.device_addr = device_addr
        PCF85063_SECONDS = 0x04
        seconds = self.read_reg(PCF85063_SECONDS, 1)
        if seconds[0] & 0x08:
            print("oscillator_stop detected!")
        else:
            print("RTC has beeing kept running!")
    
    def get_time(self):
        PCF85063_SECONDS = 0x04
        reg_data = self.read_reg(PCF85063_SECONDS, 7)
        time = {
            "seconds": self.__bcd2dec(reg_data[0] & 0x7F),
            "minutes": self.__bcd2dec(reg_data[1] & 0x7F),
            "hours": self.__bcd2dec(reg_data[2] & 0x3F),
            "day": self.__bcd2dec(reg_data[3] & 0x3F),
            "weekday": self.__bcd2dec(reg_data[4] & 0x7),
            "month": self.__bcd2dec(reg_data[5] & 0x1F),
            "year": self.__bcd2dec(reg_data[6]),
        }
        return time
    
    def set_time(self, time):
        PCF85063_SECONDS = 0x04
        buf = bytearray(7)
        buf[0] = self.__dec2bcd(time["seconds"]) & 0x7F
        buf[1] = self.__dec2bcd(time["minutes"]) & 0x7F
        buf[2] = self.__dec2bcd(time["hours"]) & 0x3F
        buf[3] = self.__dec2bcd(time["day"]) & 0x3F
        buf[4] = self.__dec2bcd(time["weekday"]) & 0x7
        buf[5] = self.__dec2bcd(time["month"] - 1) & 0x1F
        buf[6] = self.__dec2bcd(time["year"] - 2000)
        self.write_reg(PCF85063_SECONDS, buf)


