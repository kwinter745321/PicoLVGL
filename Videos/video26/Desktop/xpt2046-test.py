import sys
sys.path.append('.')
from xpt2046 import *


TP_CLK_PIN=18
TP_MOSI_PIN=19
TP_MISO_PIN=16

TP_CS_PIN=21  # Make sure this is the T_CS for Touch

# make sure the SPI is same as used for Display
spi=machine.SPI(
    0,
    baudrate=2_000_000, # the chip does not handle more than 2MHz (!)
    polarity=0,
    phase=0,
    sck=machine.Pin(TP_CLK_PIN, machine.Pin.OUT),
    mosi=machine.Pin(TP_MOSI_PIN, machine.Pin.OUT),
    miso=machine.Pin(TP_MISO_PIN, machine.Pin.OUT),
)

tsc=Xpt2046_hw(spi=spi,cs=TP_CS_PIN,rot=1)
for i in range(100000):
    if p:=tsc.pos(): print(p)

