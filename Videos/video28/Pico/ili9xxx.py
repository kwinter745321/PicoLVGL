"""Generic ILI9xxx drivers.

This code is licensed under MIT license.

Adapted from:
    https://github.com/rdagger/micropython-ili9341

The following code snippet will instantiate the driver and
automatically register it to lvgl. Adjust the SPI bus and
pin configurations to match your hardware setup::

    import ili9xxx
    from machine import SPI, Pin
    spi = SPI(0, baudrate=24_000_000, sck=Pin(18), mosi=Pin(19), miso=Pin(16))
    drv = ili9xxx.Ili9341(spi=spi, dc=15, cs=17, rst=14)
"""
from micropython import const

import st77xx

# Command constants from ILI9341 datasheet
_NOP = const(0x00)  # No-op
_SWRESET = const(0x01)  # Software reset
_RDDID = const(0x04)  # Read display ID info
_RDDST = const(0x09)  # Read display status
_SLPIN = const(0x10)  # Enter sleep mode
_SLPOUT = const(0x11)  # Exit sleep mode
_PTLON = const(0x12)  # Partial mode on
_NORON = const(0x13)  # Normal display mode on
_RDMODE = const(0x0A)  # Read display power mode
_RDMADCTL = const(0x0B)  # Read display MADCTL
_RDPIXFMT = const(0x0C)  # Read display pixel format
_RDIMGFMT = const(0x0D)  # Read display image format
_RDSELFDIAG = const(0x0F)  # Read display self-diagnostic
_INVOFF = const(0x20)  # Display inversion off
_INVON = const(0x21)  # Display inversion on
_GAMMASET = const(0x26)  # Gamma set
_DISPLAY_OFF = const(0x28)  # Display off
_DISPLAY_ON = const(0x29)  # Display on
_SET_COLUMN = const(0x2A)  # Column address set
_SET_PAGE = const(0x2B)  # Page address set
_WRITE_RAM = const(0x2C)  # Memory write
_READ_RAM = const(0x2E)  # Memory read
_PTLAR = const(0x30)  # Partial area
_VSCRDEF = const(0x33)  # Vertical scrolling definition
_MADCTL = const(0x36)  # Memory access control
_VSCRSADD = const(0x37)  # Vertical scrolling start address
_PIXFMT = const(0x3A)  # COLMOD: Pixel format set
_WRITE_DISPLAY_BRIGHTNESS = const(0x51)  # Brightness hardware dependent!
_READ_DISPLAY_BRIGHTNESS = const(0x52)
_WRITE_CTRL_DISPLAY = const(0x53)
_READ_CTRL_DISPLAY = const(0x54)
_WRITE_CABC = const(0x55)  # Write Content Adaptive Brightness Control
_READ_CABC = const(0x56)  # Read Content Adaptive Brightness Control
_WRITE_CABC_MINIMUM = const(0x5E)  # Write CABC Minimum Brightness
_READ_CABC_MINIMUM = const(0x5F)  # Read CABC Minimum Brightness
_FRMCTR1 = const(0xB1)  # Frame rate control (In normal mode/full colors)
_FRMCTR2 = const(0xB2)  # Frame rate control (In idle mode/8 colors)
_FRMCTR3 = const(0xB3)  # Frame rate control (In partial mode/full colors)
_INVCTR = const(0xB4)  # Display inversion control
_DFUNCTR = const(0xB6)  # Display function control
_PWCTR1 = const(0xC0)  # Power control 1
_PWCTR2 = const(0xC1)  # Power control 2
_PWCTRA = const(0xCB)  # Power control A
_PWCTRB = const(0xCF)  # Power control B
_VMCTR1 = const(0xC5)  # VCOM control 1
_VMCTR2 = const(0xC7)  # VCOM control 2
_RDID1 = const(0xDA)  # Read ID 1
_RDID2 = const(0xDB)  # Read ID 2
_RDID3 = const(0xDC)  # Read ID 3
_RDID4 = const(0xDD)  # Read ID 4
_GMCTRP1 = const(0xE0)  # Positive gamma correction
_GMCTRN1 = const(0xE1)  # Negative gamma correction
_DTCA = const(0xE8)  # Driver timing control A
_DTCB = const(0xEA)  # Driver timing control B
_POSC = const(0xED)  # Power on sequence control
_ENABLE3G = const(0xF2)  # Enable 3 gamma control
_PUMPRC = const(0xF7)  # Pump ratio control

