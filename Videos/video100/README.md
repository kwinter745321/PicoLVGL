# README.md - Video100

31 July 2026

# Scope
This is video 100 on a HMicroPythone/LVGL embedded solution. In this video, we create a Digital Compass using the QMC5883P sensor on a Raspberry Pi Pico2/2W family of microcontrollers. We use a built-in calibration procedure that significantly simplifies the effort. We then discuss the simple GUI design.  We demonstrate the digital compass screen with the LVGL Widgets as well as demonstrate the calibration procedure.   

The Test Rigs is a: Raspberry Pi Pico-2 with a GC9A01 Display. The wiring is provided. Actually we are using the WaveShare Touch-LCD-1.28 (so we demonstrate touch).  The Digital Compass screen does not require a touchscreen, so you can use an inexpensive display. You can fetch the firmware and programs from our GitHub site, and begin using them immediately.  

We provide a reference to get our local Declination from True North.  The Driver provides a way to change the heading to True North by simply entering your value in the  program's function: heading = magneto.compass_2d(Declination)  

In this video, 
 - Demonstrate a LVGL screen with the Digital Compass.
 - Review our research on the sensor and components.
 - Discuss the Test Rig and wiring.
 - Demonstrate the calibration procedure.

The code for this video is available at the GitHub site:
https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video100

# Files

- Desktop

- Flash

