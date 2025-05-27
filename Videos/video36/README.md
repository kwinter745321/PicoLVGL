# README - video 36 - MicroPython LVGL 9 - Integrating buttons to LVGL

# Topic 27 May 2025
This is video 36 on MicroPython and LVGL. This video researches and discusses the integration of hardware pushbuttons with LVGL. RPI Pico.  Two different integration approaches are demonstrated: "Encoder" and "Button".  The program code is reviewed. 

We used a Pico-W USB board with a PICO Breadboard Kit (that has four pushbuttons.)  Though, the programs could just as easily be run on ESP32.

In this video,
    • Research the LVGL documentation
    • Discuss INDEV features
    • Demonstrate the programs
    • Review program code

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL

Repo:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video36

The Base Board is available for purchase:
https://www.tindie.com/products/aiy745321/pico-mp-display-board/


# Contents
This directory contains the files for this video.  

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop   | test_buttonslider_display.py     | The simulate encoder demonstration program.|
|           | test_areabtn_display.py          |  The simulate button demonstration program. |
|           |                      |                            |
| Firmware  |                      |                            |
| -APRIL2025  |                      |                            |
| -Pico_W   |firmware.uf2         |   PICO_W (RP2040) firmware  (MP1.20 and LVGL 9.3)  |
|           |                      |                                 |
|           |                      |                                 |
| Pico      |                      |                             |
|           |                      |                              |
|           |Driver files          |  |
|           |   display_driver.py  | display and touch setup for ILI9341 or ST7796 display. |
|           |   ili9xxx.py         | generic ILI9341 and ST7796 driver  |
|           |   lv_utils.py        | Utility routines for LVGL |
|           |   st7xx.py           | generic driver utilized by both displays.  It's class has the base routines.                                            |
|           |   xpt2046.py       | touch driver updated for 240x320 or 320x480 displays         |
|           |                      |                                             |
|           |                      |                                                 |

