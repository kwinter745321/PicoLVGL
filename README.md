# README PicoLVGL

MicroPython LVGL for Raspberry Pi Pico

This GitHub Repository (Repo) provides MicroPython LVGL 9.x information regarding the Raspberry Pi Pico.  Here I have collected datasheets, firmware and programs for each YouTube video.

The firmware are files that result from the build of "micropython_lv". Although several output files are generated, the most useful is the "firmware.uf2" file.  One can load their Pico, by pressing the Pico's button while plugging its USB cable into a desktop. Then drag the "firmware.uf2" file into the virtual drive that appears.

# Firmware 

These firmware files are special because they contain the LVGL library within the firmware.  They are built in a Linux environment following the online directions.
Admittedly the online directions are not that clear; hence I generated the files.

| USB Board | MicroPython | LVGL | Build Date    |
|-----------|-------------|------|---------------|
| Pico      | v1.20       | v9.1 | 19 Feb 2025   |
| PicoW     | v1.20       | v9.1 | 27 Feb 2025   |
| Pico2     | v1.20       | v9.3 | 24 March 2025 |
| Pico2W    | -           | -    | -             |

kdschlosser is working on a new method of building the firmware which hopefully results in a newer version of MicroPython paired with the LVGL files.

# Programs

The programs assume you loaded your Pico with one of the above appropriate firmware.

The programs are groups of files for the Desktop and the Pico. MicroPython files for the desktop are load and run in Thonny.  Link: https://thonny.org

 The Pico files should be uploaded (via Thonny) to the virtual drive on the Pico.  These are usually driver files.  These files can be in the root or in a subdirectory called "lib".  Occasionally, I update a driver file.  I usually download it to the desktop to save it in a backup folder. Then using Thonny, I delete it on the virtual drive and re-upload (or I edit it within Thonny and save.)  

