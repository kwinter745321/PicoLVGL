# README - video 23 LVGL 9 - Button Events

05 March 2025

This is video 23.  The second video on MicroPython LVGL. This video demonstrates three code examples of button events. The hardware is a Ili9341 LCD Display with integrated Touch and SD Card.  The display board is wired to the Raspberry Pi Pico-W USB board and tested.  

# Contents
This directory contains the files for video 23.

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop | test_button_display.py     | First test. Simple button event. |
|         | test_two-button_display.py | Second test. Single event-two buttons. |
|         | test_button-data_display.py| Third test. Simple button with data passed to event. |
|         |                      |                            |
| Firmware|                      |                            |
| -Pico   |firmware.uf2         |   PICO (RP2040) firmware    |
| -Pico_W |firmware.uf2         |   PICO_W (RP2040) firmware    |
|         |                      |                                 |
| Pico    |                      |                             |
|         |   display_driver.py  | contains display and touch setup  |
|         |   ili9xxx.py         | generic ili9341 driver  |
|         |   lv_utils.py        |  lvgl utilities   |
|         |   st77xx.py          | generic display driver |
|         |   xpt2046.py         | touch driver           |