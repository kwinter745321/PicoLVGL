# README.md - Video76

13 February 2026

# Scope
This is video 76 on a MicroPython/LVGL embedded solution. In this video, we look at an integrated ST7789 display and its components.  Also we provide updated Raspberry Pi Pico2 firmware for the device since it has a 16MB Flash drive.  This device has audio, sdcard, RTC, and an IMU sensor.  We demonstrate the working drivers with two simple LVGL programs.  

You can fetch the firmware and programs from our GitHub site, and begin using them immediately.  

In this video, 
 - Demonstrate two MicroPython LVGL programs .
 - Review the device capabilities.
 - Discuss the display, audio, and sdcard configuration.

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video76

Background music is 7th Life by Adam MacDougall which is You Tube Licensed as not requiring an attribution.

# Files

 - Desktop
    - check_flash_size.py      In case you want to verify the flash.
    - test_matrix2_display.py  Displays color buttons with locations
    - test_audio2_display.py  Similar to video75 but modified for the smaller display.  Also it tests the sdcard.

 - Firmware

    - firmware.uf2    This is specific to the rp2350-Touch-lLCD-2.8 device (in that it expects the 16MB external flash chip.)

 - Flash
     - Various driver files.  Note audio2_driver.py was modified from that used in video 75.

 - Music
    - Snippets from the 7th Life mp3 exported at sample rate 44100 MHz 16bit Mono (wav) files.  PLace with the drivers on the flash
