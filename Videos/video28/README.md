# README - video 28 - MicroPython LVGL 9 - It's easy to add fonts

08 April 2025

# Topic
This is video 28. The seventh video on MicroPython LVGL. This video shows how easy it is to acquire and add external fonts to our LVGL MicroPython programs.  We continue to use the SDCard.  Finally, we provide and review a code example to display labels with different fonts.

The hardware is a 2.4 inch Ili9341 LCD Display with integrated Touch and SD Card. The display board is wired to the Raspberry Pi Pico2 USB board and tested.
All three firmware contain the MicroPython language and the LVGL API Library and are available at the GitHub site.

# In this video
    • Demonstrate external fonts
    • Discuss LVGL embedded fonts 
    • Acquire fonts
    • Convert fonts to bin files
    • Review test font code

# Contents
This directory contains the files for video 28.  

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop | test_font-demo_fs.py     | The demo program to display three interesting fonts. |
|         | test_font_fs.py | The test program reviewed with three fonts. |
|         |                      |                            |
| Firmware|                      |                            |
| -Pico   |firmware.uf2         |   PICO (RP2040) firmware  (LVGL 9.1)  |
| -Pico_W |firmware.uf2         |   PICO_W (RP2040) firmware  (LVGL 9.1)  |
| -Pico2  |firmware.uf2         |   PICO2 (RP2350) firmware  (LVGL 9.3)  |
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
| font    |                      |  font files                       |
|         |  alexbrush-reg-xx-2.bin  | alexbrush xx=24,28,30,36 sizes      |
|         |  chunkfive-reg-xx-2.bin  | chunkfive xx=24 size      |
|         |  montserrat-med-xx-2.bin  | montserrat medium xx=12,14,16...48 sizes      |
|         |  roboto-reg-xx-2.bin      | roboto xx=24 size      |

14 April 2025

I replaced the file display_driver.py to fix lines 78-80 that should not have an indent.

