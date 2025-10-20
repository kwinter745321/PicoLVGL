# README - Video 60

19 October 2025

# Scope
This is video 60 on embedded solutions. In this video, we discuss the GC9A01, we add driver code, and we begin to use it. We demonstrate three simple programs.  Our test rig is a Raspberry Pi Pico USB board using the earliest firmware.  This driver should work equally well on other Microcontrollers using the same driver set.

In this video, 
 - Demonstrate three example screens on the Waveshare GC9A01 display.
 - Present three display samples and test rig wiring.
 - Discuss the driver update.
 - Walk through the driver code update.

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video60

# Files

Desktop

 - test_helloworld_gc9a01.py       Simple program that displays a single widget.
 - test_colordots_gc9a01.py        Program that displays colorful circle objects.
 - test_clock_gc9a01.py            Program that displays a clock based on your localtime from Thonny.

Flash

 - display_driver.py               Calls the display driver (in this case the ili9xxx.Gc9a01). Edit pins here.
 - ili9xxx.py                      The display classes; includes ILI9341, ST7796, and now GC9A01.
 - lv_utils.py                     A utility used by LVGL.
 - st77xx.py                       Base display class.
 - xpt2046.py                      Not used by the GC9A01 driver.