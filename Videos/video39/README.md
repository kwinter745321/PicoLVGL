# README - video 39 - MicroPython LVGL 9 - Let's start to use LVGL Flex

# Topic 11 June 2025
This is video 39 on MicroPython and LVGL. This video presents an approach on using the LVGL Flex feature.  We utilize the new Pico2W firmware. We discuss simple features of Flex and then demonstrate using two programs.  We briefly review the code.

We use a Pico2W USB board with the Pico Display MB base board which is wired to ILI9341 Display.

In this video,
- Discuss the new Pico2W firmware
- Research the LVGL Documentation
- Finally, we demonstrate two example programs and review their code

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL

Repo:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video39

The Base Board is available for purchase:
https://www.tindie.com/products/aiy745321/pico-mp-display-board/


# Contents
This directory contains the files for this video.  

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop   | test_flex_display.py     | The first demonstration program.|
|           | test_flex2_display.py    | The second demonstration program.|
|           |                      |                            |
| Firmware  |                      |                            |
| -June2025  |                      |                            |
| -Pico2_W   |firmware.uf2         |   PICO2_W (RP2350) firmware  (MP1.25.0 and LVGL 9.3)  |
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

