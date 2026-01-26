# README.md - Video 74

26 January 2026

# Scope
This is video 74 on a MicroPython/LVGL embedded solution. In this video, we look at a variety of ST7789 displays and how to update the driver.  Also we provide updated Raspberry Pi Pico firmware.  We demonstrate the working driver on three test rigs with two simple LVGL programs.  

You can fetch the firmware and programs from our GitHub site, and begin using them immediately.  

In this video, 
 - Demonstrate two MicroPython LVGL programs on three test rigs.
 - Present three ST7789 displays in different resolutions.
 - Discuss our ST7789 research.
 - Explain how we added a new display model to the ST7789 driver.
 - (Briefly) Walk through the program code.

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video74

# Files

- Desktop
  - test_hello_display.py
  - test_colordots_display.py

  - Make sure to load the Flash driver files onto the Pico using a tool like Thonny

- Firmware

  - Various RPI PICO firmware built in January 2026

- Flash

  - display_driver.py  (Generally you edit this file to setup the display type and orientation (rot) )
  - ili9xxx.py
  - lv_utils.py
  - st77xx.py
  - xpt2046.py