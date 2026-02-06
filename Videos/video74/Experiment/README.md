# README.md


06 February 2026

# Scope
Side test on Pico2W (RP2350) to see if we can run WIFI after starting LVGL code.
This test places the LVGL code on Core1 and leaves everything else on core0. Of course, you
will need to edit the file to use your SSID and Password

Be aware to ensure its not a memory issue the ST77xx.py driver
was modified to use a much smaller framebuffer.

The program still hangs when do_connect() runs.
So there is still a conflict between WIFI and the SPI display when it uses LVGL

# Files

 - test_coreone_display.py 
 - test_coreone_withlock_display.py    (same thing but uses a thread lock)
 - st77xx.py                           modified display driver with smaller framebuffer
