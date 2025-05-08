# README - video 31 - MicroPython LVGL 9 - Let's use a larger display

29 April 2025

# Topic
This is video 31. The tenth video on MicroPython LVGL. This video researches larger displays (320x480) for the Pico using LVGL.  The wiring is described. Details on changes to the device drivers are explained. Finally, a demonstration program and two updated programs are demonstrated.  The code for the firmware, drivers and programs are at the GitHub site. 

The hardware is a 2.4 inch Ili9341 LCD Display with integrated Touch. The display board is wired to the Raspberry Pi Pico2 (RP2350) USB board and tested. The drivers should work on the Pico/PicoW, but had not been tested yet. Although, the test bed is using LVGL 9.3, the drivers should work as well on LVGL 9.1.

All three platforms contain the MicroPython 1.24 language and the LVGL 9.3 API Library and are available at the GitHub site.  The banners state MP 1.20

In this video,
- Research 480x320 displays
- Present my choice and discuss wiring
- Review driver changes
- Present a demonstration and two updated programs

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL

Repo:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video31

The Base Board is available for purchase:
https://www.tindie.com/products/aiy745321/pico-mp-display-board/


# Contents
This directory contains the files for video 31.  

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop   | test_matrix_display.py     | The demonstration program. It contains an example of 52 LVGL Button widgets. Its useful to verify touch on a larger display.|
|           | test_chart2_ulab.py | This is an update of test_chart_ulab.py and provides a bigger chart.  Also, the X Axis is configured better.|
|           | test_keyboard2_display.py  |   This is an update of test_keyboard_display.py.  The keyboard widget resized automatically to the new 480x320 display.  I aligned the Text Area to the bottom of the keyboard. |
|           |  test_xpt2046_b.py  |  Test program to verify Touch using updated driver.  |
|           |                      |                            |
| Firmware  |                      |                            |
| -FEB2025  |                      |                            |
| -Pico     |firmware.uf2         |   PICO (RP2040) firmware  (MP1.20 and LVGL 9.1)  |
| -Pico_W   |firmware.uf2         |   PICO_W (RP2040) firmware  (MP1.20 and LVGL 9.1)  |
| -Pico2    |firmware.uf2         |   PICO2 (RP2350) firmware  (MP1.20 and LVGL 9.3)  |
|           |                      |                            |
| -APRIL2025|                      |                            |
|           |                     |   The Banner states 1.20 but version info says 1.24.1      |
| -Pico     |firmware.uf2         |   PICO (RP2040) firmware  (MP1.24.1, LVGL 9.3 and ulab)  |
| -Pico_W   |firmware.uf2         |   PICO_W (RP2040) firmware  (MP1.24.1, LVGL 9.3 and ulab)  |
| -Pico2    |firmware.uf2         |   PICO2 (RP2350) firmware  (MP1.24.1, LVGL 9.3 and ulab)  |
|           |                      |                                 |
| Pico      |                      |                             |
|           |                      |                              |
|           |Driver files          | Only those drivers updated for the ST7796. |
|           |   display_driver.py  | display and touch setup for ILI9341 and ST7796 display. |
|           |   ili9xxx.py         | generic ili9341 and ST7796 driver  |
|           |   xpt2046_b.py       | touch driver updated for 320x480 display          |
|           |                      |                                             |
|           |                      |                                                 |

