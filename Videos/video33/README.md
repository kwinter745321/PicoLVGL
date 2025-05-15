# README - video 33 - MicroPython LVGL 9 - An interesting program

# Topic 15 May 2025
This is video 33 on MicroPython and LVGL. The video has a goal to find an interesting LVGL MicroPython.  The ideal program is presented. Having found an example; some of its concepts such as Networking and Asyncio are briefly discussed. Finally, the full program is reviewed.  The code for the firmware, drivers and programs are at the GitHub site. 

The hardware is the Base Board, the Raspberry Pi Pico (RP2040) USB board and the ILI9341 displays. The code is written for LVGL 9.1 graphics available on the Feb 2025 Firmware which uses MicroPython 1.20

In this video,
    • Present an example LVGL MicroPython program
    • Briefly discuss networking and asyncio on the Pico
    • Demonstrate the program
    • Review the program code


The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL

Repo:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video33

The Base Board is available for purchase:
https://www.tindie.com/products/aiy745321/pico-mp-display-board/


# Contents
This directory contains the files for this video.  

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop   | temp_humidity_display.py     | The demonstration program. It must be install on PicoW with the Feb 2025 firmware.|
|           |                      |                            |
|           |                      |                            |
| Firmware  |                      |                            |
| -FEB2025  |                      |                            |
| -Pico_W   |firmware.uf2         |   PICO_W (RP2040) firmware  (MP1.20 and LVGL 9.1)  |
|           |                      |                                 |
|           |                      |                                 |
| Pico      |                      |                             |
|           |                      |                              |
|           |Driver files          |  |
|           |   display_driver.py  | display and touch setup for ILI9341 or ST7796 display. |
|           |   ili9xxx.py         | generic ILI9341 and ST7796 driver  |
|           |   lv_utils.py        | Utility routines for LVGL |
|           |   secret.py          | Put your wireless service-name and password here.
|           |   st7xx.py           | generic driver utilized by both displays.  It's class has the base routines.                                            |
|           |   xpt2046.py       | touch driver updated for 240x320 or 320x480 displays         |
|           |                      |                                             |
|           |                      |                                                 |

