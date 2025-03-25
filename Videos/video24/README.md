# README - video 24 LVGL 9 - List

12 March 2025

This is video 24.  The third video on MicroPython LVGL. This video demonstrates three code examples of widgets that use List: List, Roller, and Dropdown. Additionally the MessageBox and Spinner widgets are introduced. Finally, some discussion is provided on applying Styles to various Parts of a widget.

The hardware is a Ili9341 LCD Display with integrated Touch and SD Card.  The display board is wired to the Raspberry Pi Pico-W USB board and tested.  

# Contents
This directory contains the files for video 24.

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop | test_list_display.py     | First test. Simple list. |
|         | test_roller_display.py | Second test. Roller example widget uses a list. |
|         | test_dropdown_display.py| Third test. Dropdown example widget uses a list. |
|         |                      |                            |
| Firmware|                      |                            |
| -Pico   |firmware.uf2         |   PICO (RP2040) firmware    |
| -Pico_W |firmware.uf2         |   PICO_W (RP2040) firmware    |
|         |                      |                                 |
| Pico    |                      |                             |
|         |   display_driver.py  | Contains display and touch setup. Updated with MessageBox  |
|         |   ili9xxx.py         | generic ili9341 driver  |
|         |   lv_utils.py        |  lvgl utilities   |
|         |   st77xx.py          | generic display driver |
|         |   xpt2046.py         | touch driver           |