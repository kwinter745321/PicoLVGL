# README - video 44 - MicroPython LVGL 9.4 - What are Subjects and Observers?

# Firmware
See the Firmware directory for Pico, PicoW, Pico2, and Pico2W versions.

# Topic 10 July 2025
This is video 44 on MicroPython and LVGL 9.4.0. This video introduces LVGL 9.4 and presents the Auxiliary Module called Observer. The new firmware includes the MicroPython 1.25.0 and the latest ulab.  An example of the Observer module is demonstrated on a standard Pico Test Rig using the ILI9341 display.

In this video, 
 - Discuss the latest LVGL 9.4 software and the firmware
 - Present the Test Rig configuration
 - Discuss the Observer module
- Demonstrate an observer example
 - Review the code

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PICOLVGL

Repo:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video44

The Base Board is available for purchase:
https://www.tindie.com/products/aiy745321/pico-mp-display-board/


# Contents
This directory contains the files for this video.  

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop   |                |                            |
|           | test_slider_display.py    | The demonstration program.|
|           |                      |                            |
|           |                      |                            |
| Firmware  |                      |                            |
| -July2025  |                      |                            |
| -Pico2W     |firmware.uf2         |   PICO (RP2040) firmware  (MP1.25.0 and LVGL 9.4)  |
| -Pico2W     |firmware.uf2         |   PICO_W (RP040) firmware  (MP1.25.0 and LVGL 9.4)  |
| -Pico2W     |firmware.uf2         |   PICO_W (RP2350) firmware  (MP1.25.0 and LVGL 9.4)  |
| -Pico2W     |firmware.uf2         |   PICO2_W (RP2350) firmware  (MP1.25.0 and LVGL 9.4)  |
|           |                      |                                 |
|           |                      |                                 |
| Pico      |                      |                             |
|           |                      |                              |
|           |Driver files          | Only those drivers updated for the ST7796. |
|           |   display_driver.py  | display and touch setup for ILI9341 and ST7796 display. |
|           |   fs_driver.py       | file system driver.           |
|           |   ili9xxx.py         | generic ili9341 and ST7796 driver.  |
|           |   lv_utils.py        |  LVGL utility.                                         |
|           |   sdcard_driver.py   | sdcard application driver.          |
|           |   sdcard2.py         | sdcard driver.        |
|           |   secret.py          | Used by network to connect to wifi.      |
|           |   st7xx.py           | generic driver utilized by both displays.  |
|           |   xpt2046.py       | touch driver updated for 320x480 display.          |
|           |                      |                                             |
|           |                      |                                                 |


