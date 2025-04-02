# README - video 27 - MicroPython LVGL 9 - Let's use the SD Card

02 April 2025

# Topic
This is video 27. The sixth video on MicroPython LVGL. This video explains how to interface to the ILI9341 Display's SD Card. We explain the wiring and the drivers.  We show how to test the SDCard and the benefit of using Thonny.  Finally, we provide and review two code examples to display and manipulate the images.

The hardware is a 2.4 inch Ili9341 LCD Display with integrated Touch and SD Card. The display board is wired to the Raspberry Pi Pico2 USB board and tested.
Al three firmware contain the MicroPython language and the LVGL API Library and are available at the GitHub site.

A 4-pin male header must be attached to the ILI9341 Display board.  This effort requires some simple soldering by the builder.
Then standard female DuPont wires can interconnect the pins of the header and the Pico.

# In this video
    • We demonstrate a program that displays an external image.
    • We discuss the SD Card and showed how to wire the interface
    • We explain the SD Card format and test the SD Card interface
    • We explain how to resize images to be displayed by the Pico
    • We review two code examples to display the image. 
	  - First using a traditional MicroPython approach, and 
	  - the second example utilizes the LVGL filesystem.

# Contents
This directory contains the files for video 25.  Each program displays the Scales in their default black color on a white background.  The various Scale Parts can be changed to a color-style if you uncomment a specific line. 

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop | test_sdcard_spi.py     | Tests just the SD Card interface to the Pico. |
|         | test_image_sdcard.py | The demo and program to display two images. |
|         | test_image_fs.py| The program to display the two images using fs_driver. |
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
| images  |                      |  image and test files                       |
|                |  test.txt                  | a simple test text file        |
|                |  dir1/                    |                                 |
|                |  cog1.png                 |  image of a cog                 |
|                |  R5.png                   |  image of my Raspberry PI 5     |

