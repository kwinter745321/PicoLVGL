# Test_scan_I2c.py
#
# Verified: 30 June 2025
#
# MicroPython v1.25.0-dirty on 2025-06-30; Raspberry Pi Pico 2 W with RP2350
#
from machine import Pin, I2C, SoftI2C
import time

##### definitions #############
I2C_SDA_PIN = 20
I2C_SCL_PIN = 21  
I2C_FREQ = 10000

USER_BUTTON_PIN = 6 

#### Init #####################
scl = Pin(I2C_SCL_PIN, mode=Pin.OUT)
sda = Pin(I2C_SDA_PIN, mode=Pin.OUT)
user = Pin(USER_BUTTON_PIN, Pin.IN)

i2c=SoftI2C( scl=Pin(I2C_SCL_PIN), sda=Pin(I2C_SDA_PIN), freq=I2C_FREQ)

#### Test Program #####################
try:
    print("----------------")
    print("Program started.")
    print("* User button setup at", user)
    print("* Test scan of I2C devices.")
    print("*",i2c)
    print("Press User button to start test or Control-c in Shell to exit.")
    user_btn = user.value()
    #print("user button=",user_btn)
    
    while user_btn != 0:
        time.sleep(.5)
        user_btn = user.value()
        #print("user button=",user_btn)
        
    print("User button pressed.\n")
    print('Scanning I2C bus...')
    devices = i2c.scan() 
    print('Scan finished.')
    device_count = len(devices)

    if device_count == 0:
        print('No I2C device found.')
    else:
        print('I2C devices found:',device_count)
        print("| Decimal Address | Hex Address |")
        print("| --------------- | ----------- |")
        for device in devices:
            xdevice = str(hex(device))
            print("| %15s " % device,end="")
            print("| %9s " % xdevice," |")

except KeyboardInterrupt:
    done = True
    print('Interrupted by Control-c.')
finally:
    print('Finished.')
    

