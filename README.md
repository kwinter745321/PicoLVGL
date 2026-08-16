# README PicoLVGL

MicroPython LVGL for Raspberry Pi Pico

This GitHub Repository (Repo) provides MicroPython LVGL 9.x information regarding the Raspberry Pi Pico.  Here I collect datasheets, firmware and programs for each YouTube video.

The firmware are files that result from the build of "micropython_lv". Although several output files are generated, the most useful is the "firmware.uf2" file.  One can load their Pico, by pressing the Pico's button while plugging its USB cable into a desktop. Then drag the "firmware.uf2" file into the virtual drive that appears.

# Firmware 

These firmware files are special because they contain the LVGL library within the firmware.  They are built in a Linux environment following the online directions.  Admittedly the online directions are not that clear; hence I generated the files.

All of these were built from the legacy lv_micropython web site.  Some firmware in 2025 are built with ulab
I did not edit any file but simply built as is (hence the banner says 1.20.)

Starting in 2026, many of the firmware are built using a combination of the MicroPython and lv_micropython sites. As the
app is bigger now, the ulab portion is not always included.

# Programs

The programs assume you loaded your Pico with one of the above appropriate firmware.

The programs are groups of files for the Desktop and the Pico. MicroPython files for the desktop are load and run in Thonny.  Link: https://thonny.org

 The Pico files should be uploaded (via Thonny) to the virtual drive on the Pico.  These are usually driver files.  These files can be in the root or in a subdirectory called "lib".  Occasionally, I update a driver file.  I usually download it to the desktop to save it in a backup folder. Then using Thonny, I delete it on the virtual drive and re-upload (or I edit it within Thonny and save.)  

 # PicoLVGL — Videos by Subject

