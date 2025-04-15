# README - video 26 - MicroPython LVGL 9 - Keyboard Widget (Best display)

28 March 2025

This is video 26. The fifth video on MicroPython LVGL. This video demonstrates the Keyboard widget. We test three different sized ILI9341 displays.  As a result, we re-visit the touch interface. Finally, we moved the code to a new Repository in GitHub.

The hardware is a 2.8 inch Ili9341 LCD Display with integrated Touch and SD Card. The display board is wired to the Raspberry Pi Pico2 USB board and tested.
Al three firmware contain the MicroPython language and the LVGL API Library and are available at the GitHub site.

In this video,
    • We demo’ed the Keyboard widget.
    • We discussed three ILI9341 displays 
    • We reviewed the driver code fix to accommodate the 2.8 and 3.2 inch displays.
    • We reviewed the Keyboard widget code  

# Contents
This directory contains the files for video 26.  Each program displays the Scales in their default black color on a white background.  The various Scale Parts can be changed to a color-style if you uncomment a specific line. 

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop | test_keyboard_display.py     | Keyboard widget. |
|         | xpt2046-test.py | I used this to re-test touch. |
|         | test_scalecircle_display.py| Third test. Round widget. |
|         |                      |                            |
| Firmware|                      |                            |
| -Pico   |firmware.uf2         |   PICO (RP2040) firmware  (LVGL 9.1)  |
| -Pico_W |firmware.uf2         |   PICO_W (RP2040) firmware  (LVGL 9.1)  |
| -Pico2  |firmware.uf2         |   PICO2 (RP2350) firmware  (LVGL 9.3)  |
|         |                      |                                 |
| Pico    |                      |                             |
|         |   display_driver.py  | Contains display and touch setup. Updated for larger 2.8 or 3.2 inch ILI9341 displays. |
|         |   ili9xxx.py         | generic ili9341 driver  |
|         |   lv_utils.py        | lvgl utilities   |
|         |   st77xx.py          | generic display driver |
|         |   xpt2046.py         | touch driver           |