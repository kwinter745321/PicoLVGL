# README.md - Video 62

04 November 2025

# Scope

This is video 62 on embedded solutions. In this video, we discuss the ST7735 technology, we update the driver code, and we begin to use it. We demonstrate three simple programs.

In this video, 
 - Demonstrate our test Hello and Color Dots programs on ST7735 displays.
 - Present three display samples and test rig wiring.
 - Discuss the driver update.
 - Walk through the driver code update.

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video62


# Files

Desktop

 - test_hello_display.py                    Main test program.  Button should be the color blue.
 - test_colordots_st7735-128x129.py         Display a number of round objects in random colors (less on column.)
 - test_colordots_st7735.py                 Display a number of round objects in random colors.

Flash-ESP32

 - display_driver.py                                Contains display and touch driver objects (using the normal esp32 pinouts).
 - Others should be the same as the pico files      See below.

Flash-pico

 - display_driver.py                                Contains display and touch driver objects (using the various pico pinouts).
 - ili9xxx.py                                       ILI9xxx series drivers including ILI9341, ST7796, and GCA901.
 - lv_utils.py                                      LV Utility.
 - st77xx.py                                        Contains the base class for displays and the newly updated ST7735 class.
 - xpt2046.py                                       Touchscreen driver (not used in this video.)

 