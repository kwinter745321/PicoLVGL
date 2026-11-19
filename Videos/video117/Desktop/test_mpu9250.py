import utime
from machine import I2C, Pin
from mpu9250 import MPU9250

i2c = I2C(scl=Pin(9), sda=Pin(8))
sensor = MPU9250(i2c)

print("MPU9250 id: " + hex(sensor.whoami))

while True:
    print(sensor.acceleration)
    print(sensor.gyro)
    print(sensor.magnetic)
    print(sensor.temperature)

    utime.sleep_ms(1000)