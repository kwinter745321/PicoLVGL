# README - video 41 - MicroPython LVGL 9 - Let's add Capacitive Touch

# Topic 25 June 2025
This is video 41 on MicroPython and LVGL. This video researches the generic FT6x36 (I2C) Touch driver and explains how it was re-written for the Hosyond Touch controller. We utilize the standard RPI Pico USB Board and interface it to the Hosyond (ST7796S) display

In this video, 
    • Discuss the generic FT6x36 driver available at the GitHub site
    • Discuss the Hosyond display and its CTP touch module
    • Present the CTP Interface and the physical pinout
    • Demonstrate the new touch driver using our standard programs
    • Finally, discuss the touch driver and updated display_driver code

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL

Repo:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video41

The Base Board is available for purchase:
https://www.tindie.com/products/aiy745321/pico-mp-display-board/


# Contents
This directory contains the files for this video.  

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop   | test_button3_display.py     | The first demonstration program.|
|           | test_matrix3_display.py    | The second demonstration program.|
|           | test_keyboard3_display.py    | The third demonstration program.|
|           | test_scan3_i2c.py    | The third demonstration program.|
|           |                      |                            |
| Firmware  |                      |                            |
| -April2025  |                      |                            |
| -Pico     |firmware.uf2         |   PICO (RP2040) firmware  (MP1.24.1 and LVGL 9.3)  |
|           |                      |                                 |
|           |                      |                                 |
| Pico      |                      |                             |
|           |                      |                              |
|           |Driver files          |  |
|           |   display_driver.py  | display and touch setup for ILI9341 or ST7796 display. |                                        |
|           |   ctp_ft6x36.py       | touch driver updated for Hosyond ST7796S display         |
|           |                      |                                             |
|           |                      |                                                 |