A subject-oriented index of videos associated with the [PicoLVGL](https://github.com/kwinter745321/PicoLVGL) GitHub repository.

The subjects are listed in **alphabetical order**. Videos may appear under more than one subject when they cover multiple related topics.

> **Repository:** [kwinter745321/PicoLVGL](https://github.com/kwinter745321/PicoLVGL)  
> **Videos:** [PicoLVGL Videos](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos)

---

## Table of Contents

- [Build Environment](#build-environment)
- [Displays](#displays)
- [Display Drivers](#display-drivers)
- [Fonts](#fonts)
- [Firmware](#firmware)
- [GUI Design](#gui-design)
- [LVGL](#lvgl)
- [MicroPython](#micropython)
- [Networking](#networking)
- [Observers](#observers)
- [Raspberry Pi Pico](#raspberry-pi-pico)
- [ROMFS](#romfs)
- [Rotary Encoders](#rotary-encoders)
- [SD Card](#sd-card)
- [Sensors](#sensors)
- [Simulator](#simulator)
- [Touchscreens](#touchscreens)
- [ulab](#ulab)
- [Widgets](#widgets)
- [Recommended Learning Paths](#recommended-learning-paths)
- [Repository Video Directory](#repository-video-directory)
- [Maintenance](#maintenance)

---

# Build Environment

Videos covering firmware compilation, source builds, and development environments.

### Video 30 — MicroPython LVGL 9: Introduction to ulab

- ulab build options
- Firmware builds
- MicroPython
- LVGL
- JupyterLab

[Video 30 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video30)

### Video 42 — MicroPython 1.25: What's ROMFS?

- MicroPython 1.25
- ROMFS
- Building firmware
- Deploying firmware
- Pico2W

[Video 42 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video42)

### Video 51 — Building MicroPython with LVGL and ulab

- Ubuntu setup
- lv_micropython
- Build prerequisites
- Firmware compilation
- Firmware verification

[Video 51 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video51)

---

# Displays

Videos dealing with display hardware, display selection, resolutions, and display-specific projects.

### Video 20 — Using ILI9341 LCD Display

- ILI9341
- Nano-GUI
- Display API
- Pico
- Fonts and widgets

[Video 20 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video20)

### Video 22 — Get Started with MicroPython LVGL v9

- ILI9341
- Touch
- SD Card
- Raspberry Pi Pico
- LVGL 9

[Video 22 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video22)

### Video 26 — Keyboard Widget / Display Testing

- ILI9341
- 2.8-inch and 3.2-inch displays
- Keyboard widget
- Touch
- Driver changes

[Video 26 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video26)

### Video 31 — Let's Use a Larger Display

- 320×480 displays
- ST7796
- ILI9341
- Larger GUI layouts
- Touch

[Video 31 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video31)

### Video 32 — Display Orientation

- Portrait
- Landscape
- Inverted Portrait
- Inverted Landscape
- ST7796
- ILI9341

[Video 32 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video32)

### Video 60 — GC9A01 Display

- GC9A01
- Round displays
- Display driver
- Clock
- Color dots

[Video 60 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video60)

### Video 62 — ST7735 Display

- ST7735
- Display driver
- Small displays
- Pico
- ESP32

[Video 62 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video62)

### Video 74 — ST7789 Displays

- ST7789
- Multiple resolutions
- Display driver updates
- Pico firmware

[Video 74 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video74)

### Video 76 — Integrated ST7789 Display

- ST7789
- Audio
- SD card
- RTC
- IMU
- Pico2

[Video 76 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video76)

### Video 85 — ILI9488 Display Investigation

- ILI9488
- 320×480
- Display compatibility
- XPT2046
- Driver development

[Video 85 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video85)

### Video 86 — Improved ILI9488 Display Driver

- ILI9488
- 16-bit and 18-bit displays
- RGB565 conversion
- Pico2W
- ESP32-S3
- Viper

[Video 86 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video86)

### Video 93 — ST7796 Display Driver Setup

- ST7796
- 320×480
- Display driver
- Pico2W
- XPT2046

[Video 93 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video93)

---

# Display Drivers

### Video 26 — ILI9341 Driver Updates

- Different display sizes
- Driver corrections
- Touch configuration

[Video 26 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video26)

### Video 31 — Larger Display Driver

- ST7796
- ILI9341
- 320×480
- XPT2046

[Video 31 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video31)

### Video 32 — Orientation Support

- Driver orientation
- Display transforms
- ST7796
- ILI9341

[Video 32 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video32)

### Video 41 — Capacitive Touch Driver

- FT6X36
- I2C
- Hosyond ST7796S
- Touch driver

[Video 41 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video41)

### Video 60 — GC9A01 Driver

- GC9A01
- `ili9xxx.py`
- Driver architecture

[Video 60 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video60)

### Video 62 — ST7735 Driver

- ST7735
- `st77xx.py`
- Driver update

[Video 62 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video62)

### Video 74 — ST7789 Driver

- ST7789
- New display models
- Resolution handling

[Video 74 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video74)

### Video 85 — ILI9488 Driver

- ILI9488
- Driver compatibility
- Proof-of-concept driver

[Video 85 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video85)

### Video 86 — Improved ILI9488 Driver

- RGB565
- 18-bit display mode
- Performance optimization
- Viper

[Video 86 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video86)

### Video 93 — Display Driver Configuration

- `display_driver.py`
- Pin configuration
- ST7796
- XPT2046

[Video 93 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video93)

---

# Fonts

### Video 28 — It's Easy to Add Fonts

- External fonts
- LVGL embedded fonts
- Font acquisition
- Font conversion
- Binary font files
- SD Card

[Video 28 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video28)

---

# Firmware

Videos useful when selecting, building, updating, or understanding Pico-family MicroPython/LVGL firmware.

### Video 22 — MicroPython LVGL v9

- Pico firmware
- Pico W firmware
- LVGL 9.1
- ILI9341

[Video 22 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video22)

### Video 26 — Multiple LVGL Firmware Versions

- Pico
- Pico W
- Pico2
- LVGL 9.1 / 9.3

[Video 26 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video26)

### Video 30 — ulab Firmware

- MicroPython 1.24.1
- LVGL 9.3
- ulab
- Firmware build options

[Video 30 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video30)

### Video 39 — Pico2W Firmware

- Pico2W
- RP2350
- MicroPython 1.25
- LVGL 9.3

[Video 39 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video39)

### Video 42 — ROMFS Firmware

- MicroPython 1.25
- ROMFS
- Pico2W
- 128 KiB ROMFS partition

[Video 42 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video42)

### Video 44 — LVGL 9.4 Firmware

- MicroPython 1.25
- LVGL 9.4
- ulab
- Pico / Pico W / Pico2 / Pico2W

[Video 44 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video44)

### Video 51 — Building Firmware

- lv_micropython
- MicroPython
- LVGL
- ulab
- Ubuntu

[Video 51 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video51)

### Video 74 — Updated ST7789 Firmware

- Pico firmware
- ST7789
- Multiple displays

[Video 74 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video74)

### Video 76 — Pico2 Firmware with 16 MB Flash

- Pico2
- 16 MB external flash
- Integrated display
- Audio
- SD Card

[Video 76 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video76)

### Video 79 — LVGL 9.5 Firmware

- LVGL 9.5
- Pico-family firmware
- Pico2W
- Chart widget

[Video 79 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video79)

### Video 82 — Round Touch Display Firmware

- Pico W
- GC9A01
- Firmware from Video 79

[Video 82 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video82)

### Video 85 — ILI9488 Firmware

- Pico2W
- ILI9488
- XPT2046

[Video 85 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video85)

### Video 86 — Pico2W / ESP32-S3 Firmware

- Pico2W UF2
- ESP32-S3 BIN
- ILI9488

[Video 86 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video86)

### Video 100 — Digital Compass Firmware

- Pico2 / Pico2W
- QMC5883P
- GC9A01
- LVGL

[Video 100 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video100)

---

# GUI Design

### Video 33 — Interesting LVGL Program

- GUI application
- Temperature and humidity
- Networking
- Asyncio

[Video 33 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video33)

### Video 38 — LVGL Canvas

- Canvas
- Drawing
- Touch interaction
- Pick-and-place GUI

[Video 38 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video38)

### Video 59 — Dynamic Screen Layout

- Responsive layouts
- Multiple resolutions
- Styles
- Navigation
- Gestures

[Video 59 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video59)

### Video 100 — Digital Compass GUI

- LVGL widgets
- Compass screen
- Calibration
- Touch

[Video 100 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video100)

---

# LVGL

### Video 22 — Get Started with MicroPython LVGL v9

- LVGL 9
- MicroPython
- Pico
- ILI9341
- Touch

[Video 22 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video22)

### Video 23 — Button Events

- LVGL events
- Buttons
- Event callbacks
- Passing event data

[Video 23 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video23)

### Video 24 — List and Related Widgets

- List
- Roller
- Dropdown
- MessageBox
- Spinner
- Styles

[Video 24 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video24)

### Video 25 — Scale Widget

- Scale
- Scale parts
- Bar + Scale
- Round Scale
- Simulator

[Video 25 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video25)

### Video 26 — Keyboard Widget

- Keyboard
- Touch
- Display sizes
- LVGL 9

[Video 26 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video26)

### Video 29 — LVGL Encoder

- Encoder input
- Rotary encoder
- Widget groups
- Navigation

[Video 29 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video29)

### Video 30 — Chart Widget and ulab

- Chart
- ulab
- Data processing
- JupyterLab

[Video 30 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video30)

### Video 31 — Large Display Widgets

- Matrix
- Chart
- Keyboard
- Touch

[Video 31 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video31)

### Video 32 — Orientation

- Display orientation
- Keyboard
- Driver integration

[Video 32 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video32)

### Video 36 — Hardware Buttons and LVGL

- INDEV
- Encoder
- Button input
- Hardware pushbuttons

[Video 36 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video36)

### Video 38 — Canvas

- Canvas drawing
- LVGL simulator
- Touch
- Drawing objects

[Video 38 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video38)

### Video 39 — Flex

- LVGL Flex
- Layout
- Pico2W
- Responsive UI

[Video 39 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video39)

### Video 44 — Subjects and Observers

- LVGL 9.4
- Observer module
- Subjects
- Data observation

[Video 44 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video44)

### Video 54 — Slider and Button GUI

- Slider
- Button
- GUI examples
- Pico

[Video 54 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video54)

### Video 59 — Dynamic Screen Layout

- Screen layout
- Navigation
- Gestures
- Styles

[Video 59 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video59)

### Video 63 — LVGL Simulator on Raspberry Pi

- LVGL simulator
- MicroPython
- SDL2
- Raspberry Pi OS

[Video 63 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video63)

### Video 79 — LVGL 9.5 Chart

- LVGL 9.5
- Chart
- Pico2W
- Web data

[Video 79 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video79)

### Video 93 — Button and Slider

- ST7796
- Button
- Slider
- Display driver

[Video 93 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video93)

### Video 100 — Digital Compass

- LVGL
- Compass GUI
- Widgets
- Calibration

[Video 100 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video100)

---

# MicroPython

This is the primary subject area of the PicoLVGL repository.

### Video 20 — ILI9341 LCD Display

- MicroPython
- ILI9341
- Nano-GUI

[Video 20 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video20)

### Video 22 — MicroPython LVGL v9

- MicroPython
- LVGL 9
- Pico
- Touch
- SD Card

[Video 22 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video22)

### Video 23 — Button Events

- MicroPython
- LVGL events
- Button callbacks

[Video 23 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video23)

### Video 24 — List Widgets

- MicroPython
- List
- Roller
- Dropdown
- Styles

[Video 24 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video24)

### Video 25 — Scale Widget

- MicroPython
- LVGL Scale
- Simulator

[Video 25 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video25)

### Video 26 — Keyboard Widget

- MicroPython
- Keyboard
- ILI9341
- Touch

[Video 26 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video26)

### Video 27 — SD Card

- MicroPython
- SD Card
- Images
- LVGL filesystem

[Video 27 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video27)

### Video 28 — External Fonts

- MicroPython
- LVGL fonts
- SD Card
- Font conversion

[Video 28 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video28)

### Video 29 — Rotary Encoder

- MicroPython
- Rotary encoder
- LVGL input
- Widget groups

[Video 29 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video29)

### Video 30 — ulab

- MicroPython
- ulab
- JupyterLab
- Charts

[Video 30 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video30)

### Video 31 — Larger Displays

- MicroPython
- 320×480
- ST7796
- ILI9341

[Video 31 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video31)

### Video 32 — Display Orientation

- MicroPython
- Display drivers
- Orientation

[Video 32 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video32)

### Video 33 — Networking and Asyncio

- MicroPython
- Networking
- Asyncio
- Pico W

[Video 33 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video33)

### Video 36 — Hardware Buttons

- MicroPython
- GPIO
- Buttons
- LVGL INDEV

[Video 36 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video36)

### Video 38 — Canvas

- MicroPython
- Canvas
- Simulator
- Touch

[Video 38 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video38)

### Video 39 — Flex

- MicroPython
- LVGL Flex
- Pico2W

[Video 39 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video39)

### Video 41 — Capacitive Touch

- MicroPython
- FT6X36
- I2C
- Touch

[Video 41 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video41)

### Video 42 — ROMFS

- MicroPython 1.25
- ROMFS
- Pico2W

[Video 42 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video42)

### Video 44 — LVGL 9.4

- MicroPython 1.25
- LVGL 9.4
- Observers
- ulab

[Video 44 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video44)

### Video 51 — Firmware Build

- MicroPython
- LVGL
- ulab
- Ubuntu

[Video 51 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video51)

### Video 54 — GUI Setup

- MicroPython
- LVGL
- Slider
- Button

[Video 54 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video54)

### Video 59 — Dynamic Layout

- MicroPython
- LVGL
- Multiple displays
- Styles

[Video 59 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video59)

### Video 60 — GC9A01

- MicroPython
- Round display
- GC9A01

[Video 60 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video60)

### Video 62 — ST7735

- MicroPython
- ST7735
- Display drivers

[Video 62 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video62)

### Video 63 — Raspberry Pi Simulator

- MicroPython
- LVGL
- SDL2
- Raspberry Pi

[Video 63 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video63)

### Video 74 — ST7789

- MicroPython
- ST7789
- Display drivers

[Video 74 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video74)

### Video 76 — Integrated Touch LCD

- MicroPython
- ST7789
- Audio
- SD Card
- RTC
- IMU

[Video 76 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video76)

### Video 79 — LVGL 9.5

- MicroPython
- LVGL 9.5
- Chart
- Open-Meteo

[Video 79 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video79)

### Video 82 — Round Touch LCD

- MicroPython
- GC9A01
- CST816S
- Pico W

[Video 82 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video82)

### Video 85 — ILI9488

- MicroPython
- ILI9488
- Pico2W
- XPT2046

[Video 85 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video85)

### Video 86 — Improved ILI9488

- MicroPython
- ILI9488
- RGB565
- Viper

[Video 86 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video86)

### Video 93 — Display Driver

- MicroPython
- ST7796
- XPT2046
- Pico2W

[Video 93 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video93)

### Video 100 — Digital Compass

- MicroPython
- QMC5883P
- Pico2 / Pico2W
- LVGL

[Video 100 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video100)

---

# Networking

### Video 33 — An Interesting Program

- Pico W
- Networking
- Asyncio
- Temperature/humidity display

[Video 33 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video33)

### Video 79 — Open-Meteo Weather Data

- Open-Meteo API
- Web data
- Pico2W
- LVGL Chart

[Video 79 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video79)

---

# Observers

### Video 44 — What Are Subjects and Observers?

- LVGL 9.4
- Observer module
- Subjects
- Data changes
- MicroPython

[Video 44 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video44)

---

# Raspberry Pi Pico

The repository is specifically focused on MicroPython/LVGL for the Raspberry Pi Pico family. The README describes firmware and programs for Pico, Pico W, Pico2, and related boards.

### Video 22 — Get Started with MicroPython LVGL v9

[Video 22 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video22)

### Video 27 — SD Card

[Video 27 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video27)

### Video 30 — ulab

[Video 30 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video30)

### Video 36 — Hardware Buttons

[Video 36 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video36)

### Video 39 — Pico2W Flex

[Video 39 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video39)

### Video 42 — Pico2W ROMFS

[Video 42 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video42)

### Video 44 — LVGL 9.4

[Video 44 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video44)

### Video 51 — Firmware Build

[Video 51 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video51)

### Video 74 — ST7789

[Video 74 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video74)

### Video 76 — Pico2 Integrated Display

[Video 76 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video76)

### Video 79 — Pico2W + LVGL 9.5

[Video 79 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video79)

### Video 82 — Pico W + GC9A01

[Video 82 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video82)

### Video 85 — Pico2W + ILI9488

[Video 85 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video85)

### Video 86 — Pico2W + ILI9488

[Video 86 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video86)

### Video 93 — Pico2W + ST7796

[Video 93 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video93)

### Video 100 — Pico2 / Pico2W Digital Compass

[Video 100 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video100)

---

# ROMFS

### Video 42 — MicroPython 1.25: What's ROMFS?

- ROMFS
- MicroPython 1.25
- Firmware
- Pico2W
- Building and deploying applications

[Video 42 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video42)

---

# Rotary Encoders

### Video 29 — Will a LVGL Encoder Work?

- LVGL Encoder input
- KY-040 rotary encoder
- Wiring
- Driver files
- Widget groups
- Navigation
- 3D-printable mounting plate

[Video 29 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video29)

---

# SD Card

### Video 22 — Get Started with MicroPython LVGL v9

- ILI9341
- Integrated SD Card
- Pico
- LVGL

[Video 22 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video22)

### Video 27 — Let's Use the SD Card

- SD Card wiring
- SPI
- Image files
- Image resizing
- LVGL filesystem
- `fs_driver`

[Video 27 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video27)

### Video 28 — External Fonts

- SD Card
- Font files
- LVGL filesystem
- External fonts

[Video 28 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video28)

### Video 76 — Integrated Display with SD Card

- SD Card
- ST7789
- Audio
- 16 MB flash

[Video 76 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video76)

---

# Sensors

### Video 33 — Temperature and Humidity

- Temperature/humidity application
- Pico W
- Networking
- Asyncio
- LVGL

[Video 33 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video33)

### Video 76 — Integrated IMU

- IMU sensor
- ST7789
- Pico2
- Audio
- SD Card

[Video 76 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video76)

### Video 100 — Digital Compass

- QMC5883P magnetometer
- Calibration
- Compass heading
- Magnetic declination
- Pico2 / Pico2W

[Video 100 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video100)

---

# Simulator

### Video 25 — LVGL MicroPython Simulator

- Online simulator
- LVGL 9
- Scale widget
- Simulator compatibility

[Video 25 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video25)

### Video 30 — ulab and the Chart Widget

- LVGL simulator
- Chart
- LVGL 9.0 compatibility
- ulab

[Video 30 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video30)

### Video 38 — Canvas with the Online Simulator

- Canvas
- Drawing
- Touch
- Simulator

[Video 38 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video38)

### Video 63 — LVGL Simulator on Raspberry Pi

- Raspberry Pi
- Raspberry Pi OS
- SDL2
- MicroPython LVGL
- Bookworm
- Trixie

[Video 63 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video63)

---

# Touchscreens

### Video 22 — ILI9341 Touch

- Integrated touchscreen
- ILI9341
- XPT2046

[Video 22 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video22)

### Video 26 — Touch Reconfiguration

- XPT2046
- 2.8-inch and 3.2-inch displays
- Touch driver

[Video 26 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video26)

### Video 32 — Touch and Orientation

- XPT2046
- Display orientation
- 320×480

[Video 32 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video32)

### Video 36 — Hardware Buttons

- Hardware input
- LVGL INDEV
- Encoder
- Buttons

[Video 36 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video36)

### Video 41 — Capacitive Touch

- FT6X36
- I2C
- Hosyond ST7796S
- Capacitive touch

[Video 41 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video41)

### Video 82 — Round Touch LCD

- GC9A01
- CST816S
- Pico W
- Touchscreen orientation

[Video 82 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video82)

### Video 85 — ILI9488 + XPT2046

- ILI9488
- XPT2046
- Pico2W

[Video 85 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video85)

### Video 86 — ILI9488 + XPT2046

- ILI9488
- Touch
- Pico2W
- ESP32-S3

[Video 86 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video86)

### Video 93 — ST7796 + XPT2046

- ST7796
- XPT2046
- Pico2W

[Video 93 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video93)

### Video 100 — GC9A01 Touch

- GC9A01
- CST816
- Pico2
- Digital Compass

[Video 100 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video100)

---

# ulab

### Video 30 — Introduction to ulab

- ulab
- JupyterLab
- Numerical functions
- LVGL Chart
- Firmware with ulab

[Video 30 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video30)

### Video 31 — Larger Display Chart

- ulab
- LVGL Chart
- 480×320 display
- Updated chart example

[Video 31 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video31)

### Video 44 — LVGL 9.4 and Latest ulab

- LVGL 9.4
- MicroPython 1.25
- ulab
- Observer

[Video 44 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video44)

---

# Widgets

### Video 23 — Button Events

- Button
- Events
- Callbacks

[Video 23 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video23)

### Video 24 — List Widgets

- List
- Roller
- Dropdown
- MessageBox
- Spinner

[Video 24 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video24)

### Video 25 — Scale

- Scale
- Bar
- Round Scale

[Video 25 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video25)

### Video 26 — Keyboard

- Keyboard
- Text input
- Touch

[Video 26 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video26)

### Video 29 — Encoder Groups

- Encoder
- Slider
- Widget groups
- Navigation

[Video 29 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video29)

### Video 30 — Chart

- Chart
- ulab
- Data

[Video 30 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video30)

### Video 31 — Matrix, Chart, and Keyboard

- Matrix
- Chart
- Keyboard
- Text area

[Video 31 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video31)

### Video 36 — Button and Encoder Input

- Button
- Slider
- Encoder
- INDEV

[Video 36 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video36)

### Video 38 — Canvas

- Canvas
- Drawing
- Touch

[Video 38 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video38)

### Video 44 — Observer

- Slider
- Observer
- Subject
- Data changes

[Video 44 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video44)

### Video 54 — Slider and Button

- Slider
- Button
- GUI

[Video 54 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video54)

### Video 60 — Hello World, Color Dots, and Clock

- Label
- Color objects
- Clock

[Video 60 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video60)

### Video 62 — Hello World and Color Dots

- Button
- Color dots
- Display testing

[Video 62 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video62)

### Video 63 — LVGL Demonstration Programs

- Button
- Keyboard
- Matrix
- Advanced demo
- Slider

[Video 63 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video63)

### Video 79 — Chart

- Chart
- Weather data
- Web API

[Video 79 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video79)

### Video 93 — Button and Slider

- Button
- Slider
- ST7796

[Video 93 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video93)

### Video 100 — Digital Compass

- Compass
- Labels
- Buttons
- Calibration GUI

[Video 100 files](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video100)

---

# Recommended Learning Paths

## Beginner — MicroPython + LVGL

1. [Video 22 — Get Started with MicroPython LVGL v9](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video22)
2. [Video 23 — Button Events](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video23)
3. [Video 24 — List and Related Widgets](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video24)
4. [Video 25 — Scale Widget](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video25)
5. [Video 26 — Keyboard Widget](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video26)
6. [Video 36 — Hardware Buttons](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video36)
7. [Video 54 — Slider and Button GUI](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video54)

## Display / Touch Developer

1. [Video 22 — ILI9341](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video22)
2. [Video 26 — Multiple ILI9341 Sizes](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video26)
3. [Video 31 — 320×480 Displays](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video31)
4. [Video 32 — Display Orientation](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video32)
5. [Video 41 — Capacitive Touch](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video41)
6. [Video 60 — GC9A01](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video60)
7. [Video 74 — ST7789](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video74)
8. [Video 85 — ILI9488](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video85)
9. [Video 86 — Improved ILI9488](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video86)
10. [Video 93 — ST7796](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video93)

## Firmware Builder

1. [Video 30 — ulab Firmware](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video30)
2. [Video 42 — ROMFS](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video42)
3. [Video 44 — LVGL 9.4 Firmware](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video44)
4. [Video 51 — Build MicroPython/LVGL/ulab](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video51)
5. [Video 76 — Pico2 16 MB Flash](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video76)
6. [Video 79 — LVGL 9.5 Firmware](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video79)

## Advanced LVGL

1. [Video 29 — Rotary Encoder](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video29)
2. [Video 30 — ulab and Chart](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video30)
3. [Video 38 — Canvas](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video38)
4. [Video 39 — Flex](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video39)
5. [Video 44 — Subjects and Observers](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video44)
6. [Video 59 — Dynamic Screen Layout](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video59)
7. [Video 63 — Raspberry Pi Simulator](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video63)
8. [Video 79 — LVGL 9.5 + Open-Meteo](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video79)
9. [Video 100 — Digital Compass](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos/video100)

---

# Repository Video Directory

The current `Videos` directory contains these video folders:

```text
video20
video22
video23
video24
video25
video26
video27
video28
video29
video30
video31
video32
video33
video34
video35
video36
video38
video39
video41
video42
video44
video51
video54
video59
video60
video62
video63
video74
video76
video79
video82
video85
video86
video93
video100
```

[Open the complete Videos directory](https://github.com/kwinter745321/PicoLVGL/tree/main/Videos)

---


**Last reviewed:** August 16, 2026




