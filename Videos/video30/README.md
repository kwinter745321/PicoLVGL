# README - video 30 - MicroPython LVGL 9 - Introduction to ulab

22 April 2025

# Topic
This is video 30. The ninth video on MicroPython LVGL. This video introduces ulab and demonstrates a sampling of methods and functions via a JupyterLab Sheet.  Additionally, a new firmware and the ulab build options are described.  Finally, a LVGL Chart Wizard program is presented along with a review of the code. 

The hardware is a 2.4 inch Ili9341 LCD Display with integrated Touch. The display board is wired to the Raspberry Pi Pico USB board and tested. The platform is a standard Pico (RP2040).  I verified the code works the same way on a Pico2 USB board.  

Some of the Chart function names changed between LVGL 9.1 and LVGL 9.3.   So, the code example includes the LVGL 9.1 statements (commented out).   By using the LVGL 9.1 statements, I was verify the program in the online simulator which is using LVGL 9.0.  Of course it does not have ulab so I used reasonable values.

If you update to the latest firmware, please backup any Pico files.  I noticed that my RP2040 Pico-W
did not keep the files.  Whereas RP2040 happily kept everything.

All three platforms contain the MicroPython language and the LVGL 9.3 API Library and are available at the GitHub site.

In this video,
    • We research ulab
    • We demonstrate ulab capabilities using a Jupyter notebook
    • We discuss the specific firmware available at my GitHub site
    • We review the program code of a chart widget and using a couple of lab functions

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL

Repo:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video30

The Base Board is available for purchase:
https://www.tindie.com/products/aiy745321/pico-mp-display-board/


# Contents
This directory contains the files for video 30.  

| Folders | File list | Explanation |
|---------|-----------|-------------|
| Desktop   | test_chart_ulab.py     | The demonstration program. It contains an example of a LVGL Chart widget and an example using some ulab functions. |
|           | ulab_info.py | The information program mentioned in the ulab online documentation. |
|           |                      |                            |
|           |                      |                            |
| Notebook        | ulab_test.ipynb | A JupyterLab notebook  with ulab functions that were demonstrated in the video.
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
|           | Air.csv              |  Ten values that are comma separated in a text file.  The single set of data was extracted from the top of the original file.                            |
|           |                      |                              |
|           |Driver files          | Should already be on your Pico from previous videos. |
|           |   display_driver.py  | display and touch setup for ILI9341 display. |
|           |   fs_driver.py         | generic LVGL file system driver  |
|           |   ili9xxx.py         | generic ili9341 driver  |
|           |   lv_utils.py        | lvgl utilities   |
|           |   sdcard.py          | generic MicroPython sdcard driver   |
|           |   sdcard2.py         | MicroPython sdcard driver modified for my standard Pico  |
|           |   st77xx.py          | generic display driver |
|           |   xpt2046.py         | touch driver           |
|           |                      |                                             |
|           |                      |                                                 |

