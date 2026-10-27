# README.md - Video113

27 October 2026

# Scope
This is video 113 on an MicroPython/LVGL embedded solution. In today’s video we look at the recently released LVGL 9.6.0.  In this video, we discuss the impact of the release.  We demonstrate our typical test programs and a new program made better by the 9.6 release. Our TestRig is a Raspberry Pi Pico2W (RPI_PICO2_W) with a ST7796 Display.  We also briefly connect ILI9341 and ST7735 displays.


In this video, 
    • Demonstrate the button3/matrix3 test programs, and a new program made better by LVGL 9.6.
    • Briefly describe the impact (in terms of memory needs).
    • Briefly describe the firmware (in terms of Flash storage that remains).
    • Demonstrate the LVGL program showing the ST7796, ILI9341, and ST7735 using the update display driver (dd.py).

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video113

# Files

 - Firmware

    - all four generic RPI Pico firmware with MicroPython 1.29, LVGL 9.6.0, and ulab

 - Desktop

     - test_button3_display.py
     - test_matrix3_display.py
     - test_split_display.py
     - test_heap_afterimport.py

 - Flash
     - dd.py (improved version of display_driver.py)
     - display_driver.py
     - ili9xxx.py  (updated)
     - st77xx.py  (updated)
     - xpt2046.py