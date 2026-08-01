# Summary of Video100: "v100 Digital Compass"

## Overview
This video demonstrates a **Digital Compass** built using **MicroPython 1.27** and **LVGL 9.5** on a **Pico2 USB board** with a **WaveShare GC9A01 Touch-LCD 1.28"** display. It's designed to be affordable, using a $3 QMC5883P magnetometer sensor (mounted in plastic brackets) and a CST816 touchscreen instead of the common XPT2046.

## Key Features

### Hardware & Setup
- **Display**: GC9A01 (ili9xxx driver), 240x240 pixel round screen. LVGL widgets stay inside a circular area.
- **Touchscreen**: CST816 driver with glossy glass + factory-calibrated points; uses MicroPython's **SoftI2C**.
- **Sensor**: QMC5883P GY271, mounted on plastic nylon screws for metal-interference mitigation. Uses **SoftSPI** for I2C communication.
- **Mounting**: 3D-printed bracket with two nylon screws, avoiding metal objects near the sensor.

### Software
- **LVGL Widgets**: Four simple widgets — a compass scale (static red pointer), heading display, digital heading, and a test button.
- **Drivers**: Modified GitHub driver by TurboFan for QMC5883P; includes auto-calibration and saved/load calibration results.
- **Code**: Uses **MicroPython** with standard `import` syntax; runs from flash or desktop.

## Calibration & Accuracy
- **Calibration**: Requires hundreds of readings to calculate hard/soft iron offsets. Z-axis ignored for basic heading (ArcTan2(Y/X)).
- **Accuracy**: Initial attempts failed to point north; the issue was a mis-identified GY271 sensor. The TurboFan driver fixed this, improving accuracy significantly.
- **Declination**: Optional adjustment for True North.

## Demonstration
- **Demo**: The compass reacts smoothly to rotation, mimicking a watch face. Tested with `test_button3_display.py` and `test_compass_display.py`.
- **Reset**: A hard reset is required to switch programs.

## Notes
- Subscribes to the channel and likes help the channel.
- The project emphasizes affordability, simplicity, and a polished look with a round display.
- IMU sensors (for pitch/roll/altitude) are mentioned as an optional upgrade for flight applications.

This project is ideal for hobbyists and embedded systems enthusiasts looking for an affordable, visually appealing compass solution.
