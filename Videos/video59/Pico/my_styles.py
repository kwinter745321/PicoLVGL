# my_styles.py
#
# Created: 13 October 2025
#
# Copyright (C) 2025 KW Services.
# MIT License
#
# Verified on: 14 October 2025
# MicroPython v1.26.0 on 2025-08-15; Raspberry Pi Pico 2 W with RP2350
# LVGL 9.3
import lvgl as lv
lv.init()

# colors
black = lv.color_hex(0)
white = lv.color_hex(0xFFFFFF)
bluedk = lv.color_hex(0x2F8CD8)
bluegrad = lv.color_hex(0x005782)
blueborder = lv.color_hex(0x0077b3)
bluepress =  lv.color_hex(0x006699)
bluepressgrad = lv.color_hex(0x00334d)
tf_font = lv.font_montserrat_24
text_font = lv.font_montserrat_16

dispp = lv.display_get_default()
##light_theme = lv.theme_default_init(dispp, lv.palette_main(lv.PALETTE.BLUE), lv.palette_main(lv.PALETTE.RED), False, lv.font_default())
dark_theme = lv.theme_default_init(dispp, lv.palette_main(lv.PALETTE.BLUE), lv.palette_main(lv.PALETTE.RED), True, lv.font_montserrat_16)
dispp.set_theme(dark_theme)

btnstyle = lv.style_t()
btnstyle.init()
btnstyle.set_radius(5)
btnstyle.set_bg_opa(lv.OPA.COVER)
btnstyle.set_bg_color(lv.palette_main(lv.PALETTE.BLUE))
btnstyle.set_outline_width(2)
btnstyle.set_outline_color(lv.palette_main(lv.PALETTE.BLUE))
btnstyle.set_outline_pad(8)
btnstyle.set_text_font(text_font)
btnstyle.set_text_color(black)

pressedstyle = lv.style_t()
pressedstyle.init()
pressedstyle.set_bg_color(bluepress)
pressedstyle.set_bg_grad_color( bluepressgrad)
pressedstyle.set_bg_grad_dir(lv.GRAD_DIR.VER)
pressedstyle.set_text_color(white)

header_footer = lv.style_t()
header_footer.init()
header_footer.set_bg_color(bluedk)
header_footer.set_radius(0)
header_footer.set_pad_all(0)
header_footer.set_pad_row(0)
header_footer.set_pad_column(0)
header_footer.set_bg_opa(lv.OPA.COVER)
header_footer.set_bg_grad_color(bluegrad)
header_footer.set_bg_grad_dir(lv.GRAD_DIR.VER)
header_footer.set_border_color(blueborder)
header_footer.set_border_opa(lv.OPA.TRANSP)
header_footer.set_border_width(1)
header_footer.set_text_color(white)

togstyle = lv.style_t()
togstyle.init()
togstyle.set_text_color(white)

