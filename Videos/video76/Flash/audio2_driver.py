# audio_driver.py
#
# Created: 03 February 2026 (custom to the device)
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# Waveshare ESP32-S3-Touch-LCD-3.5C
# MicroPython v1.20.0-2510.gacfeb7b7e.dirty on 2025-11-23;
# Generic ESP32S3 module with ESP32S3
#

from machine import reset, Pin, PWM
from display_driver import disp, touch
import time, os
import machine
from machine import SoftI2C,SoftSPI
from machine import I2S
from sdcard import SDCard
import gc

#import es8311

#i2c = SoftI2C( scl=Pin(7), sda=Pin(6), freq=100_000)

#### I2S ####################
mck_pin = -1       # master clock
sck_pin = Pin(2)   # Serial clock output
ws_pin = Pin(3)    # Word clock output
sd_pin = Pin(4)    # Serial data output

SAMPLE_RATE = 44100   #16000   #44100
BUFFER_SIZE = 1024  #1024 # Buffer size for reading file chunks

##### Master Clock ############
#CLOCK_PIN = 12                     # MCK pin
#MASTER_FREQ_HZ = SAMPLE_RATE*256   # Set the required master clock frequency in Hz (e.g., 44100)
#DUTY_CYCLE_50_PERCENT = 32768      # 50% duty cycle for 16-bit resolution (65535 / 2)
#mck_pwm = PWM(mck_pin, freq=MASTER_FREQ_HZ, duty_u16=DUTY_CYCLE_50_PERCENT)
#print(f"Master clock running on Pin {CLOCK_PIN} at {mck_pwm.freq()} Hz with 50% duty cycle.")

#### Globals
audio_out = None
done = False
paused = False
file = ""

#    wp = WavPlayer(id=I2S_ID,
#                   sck_pin=Pin(SCK_PIN),
#                   ws_pin=Pin(WS_PIN),
#                   sd_pin=Pin(SD_PIN),
#                   ibuf=BUFFER_LENGTH_IN_BYTES)
#    wp.play("YOUR_WAV_FILE.wav", loop=True)

def reset_globals():
    global done, paused, file
    done = False
    paused = False
    file = ""

def do_wp(filename):
    global done
    print("Wav player")
    wp.play(filename)
    
def send_audio(filename):
    #wp.play(filename, loop=False)
    done = False
    send_audio2(filename)
                
def send_audio2(filename):
    global sck_pin, ws_pin, sd_pin, SAMPLE_RATE, BUFFER_SIZE
    global done
    chunk = 0
    #pa_status = tca.write_port(7, 1)
    #print("Power Amplifier Status:",pa_status)
    
    audio_out = I2S(0,
                sck=sck_pin, ws=ws_pin, sd=sd_pin,
                mode=I2S.TX,
                bits=16,
                format=I2S.MONO,
                rate=SAMPLE_RATE,
                ibuf=BUFFER_SIZE
                )
    #codec.set_dac_volume(dac_volume)
    gc.collect()
    try:
        if filename == "":
            filename = "7thlife-7.wav"
        #file = "/sd/" + filename
        file = filename
        print("audio_out playing",file)
        num_read = 0
        with open(file, 'rb') as f:
            f.seek(44)  #skip WAV header
            sample = bytearray(BUFFER_SIZE)
            mv = memoryview(sample)
            while not done:
                chunk += 1
                num_read = f.readinto(mv)
                if num_read == 0:
                    break
                audio_out.write(mv[:num_read])
    except OSError as e:
        print(f"Error opening/reading file: {e}")
    finally:
        # Deinitialize I2S after playback is complete
        print("Blocks read:[{}]".format(chunk))
        audio_out.deinit()
        #pa_status = tca.write_port(7, 0)
        