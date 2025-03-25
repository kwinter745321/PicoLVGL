# README - video 25 LVGL 9 - Scale Widget

21 March 2025

This is video 25.  The fourth video on MicroPython LVGL. This video demonstrates the Scale widget with three code examples.  Additionally the LVGL MicroPython Simulator is introduced.

The hardware is a Ili9341 LCD Display with integrated Touch and SD Card. The display board is wired to the Raspberry Pi Pico USB board and tested.

In this video,
- Review three code examples: Simple Scale, Bar with Scale and a Round Scale.
- Introduce LVGL MicroPython Simulator.
- Discuss Scale LVGL Parts.  

The hardware is a Ili9341 LCD Display with integrated Touch and SD Card.  The display board is wired to the Raspberry Pi Pico-W USB board and tested.  

Note:  The RPI Pico USB board is used in this video to ensure the display of the Round Scale.

Simulator:
https://sim.lvgl.io/v9.0/micropython/ports/javascript/index.html 

# Contents
This directory contains the files for video 25.  Each program displays the Scales in their default black color on a white background.  The various Scale Parts can be changed to a color-style if you uncomment a specific line. 

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop | test_scale_display.py     | First test. Simple Scale widget. |
|         | test_scalebar_display.py | Second test. Scale aligned to a Bar widget. |
|         | test_scalecircle_display.py| Third test. Round widget. |
|         |                      |                            |
| Firmware|                      |                            |
| -Pico   |firmware.uf2         |   PICO (RP2040) firmware    |
| -Pico_W |firmware.uf2         |   PICO_W (RP2040) firmware    |
|         |                      |                                 |
| Pico    |                      |                             |
|         |   display_driver.py  | Contains display and touch setup. A Reset button is provided to hard reset the Pico as needed. |
|         |   ili9xxx.py         | generic ili9341 driver  |
|         |   lv_utils.py        | lvgl utilities   |
|         |   st77xx.py          | generic display driver |
|         |   xpt2046.py         | touch driver           |