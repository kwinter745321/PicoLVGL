# README - video 32 - MicroPython LVGL 9 - Let's improve the display driver for orientation

# Topic 08 May 2025
This is video 32 on MicroPython. This video discusses a suggested change to the display driver to manage orientation modes.  The orientations are Portrait, Landscape, Inverted Portrait, and Inverted Landscape. Details on changes to the device drivers are explained. Finally, the keyboard program is demonstrated on the 4 inch ST7796 and the 2.8 inch ILI9341 displays. The code also includes transform calculations for the 2.4 inch ILI9341 display. The code for the firmware, drivers and programs are at the GitHub site. 

The hardware is the Pico MP Display Base Board, the Raspberry Pi Pico (RP2040) USB board and three displays. The drivers should work on the Pico2/PicoW. The April Firmware LVGL 9.3 is utilized. All three platforms contain the MicroPython 1.24 language and the LVGL 9.3 API Library and are available at the GitHub site.  The banners state MP 1.20

In this video,
- Discuss improvements needed and seeking your feedback via Comments
- Demonstrate Landscape and Portrait mode on the 4.0 inch ST7796 display
- We review the driver changes to manage the orientations
- Demonstrate all four orientations on the 2.8 inch ILI9341 display

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL

Repo:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video32

The Base Board is available for purchase:
https://www.tindie.com/products/aiy745321/pico-mp-display-board/


# Contents
This directory contains the files for this video.  

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop   | test_keyboard2_display.py     | The demonstration program. It reconfigures itself for the various orientations.|
|           |                      |                            |
|           |                      |                            |
| Firmware  |                      |                            |
| -APRIL2025|                      |                            |
|           |                     |   The Banner states 1.20 but version info says 1.24.1      |
| -Pico     |firmware.uf2         |   PICO (RP2040) firmware  (MP1.24.1, LVGL 9.3 and ulab)  |
| -Pico_W   |firmware.uf2         |   PICO_W (RP2040) firmware  (MP1.24.1, LVGL 9.3 and ulab)  |
| -Pico2    |firmware.uf2         |   PICO2 (RP2350) firmware  (MP1.24.1, LVGL 9.3 and ulab)  |
|           |                      |                                 |
|           |                      |                                 |
| Pico      |                      |                             |
|           |                      |                              |
|           |Driver files          | Only those drivers updated for the ST7796. |
|           |   display_driver.py  | display and touch setup for ILI9341 and ST7796 display. |
|           |   ili9xxx.py         | generic ili9341 and ST7796 driver  |
|           |   st7xx.py           | generic driver utilized by both displays.  It's class has the base routines.                                            |
|           |   xpt2046.py       | touch driver updated for 320x480 display          |
|           |                      |                                             |
|           |                      |                                                 |