_MADCTL_MY = const(0x80)  # page address order (0: top to bottom; 1: bottom to top)
_MADCTL_MX = const(0x40)  # column address order (0: left to right; 1: right to left)
_MADCTL_MV = const(0x20)  # page/column order (0: normal mode 1; reverse mode)
_MADCTL_ML = const(
    0x10
)  # line address order (0: refresh to to bottom; 1: refresh bottom to top)
_MADCTL_BGR = const(0x08)  # colors are BGR (not RGB)
_MADCTL_RTL = const(0x04)  # refresh right to left

_MADCTL_ROTS = (
    const(_MADCTL_MX),  # 0 = portrait
    const(_MADCTL_MV),  # 1 = landscape
    const(_MADCTL_MY),  # 2 = inverted portrait
    const(_MADCTL_MX | _MADCTL_MY | _MADCTL_MV),  # 3 = inverted landscape
)

ILI9XXX_PORTRAIT = st77xx.ST77XX_PORTRAIT
ILI9XXX_LANDSCAPE = st77xx.ST77XX_LANDSCAPE
ILI9XXX_INV_PORTRAIT = st77xx.ST77XX_INV_PORTRAIT
ILI9XXX_INV_LANDSCAPE = st77xx.ST77XX_INV_LANDSCAPE


class Ili9341_hw(st77xx.St77xx_hw):
    def __init__(self, **kw):
        """ILI9341 TFT Display Driver."""
        super().__init__(
            res=(240, 320),
            suppRes=[
                (240, 320),
            ],
            model=None,
            suppModel=None,
            bgr=False,
            **kw,
        )

    def config_hw(self):
        self._run_seq(
            [
                (_SLPOUT, None, 100),
                (_PWCTRB, b"\x00\xC1\x30"),  # Pwr ctrl B
                (_POSC, b"\x64\x03\x12\x81"),  # Pwr on seq. ctrl
                (_DTCA, b"\x85\x00\x78"),  # Driver timing ctrl A
                (_PWCTRA, b"\x39\x2C\x00\x34\x02"),  # Pwr ctrl A
                (_PUMPRC, b"\x20"),  # Pump ratio control
                (_DTCB, b"\x00\x00"),  # Driver timing ctrl B
                (_PWCTR1, b"\x23"),  # Pwr ctrl 1
                (_PWCTR2, b"\x10"),  # Pwr ctrl 2
                (_VMCTR1, b"\x3E\x28"),  # VCOM ctrl 1
                (_VMCTR2, b"\x86"),  # VCOM ctrl 2
                (_VSCRSADD, b"\x00"),  # Vertical scrolling start address
                (_PIXFMT, b"\x55"),  # COLMOD: Pixel format
                (_FRMCTR1, b"\x00\x18"),  # Frame rate ctrl
                (_DFUNCTR, b"\x08\x82\x27"),
                (_ENABLE3G, b"\x00"),  # Enable 3 gamma ctrl
                (_GAMMASET, b"\x01"),  # Gamma curve selected
                (
                    _GMCTRP1,
                    b"\x0F\x31\x2B\x0C\x0E\x08\x4E\xF1\x37\x07\x10\x03\x0E\x09\x00",
                ),
                (
                    _GMCTRN1,
                    b"\x00\x0E\x14\x03\x11\x07\x31\xC1\x48\x08\x0F\x0C\x31\x36\x0F",
                ),
                (_SLPOUT, None, 100),
                (_DISPLAY_ON, None),
            ]
        )

    def apply_rotation(self, rot):
        self.rot = rot
        if (self.rot % 2) == 0:
            self.width, self.height = self.res
        else:
            self.height, self.width = self.res
        self.write_register(
            _MADCTL,
            bytes([_MADCTL_BGR | _MADCTL_ROTS[self.rot % 4]]),
        )


class Ili9341(Ili9341_hw, st77xx.St77xx_lvgl):
    def __init__(self, doublebuffer=True, factor=4, **kw):
        """See :obj:`Ili9341_hw` for the meaning of the parameters."""

        Ili9341_hw.__init__(self, **kw)
        st77xx.St77xx_lvgl.__init__(self, doublebuffer, factor)





