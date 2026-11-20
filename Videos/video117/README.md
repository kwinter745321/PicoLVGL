# README.md -  video117 

19 November 2026

# Scope
This is video 117 on an MicroPython/LVGL embedded solution. In today’s video we look at a program that demonstrates fast graphics. This is a Ball game written in 1.29 MicroPython and the 9.6 LVGL release. Our TestRig is a Raspberry Pi Pico2W (RPI_PICO2_W) with an ILI9341 Display.  We also verified a ST7796 display (not shown) that only requires the screen resolution.

In this video, 
 - Demonstrate the Ball Game program.
 - Briefly describe the design.
 - Briefly describe the wiring (since its similiar to a previous video).

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video117

# Files

 - Firmware

    - all four generic RPI Pico firmware with MicroPython 1.29, LVGL 9.6.0, and ulab

 - Desktop

     - ball_game_dd.py
     - test_mpu9250.py

 - Flash
     - dd.py (we used this one)
     - display_driver.py (not updated)
     - ili9xxx.py  
     - st77xx.py  
     - xpt2046.py
     - Tuupola's MPU9250 driver
         - mpu9250.py
         - mpu6500.py
         - ak8963.py