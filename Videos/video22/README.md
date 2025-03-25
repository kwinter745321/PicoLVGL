# README   - video22 - Raspberry Pi Pico - Get Started with MicroPython LVGL v9


# Overview
26 February 2025


This is video 22.  This video discusses a MicroPython LVGL Graphics Library for the Raspberry Pi Pico (RP2040).
The hardware is a Ili9341 LCD Display with integrated Touch and SD Card.  The display board is wired to the Raspberry Pi Pico USB board and tested.  We show a demonstration LVGL v9 program (written in MicroPython) and then review the code. 

# Contents
This directory contains the files for video 22.

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop | ili9xxx-test.py | tests the display |
|         | test_ili9xxx_demo.py | Demonstration program |
|         | xpt2046-test.py      | tests the touch controller |
|         |                      |                            |
| Firmware     | firmware.uf2    |   drag this file to the Pico  |
|         |                      |                                 |
| Pico    |                      |                             |
|         |   ili9xxx.py         | generic ili9341 driver  |
|         |   lv_utils.py        |  lvgl utilities   |
|         |   st77xx.py          | generic display driver |
|         |   xpt2046.py         | touch driver           |


# Update 28 Febrary 2025

Included the Pico_W (RP2040) firmware.


