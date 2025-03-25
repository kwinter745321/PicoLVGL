# README.md - video 20

# Using ILI9341 LCD Display

12 January 2025

## files on the Desktop

aclock.py is the "main program" file that makes call into the API.

## API Files on the Pico
	
API files with only the drivers for the ili9341 LCD Display.
Original GitHub files can be found here: 
[MicroPython-Nano-GUI](https://github.com/peterhinch/micropython-nano-gui)

| Folders | File list |
|---------|-----------|
| drivers | boolpalette.py |
|         | li9341_pico.py |
|         | ili9341.py      |
|         |                  | 
| gui     | core "folder"    |
|         | fonts "folder"   |
|         | widgets "folder" |
|         |                 |
| color_setup.py |          |
|           |              |

## Using the API

Changes to the Nano-GUI files were minimized to keep Peter's files as-is as much as possible.
I run the main program within Thonny on the desktop and the API files all exist on the Pico \flash directory.

Notes:
- The imports were updated with the proper folder. (Becuase they were moved.)
- The color_setup.py is modified to use ili9341_pico. This is the "interface" file used by Peter.
- Color Names were added to the aclock.py program (as described below.)

CWriter is the class to display text on a LCD Display. It requires a font.
Fonts are defined in font files.  The Peter Hinch font files are in a specific format and contain class methods withsize information for the specific font.  These font files are therefore compatiable only with demo programs mentioned in the Nano-GUI API. or, by creating a program that uses Nano-GUI graphics.

## Using the Demo Programs

The demo program "aclock.py" is what I used to test the API.

There is a micropython file called colors.py withing gui/core.  This should define colors for your program.
But I had to add this fragment to the top of aclock to get it to "know" the colors:

```
#added
from gui.core.colors import BLACK, GREEN, RED, YELLOW
```

Other demo programs could be run from Thonny.  But I did not try them all.