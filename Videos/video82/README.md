# README.md - Video82

26 March 2026

# Scope
This is video 82 on a MicroPython/LVGL embedded solution. In this video, we try a Round Touch LCD display.  We had trouble using the CST816S driver (and found that others have also.)  We found a simple solution though.  

We use firmware published on March 02. Our test rig is a Pico W (RP2040) with an integrated GC9A01 Display. You can fetch the firmware and programs from our GitHub site, and begin using them immediately.  

In this video, 
 - We demonstrate our typical GUI test programs on the touch LCD
 - We explain our project expectations
 - We discuss the minor but important software changes
 - Our review will show where we made the minor changes.

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video82

Background music is 7th Life by Adam MacDougall which is You Tube Licensed as not requiring an attribution.

# Files

 - Desktop
   - test_button3_display.py
   - test_matrix3_display.py

 - Firmware  
  - See the firmware in Video 79

 - Flash

  - cst816.py
  - display_driver.py
  - ili9xxx.py
  - lv_utils.py
  - st77xx.py