class Ili9488_hw(st77xx.St77xx_hw):
    def __init__(self, **kw):
        """ILI9488 TFT Display Driver."""
        super().__init__(
            res=(240, 320),
            suppRes=[
                (240, 320),
            ],
            model=None,
            suppModel=None,
            bgr=False,
            **kw,
        )

    def config_hw(self):
        self.display_name = 'ILI9488'
        p16 = None
        if p16:
            pix_format = [0x55]
        else:
            pix_format = [0x66]
        self._run_seq(
            [
                (_SLPOUT, None, 200),  #01
                # (_PWCTRB, b"\x00\x12\x80"),  # Pwr ctrl B  #0c5
                # (_POSC, b"\xa9\x51\x2c\x02"),  # Pwr on seq. ctrl  #0xF7
                # (_DTCA, b"\x85\x00\x78"),  # Driver timing ctrl A
                # (_PWCTRA, b"\x39\x2C\x00\x34\x02"),  # Pwr ctrl A
                # (_PUMPRC, b"\x20"),  # Pump ratio control
                # (_DTCB, b"\x00\x00"),  # Driver timing ctrl B

                (_PWCTR1, b"\x17\x15"),  # Pwr ctrl 1
                (_PWCTR2, b"\x41"),  # Pwr ctrl 2
                # (_PWCTR3, b"\x44"),  # Pwr ctrl 1
                # (_PWCTR5, b"\x00\x12\x80"),  # Pwr ctrl 2

                # (_VMCTR1, b"\x3E\x28"),  # VCOM ctrl 1
                # (_VMCTR2, b"\x86"),  # VCOM ctrl 2
                # (_VSCRSADD, b"\x00"),  # Vertical scrolling start address

                (_FRMCTR1, b"\xA0"),  # Frame rate ctrl
                (_INVCTR, b"\x02"),  #disp inverson cntrl
                # (_DISSET5, b"\x02\x02"),  #display func cntrl

                # (_DFUNCTR, b"\x08\x82\x27"),
                # (_ENABLE3G, b"\x00"),  # Enable 3 gamma ctrl
                # (_GAMMASET, b"\x01"),  # Gamma curve selected
                (_GMCTRP1, bytes([0x00, 0x03, 0x09, 0x08, 0x16, 0x0A, 0x3F, 0x78, 0x4C, 0x09, 0x0A, 0x08, 0x16, 0x1A, 0x0F])),  #xe0
                (_GMCTRN1, bytes([0x00, 0x16, 0x19, 0x03, 0x0F, 0x05, 0x32, 0x45, 0x46, 0x04, 0x0E, 0x0D, 0x35, 0x37, 0x0F])),  #e1
                #{'cmd': 0x3A, 'data': bytes(pix_format)},
                (_PIXFMT, b"\x66"),   #0x3A
                # {'cmd': 0xB0, 'data': bytes([0x00])},
                # {'cmd': 0xB1, 'data': bytes([0xA0])},
                # {'cmd': 0xB4, 'data': bytes([0x02])},
                # {'cmd': 0xB6, 'data': bytes([0x02, 0x02])},
                # {'cmd': 0xE9, 'data': bytes([0x00])},
                # {'cmd': 0x53, 'data': bytes([0x28])},
                # {'cmd': 0x51, 'data': bytes([0x7F])},
                 (_SLPOUT, None, 100),
                (_DISPLAY_ON, 0, 120),
                
            ])

    def apply_rotation(self, rot):
        self.rot = rot
        if (self.rot % 2) == 0:
            self.width, self.height = self.res
        else:
            self.height, self.width = self.res
        self.write_register(
            _MADCTL,
            bytes([_MADCTL_BGR | _MADCTL_ROTS[self.rot % 4]]),
        )


class Ili9488(Ili9488_hw, st77xx.St77xx_lvgl):
    def __init__(self, doublebuffer=True, factor=4, **kw):
        """See :obj:`Ili9488_hw` for the meaning of the parameters."""

        Ili9488_hw.__init__(self, **kw)
        st77xx.St77xx_lvgl.__init__(self, doublebuffer, factor)


RGB666 = 1
RGB565 = 2


