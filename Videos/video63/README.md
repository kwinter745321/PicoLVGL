# README - Video 63

11 November 2025

# Scope

This is video 63 on embedded solutions. In this video, we run the LVGL Simulator on a Raspberry Pi. To ensure it executes, we the MicroPython LVGL application from source and configure a SDL2 Display on the Raspberry Pi OS.  We tested the application on Raspberry PI OS Bookworm and Raspberry PI OS Trixie (the latest).

In this video, 
 - Demonstrate three LVGL program.
 - Discuss the MicroPython LVGL Source and executable.
 - Walk through the application build.

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video63

# Files

- Executable (Folder)
 - Bookworm
     - micropython                  Built on Raspberry Pi 5 Bookworm
 - Trixie
     - micropython                  Built on Raspberry Pi 5 Trixie

 - Desktop (Folder)
     - display_driver.py          Edit this file to change display resolution.
     - test_button_display.py     Makes sure RGB is okay and abiltiy to touch a button.
     - test_keyboard_display.py   Tests the keyboard.
     - test_matrix_display.py     Displays colorful buttons.
     - test_advanced_demo.py      Modified version of an example program from lvgl team.
     - test_slider_display        Test program from a previous video.

>Note: If you want to invoke these programs from a remote folder like we did in the video, then first enter this command in the terminal (before starting MicroPython):
>
>```
>export DISPLAY=:0.0
>```
>
