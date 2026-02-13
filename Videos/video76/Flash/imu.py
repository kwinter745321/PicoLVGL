from machine import Pin, I2C
import time

I2C_SCL = 7
I2C_SDA = 6

class IMU(object):
    def __init__(self, i2c, device_addr = 0x68):
        self.i2c = i2c
        self.device_addr = device_addr
    def read_reg(self, reg, len):
        data = self.i2c.readfrom_mem(self.device_addr, reg, len, addrsize = 8)
        return data
    def write_reg(self, reg, value):
        self.i2c.writeto_mem(self.device_addr, reg, bytes([int(value)]))
        
        
class QMI8658(IMU):
    def __init__(self, i2c, device_addr = 0x6B):
        super().__init__(i2c, device_addr)
        time.sleep(0.01)
        self.write_reg(0x60, 0xb0)
        time.sleep(0.01)
        self.write_reg(0x02, 0x40)
        # REG CTRL2 : QMI8658AccRange_8g  and QMI8658AccOdr_1000Hz
        self.write_reg(0x03, 0x95)
        # REG CTRL3 : QMI8658GyrRange_512dps and QMI8658GyrOdr_1000Hz
        self.write_reg(0x04, 0xd5)
        # REG CTRL4 : No
        self.write_reg(0x05, 0x00)
        # REG CTRL5 : Enable Gyroscope And Accelerometer Low-Pass Filter 
        self.write_reg(0x06, 0x11)
        # REG CTRL6 : Disables Motion on Demand.
        self.write_reg(0x07, 0x00)
        # REG CTRL7 : Enable Gyroscope And Accelerometer
        self.write_reg(0x08, 0x03)
        time.sleep(0.1)
    
    def read_raw_data(self):
        QMI8658_STATUS0 = 0x2E
        QMI8658_AX_L = 0x35
        QMI8658_TIMESTAMP_LOW = 0x30
        QMI8658_TEMP_L = 0x33
        status = self.read_reg(QMI8658_STATUS0, 1)
        if status[0] & 0x03:
            reg_data = self.read_reg(QMI8658_AX_L, 12)
            data = [0, 0, 0, 0, 0, 0]
            for i in range(6):
                data[i] = (reg_data[(i * 2) + 1] << 8) | (reg_data[i * 2])
                if data[i] >= 32767:
                    data[i] = data[i] - 65535
            reg_data = self.read_reg(QMI8658_TIMESTAMP_LOW, 3)
            timestamp = (reg_data[2] << 16) | (reg_data[1] << 8) | reg_data[0]
            
            reg_data = self.read_reg(QMI8658_TEMP_L, 2)
            temperature = reg_data[1] + reg_data[0] / 256.0
            temperature = round(temperature, 2)
            raw_data = {
                "accel_x": data[0],
                "accel_y": data[1],
                "accel_z": data[2],
                "gyro_x": data[3],
                "gyro_y": data[4],
                "gyro_z": data[5],
                "timestamp": timestamp,
                "temperature": temperature
            }
            return raw_data
        return None
    
if __name__ == "__main__":
    i2c = I2C(id = 1, scl = Pin(I2C_SCL), sda = Pin(I2C_SDA), freq = 400_000)
    qmi8658 = QMI8658(i2c)
    while True:
        raw_data = qmi8658.read_raw_data()
        if raw_data:
            print("accel:" + str(raw_data.get("accel_x"))+ ", " + str(raw_data.get("accel_y")) + ", " + str(raw_data.get("accel_z")))
            print("gyro:" + str(raw_data.get("gyro_x"))+ ", " + str(raw_data.get("gyro_y")) + ", " + str(raw_data.get("gyro_z")))
            print("temperature:" + str(raw_data.get("temperature")))
            print("timestamp:" + str(raw_data.get("timestamp")))
            print("--------------------")
        time.sleep(0.05)