class st7796(ili9XXX.ili9XXX):

    # The st7795 display controller has an internal framebuffer arranged in 320 x 480
    # configuration. Physical displays with pixel sizes less than 320 x 480 must supply a start_x and
    # start_y argument to indicate where the physical display begins relative to the start of the
    # display controllers internal framebuffer.

    def __init__(self,
        miso=-1, mosi=19, clk=18, cs=17, dc=0, rst=1, power=-1, backlight=15, backlight_on=1, power_on=0,
        spihost=0, spimode=0, mhz=80, hybrid=True, width=320, height=480, start_x=0, start_y=0,
        colormode=ili9XXX.COLOR_MODE_RGB, rot=ili9XXX.PORTRAIT, invert=False, double_buffer=True, half_duplex=True,
        asynchronous=False, initialize=True, color_format=lv.COLOR_FORMAT.NATIVE_REVERSE, pixel_format=RGB666):
        
        if pixel_format == RGB666:
            pixel_format = 0x06  # 262K-Colors
            factor = 4
            if lv.color_t.__SIZE__ != 4:
                raise RuntimeError(
                    'ST7796 micropython driver '
                    'requires defining LV_COLOR_DEPTH=32'
                )
        elif pixel_format == RGB565:
            factor = 2
            pixel_format = 0x05  # 65K-Colors
            if lv.color_t.__SIZE__ != 2:
                raise RuntimeError(
                    'ST7796 micropython driver '
                    'requires defining LV_COLOR_DEPTH=16'
                )
            
        else:
            raise RuntimeError(
                'Invalid pixel format, only RGB565 and RGB666 can be used'
            )

        self.display_name = 'ST7796'

        self.init_cmds = [
            {'cmd': 0x01, 'data': bytes([]), 'delay':120},  # SWRESET
            {'cmd': 0x11, 'data': bytes([]), 'delay':120},  # SLPOUT
            {'cmd': 0xF0, 'data': bytes([0xC3])},  # CSCON
            {'cmd': 0xF0, 'data': bytes([0x96])},  # CSCON
            {'cmd': 0x36, 'data': bytes([self.madctl(colormode, rot, (ili9XXX.MADCTL_MX | ili9XXX.MADCTL_MY, ili9XXX.MADCTL_MV | ili9XXX.MADCTL_MY, 0, ili9XXX.MADCTL_MX | ili9XXX.MADCTL_MV))])},  # MADCTL
            {'cmd': 0x3A, 'data': bytes([pixel_format])},  # Interface_Pixel_Format
            {'cmd': 0xB4, 'data': bytes([0x01])},  # INVTR
            {'cmd': 0xB6, 'data': bytes([0x80, 0x02, 0x3B])},  # DFC
            {'cmd': 0xE8, 'data': bytes([0x40, 0x8A, 0x00, 0x00, 0x29, 0x19, 0xA5, 0x33])},  # DOCA
            {'cmd': 0xC1, 'data': bytes([0x06])},  # PWR2
            {'cmd': 0xC2, 'data': bytes([0xA7])},  # PWR3
            {'cmd': 0xC5, 'data': bytes([0x18]), 'delay':120},  # VCMPCTL
            {'cmd': 0xE0, 'data': bytes([0xF0, 0x09, 0x0b, 0x06, 0x04, 0x15, 0x2F, 0x54, 0x42, 0x3C, 0x17, 0x14, 0x18, 0x1B])},  # PGC
            {'cmd': 0xE1, 'data': bytes([0xE0, 0x09, 0x0B, 0x06, 0x04, 0x03, 0x2B, 0x43, 0x42, 0x3B, 0x16, 0x14, 0x17, 0x1B]), 'delay':120},  # NGC
            {'cmd': 0xF0, 'data': bytes([0x3C])},  # CSCON
            {'cmd': 0xF0, 'data': bytes([0x69]), 'delay':120},  # CSCON
            {'cmd': 0x29, 'data': bytes([])}  # DISPON
        ]

        super().__init__(miso=miso, mosi=mosi, clk=clk, cs=cs, dc=dc, rst=rst, power=power, backlight=backlight,
            backlight_on=backlight_on, power_on=power_on, spihost=spihost, spimode=spimode, mhz=mhz, factor=factor, hybrid=hybrid,
            width=width, height=height, start_x=start_x, start_y=start_y, invert=invert, double_buffer=double_buffer,
            half_duplex=half_duplex, display_type=DISPLAY_TYPE_ST7796, asynchronous=asynchronous,
            initialize=initialize, color_format=color_format)
        