# README - Video 104

28 August 2026

# Scope
This is video 104 on a MicroPython LVGL embedded solution. The MicroPython v1.29.0 release (24 August 2026) introduces significant hardware expansions, including support for new boards. As such, we built a new set of firmware for the RPI PICO dev boards. We discuss details of the Release. And, of course we provide the firmware at our GitHub site.  This firmware also integrates LVGL 9.5.0 and ulab 6.12 for enhanced graphics capabilities.  We were careful to reduce the Flash partition to 512K (256K for RPI_PICO_W).  We demonstrate our test LVGL programs using the firmware on a RPI_PICO2_W with a ST7796 display.

In this video:
- We discuss the highlights of the release.
- We explain the increased code size and our firmware build
- Demonstrate our test LVGL programs 

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video104

# Files

 - Firmware

    - RPI_PICO
    - RPI_PICO_W
    - RPI_PICO2
    - RPI_PICO2_W

 - Desktop
   - test_button3_display.py
   - test_matrix3_display.py

 - Flash

   - display_driver.py  - Edit to place your choice of display and touch and their pin assignments
   - various drivers
   