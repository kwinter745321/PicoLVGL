# README - video 38 - MicroPython LVGL 9 - Let's use LVGL Canvas

# Topic 03 June 2025
This is video 38 on MicroPython and LVGL. This video presents an approach on how to draw on the LVGL Canvas widget.  We utilize the online LVGL Simulator to discuss the various details.  We use the simulator three times to add different features.  Finally we demonstrate the final version of the pick and place canvas program.

We use a Pico USB board with the Pico Display MB base board which is wired to ILI9341 Display.

In this video,
    • Present the LVGL Canvas drawing approach
    • Utilize the online LVGL simulator to:
	◦ Discuss the various draw and canvas statements
        ◦ Next we use a button to update the canvas
        ◦ Thirdly, we utilize the inherent-LVGL touch device to place drawing objects
    • Finally, we demonstrate the canvas program and review the code

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL

Repo:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video38

The Base Board is available for purchase:
https://www.tindie.com/products/aiy745321/pico-mp-display-board/


# Contents
This directory contains the files for this video.  

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop   | test_canvas_display.py     | The demonstration program.|
|           |                                  |                                            |
| Simulator |                                  |                                            |
|           | test_simple_simulator.py          |  The first code snippet. |
|           | test_update_simulator.py          |  The secondcode snippet. |
|           | test_indev_simulator.py          |  The third code snippet. |
|           |                      |                            |
| Firmware  |                      |                            |
| -APRIL2025  |                      |                            |
| -Pico_W   |firmware.uf2         |   PICO_W (RP2040) firmware  (MP1.20 and LVGL 9.3)  |
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

