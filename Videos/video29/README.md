# README - video 29 - MicroPython LVGL 9 - Will a LVGL Encoder work?

15 April 2025

# Topic
This is video 29. The eighth video on MicroPython LVGL. This video describes the LVGL Encoder operating logic, researches rotary encoders, discusses wiring a rotary encoder to the Pico and reviews several code examples. 

The hardware is a 2.4 inch Ili9341 LCD Display with integrated Touch and a KY-040 Rotary Encoder. The display board is wired to the Raspberry Pi Pico USB board and tested. So the platform was switched to a standard Pico (RP2040).  This is to try out an update to LVGL 9.3 (MicroPython is version 1.20 )  The code will work as is on LVGL 9.1.  

Note: the Pico2, at the moment, has an issue with the LVGL Encoder (INDEV) setup and hangs.  The Pico2 does work with the Rotary Encoder driver, so you can directly manage the device. 

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
This directory contains the files for video 29.  

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop | test_rotary_driver.py     | Test your Rotary Encoder with the new driver files. |
|         | test_group_encoder.py | The demonstration program. It contains an example of multiple widgets in an Encoder group. |
|         | test_slider_encoder.py | A test program with a single widget and example of disabling the Nav mode.
|         |                      |                            |
| Firmware|                      |                            |
| -Pico   |firmware.uf2         |   PICO (RP2040) firmware  (LVGL 9.1)  |
| -Pico_W |firmware.uf2         |   PICO_W (RP2040) firmware  (LVGL 9.1)  |
| -Pico2  |firmware.uf2         |   PICO2 (RP2350) firmware  (LVGL 9.3)  |
|         |                      |                            |
| -Pico   |firmware.uf2         |   PICO (RP2040) firmware  (LVGL 9.3)  |
| -Pico_W |firmware.uf2         |   PICO_W (RP2040) firmware  (LVGL 9.3)  |
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
| STL     |   RotaryPanel.stl    | 3D-printable plate to hold the Rotary Encoder.  |
|         |                      |                                                 |


