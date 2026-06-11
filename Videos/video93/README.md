# README.md - video93

11 June 2026

# Scope
This is video 93 on a MicroPython LVGL embedded solution. We introduce the Display Driver file that integrates the other drivers for the Display and touchscreen.  The display_driver.py file is where you specify the actual pins used in your project.  The Test Rig is using a ST7796 Display with XPT2046 touchscreen and the microcontroller is a RPI Pico 2W microcontroller (MCU).  

We provide the latest firmware although the program should operate on any (2025-2026) firmware specific to your model.  The drivers work the same way on other microcontrollers (like the ESP32. ) 

You can fetch the test program from our PicoLVGL GitHub site. 

In this video, 
 - Look at the ST7796 Display.
 - Review the Display Driver file to setup display.
 - Demonstrate a simple application using a button and slider.

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video93

# Files

 - Desktop
   - test_button3_display.py

 - Firmware
   - copy of the RPI Pico2W firmware

- Flash
   - display_driver.py
   - various other driver files used by display_driver

