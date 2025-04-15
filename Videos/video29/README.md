# README - video 29 - MicroPython LVGL 9 - Will a LVGL Encoder work?

15 April 2025

# Topic
This is video 29. The eighth video on MicroPython LVGL. This video describes the LVGL Encoder operating logic, researches rotary encoders, discusses wiring a rotary encoder to the Pico and reviews several code examples. 

The hardware is a 2.4 inch Ili9341 LCD Display with integrated Touch and a KY-040 Rotary Encoder. The display board is wired to the Raspberry Pi Pico USB board and tested. So the platform was switched to a standard Pico (RP2040).  This is to try out an update to LVGL 9.3 (MicroPython is version 1.20 )  The code will work as is on LVGL 9.1.

If you update to the latest firmware, please backup any Pico files.  I noticed that my RP2040 Pico-W
did not keep the files.  Whereas RP2040 happily kept everything.

All three platforms contain the MicroPython language and the LVGL 9.3 API Library and are available at the GitHub site.

# In this video,
    • An explanation of the LVGL Rotary Encoder logic
    • Rotary encoder hardware
    • Wire & Mount a rotary encoder
    • Rotary encoder driver files
    • Testing our rotary encoder
    • Review of test LVGL example code

# Contents
This directory contains the files for video 29.  Each program displays the Scales in their default black color on a white background.  The various Scale Parts can be changed to a color-style if you uncomment a specific line. 

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop | test_abc.py     | The demo program to abc. |
|         | test_abc.py | The test program reviewed abc. |
|         |                      |                            |
| Firmware|                      |                            |
| -Pico   |firmware.uf2         |   PICO (RP2040) firmware  (LVGL 9.1)  |
| -Pico_W |firmware.uf2         |   PICO_W (RP2040) firmware  (LVGL 9.1)  |
| -Pico2  |firmware.uf2         |   PICO2 (RP2350) firmware  (LVGL 9.3)  |
|         |                      |                                 |
| Pico    |                      |                             |
|         |   display_driver.py  | display and touch setup for ILI9341 display. |
|         |   fs_driver.py         | generic LVGL file system driver  |
|         |   ili9xxx.py         | generic ili9341 driver  |
|         |   lv_utils.py        | lvgl utilities   |
|         |   sdcard.py          | generic MicroPython sdcard driver   |
|         |   sdcard2.py         | MicroPython sdcard driver modified for my standard Pico  |
|         |   st77xx.py          | generic display driver |
|         |   xpt2046.py         | touch driver           |
|         |                      |                                             |


