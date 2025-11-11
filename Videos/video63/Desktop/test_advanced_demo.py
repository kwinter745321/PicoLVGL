# test_advanced_demo.py
#
# Created: part of MicroPython LVGL source
# Updated: 10 November 2025
#
# Copyright (C) 2025 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.20.0-2510.gacfeb7b7e on 2025-11-09; linux [GCC 14.2.0] version
# LVGL 9.3

import lvgl as lv
import display_driver
from display_driver import display as disp

import lvgl as lv
# lvgl must be initialized before any lvgl function is called or object/struct is constructed!
lv.init()

##############################################################################
# Styles
##############################################################################

class ColorStyle(lv.style_t):
    def __init__(self, color):
        super().__init__()
        self.set_bg_opa(lv.OPA.COVER)
        self.set_bg_color(lv.color_hex3(color))
        self.set_bg_grad_color(lv.color_hex3(0xFFF))
        self.set_bg_grad_dir(lv.GRAD_DIR.VER)
        self.set_bg_main_stop(0)
        self.set_bg_grad_stop(128)

class ShadowStyle(lv.style_t):
    def __init__(self):
        super().__init__()
        self.set_shadow_opa(lv.OPA.COVER)
        self.set_shadow_width(3)
        self.set_shadow_color(lv.color_hex3(0xAAA))
        self.set_shadow_offset_x(5)
        self.set_shadow_offset_y(3)
        self.set_shadow_spread(0)

# A square button with a shadow when not pressed
class ButtonStyle(lv.style_t):
    def __init__(self):
        super().__init__()
        self.set_radius(lv.dpx(8))
        self.set_shadow_opa(lv.OPA.COVER)
        self.set_shadow_width(lv.dpx(10))
        self.set_shadow_color(lv.color_hex3(0xAAA))
        self.set_shadow_offset_x(lv.dpx(10))
        self.set_shadow_offset_y(lv.dpx(10))
        self.set_shadow_spread(0)

class ButtonPressedStyle(lv.style_t):
    def __init__(self):
        super().__init__()
        self.set_shadow_offset_x(lv.dpx(0))
        self.set_shadow_offset_y(lv.dpx(0))

##############################################################################
# Themes
#############################################################################
class AdvancedDemoTheme(lv.theme_t):
    def __init__(self):
        super().__init__()
        self.button_style = ButtonStyle()
        self.button_pressed_style = ButtonPressedStyle()

        # This theme is based on active theme (material)
        base_theme = lv.theme_get_from_obj(lv.screen_active())

        # This theme will be applied only after base theme is applied
        self.set_parent(base_theme)

        # Set the "apply" callback of this theme to our custom callback
        self.set_apply_cb(self.apply)

        # Activate this theme on default display
        lv.display_get_default().set_theme(self)

    def apply(self, theme, obj):
        if obj.get_class() == lv.button_class:
            obj.add_style(self.button_style, lv.PART.MAIN)
            obj.add_style(self.button_pressed_style, lv.PART.MAIN | lv.STATE.PRESSED)
##############################################################################

member_name_cache = {}

def get_member_name(obj, value):
    try:
        return member_name_cache[id(obj)][id(value)]
    except KeyError:
        pass

    for member in dir(obj):
        if getattr(obj, member) == value:
            try:
                member_name_cache[id(obj)][id(value)] = member
            except KeyError:
                member_name_cache[id(obj)] = {id(value): member}
            return member

class SymbolButton(lv.button):
    def __init__(self, parent, symbol, text):
        super().__init__(parent)
        self.symbol = lv.label(self)
        self.symbol.set_text(symbol)
        self.label = lv.label(self)
        self.label.set_text(text)
        self.set_flex_flow(lv.FLEX_FLOW.COLUMN)
        self.set_flex_align(
            lv.FLEX_ALIGN.SPACE_EVENLY, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER
        )

class Page_Buttons:
    def __init__(self, app, page):
        self.app = app
        self.page = page
        self.button_event_count = {"Play": 0, "Pause": 0}

        self.page.set_flex_flow(lv.FLEX_FLOW.ROW)
        self.page.set_flex_align(
            lv.FLEX_ALIGN.SPACE_EVENLY, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.START
        )

        self.button1 = SymbolButton(page, lv.SYMBOL.PLAY, "Play")
        self.button1.set_size(80, 80)

        self.button2 = SymbolButton(page, lv.SYMBOL.PAUSE, "Pause")
        self.button2.set_size(80, 80)

        self.label = lv.label(page)
        self.label.add_flag(lv.obj.FLAG.IGNORE_LAYOUT)
        self.label.align(lv.ALIGN.BOTTOM_LEFT, 0, 0)

        def button_cb(event, name):
            self.button_event_count[name] += 1
            event_name = get_member_name(lv.EVENT, event.code)
            if all(
                (not event_name.startswith(s)) for s in ["DRAW", "GET", "STYLE", "REFR"]
            ):
                self.label.set_text(
                    "[%d] %s %s" % (self.button_event_count[name], name, event_name)
                )

        for button, name in [(self.button1, "Play"), (self.button2, "Pause")]:
            button.add_event_cb(
                lambda event, button_name=name: button_cb(event, button_name),
                lv.EVENT.ALL,
                None,
            )

class Page_Simple:
    def __init__(self, app, page):
        self.app = app
        self.page = page
        self.test_events = []

        self.page.set_flex_flow(lv.FLEX_FLOW.COLUMN)
        self.page.set_flex_align(
            lv.FLEX_ALIGN.SPACE_EVENLY, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER
        )

        # slider
        self.slider = lv.slider(page)
        self.slider.set_width(lv.pct(80))
        self.slider_label = lv.label(page)
        self.slider.add_event_cb(self.on_slider_changed, lv.EVENT.VALUE_CHANGED, None)
        self.on_slider_changed(None)

        # style selector
        self.styles = [
            ("Gray", ColorStyle(0xCCC)),
            ("Red", ColorStyle(0xF00)),
            ("Green", ColorStyle(0x0F0)),
            ("Blue", ColorStyle(0x00F)),
        ]

        self.style_selector = lv.dropdown(page)
        self.style_selector.add_style(ShadowStyle(), lv.PART.MAIN)
        self.style_selector.align(lv.ALIGN.OUT_BOTTOM_LEFT, 0, 40)
        self.style_selector.set_options("\n".join(x[0] for x in self.styles))
        self.style_selector.add_event_cb(
            self.on_style_selector_changed, lv.EVENT.VALUE_CHANGED, None
        )

        # counter button
        self.counter_button = lv.button(page)
        self.counter_button.set_size(80, 80)
        self.counter_label = lv.label(self.counter_button)
        self.counter_label.set_text("Count")
        self.counter_label.align(lv.ALIGN.CENTER, 0, 0)
        self.counter_button.add_event_cb(self.on_counter_button, lv.EVENT.CLICKED, None)
        self.counter = 0

    def on_slider_changed(self, event):
        self.slider_label.set_text(str(self.slider.get_value()))

    def on_style_selector_changed(self, event):
        selected = self.style_selector.get_selected()
        tabview = self.app.screen_main.tabview
        if hasattr(self, "selected_style"):
            tabview.remove_style(self.selected_style, lv.PART.MAIN)
        self.selected_style = self.styles[selected][1]
        tabview.add_style(self.selected_style, lv.PART.MAIN)

    def on_counter_button(self, event):
        self.counter += 1
        self.counter_label.set_text(str(self.counter))


class Anim(lv.anim_t):
    def __init__(
        self,
        obj,
        val,
        size,
        exec_cb,
        path_cb,
        time=500,
        playback=False,
        completed_cb=None,
    ):
        super().__init__()
        self.init()
        self.set_duration(time)
        self.set_values(val, val + size)
        if callable(exec_cb):
            self.set_custom_exec_cb(exec_cb)
        else:
            self.set_exec_cb(obj, exec_cb)
        self.set_path_cb(path_cb)
        if playback:
            self.set_playback(0)
        if completed_cb:
            self.set_completed_cb(completed_cb)
        self.start()


class AnimatedChart(lv.chart):
    def __init__(self, parent, val, size):
        super().__init__(parent)
        self.val = val
        self.size = size
        self.max = 2000
        self.min = 500
        self.factor = 100
        self.anim_phase1()

    def anim_phase1(self):
        self.phase1 = Anim(
            self,
            self.val,
            self.size,
            lambda a, val: self.set_axis_range(self.AXIS.PRIMARY_Y, 0, val),
            lv.anim_t.path_ease_in,
            completed_cb=lambda a: self.anim_phase2(),
            time=(self.max * self.factor) // 100,
        )

    def anim_phase2(self):
        self.phase2 = Anim(
            self,
            self.val + self.size,
            -self.size,
            lambda a, val: self.set_axis_range(self.AXIS.PRIMARY_Y, 0, val),
            lv.anim_t.path_ease_out,
            completed_cb=lambda a: self.anim_phase1(),
            time=(self.min * self.factor) // 100,
        )

class Page_Text:
    def __init__(self, app, page):
        self.app = app
        self.page = page
        self.page.set_flex_flow(lv.FLEX_FLOW.COLUMN_WRAP)
        self.kb = lv.keyboard(self.page)
        self.ta = lv.textarea(self.page)
        self.kb.set_textarea(self.ta)
        self.ta.set_height(lv.pct(30))
        self.ta.set_width(lv.pct(100))
        
        #### Keyboard ###########
        self.kb.align(lv.ALIGN.TOP_LEFT, 0, 0)
        self.kb.set_height(lv.pct(60))
        self.kb.set_pos(0,0)
        self.kb.set_textarea(self.ta)
        self.kb.set_style_bg_color(lv.color_black(), lv.PART.MAIN)
        self.kb.set_style_text_color(lv.color_black(),lv.PART.ITEMS)


class Page_Chart:
    def __init__(self, app, page):
        self.app = app
        self.page = page
        self.page.set_flex_flow(lv.FLEX_FLOW.ROW)
        self.page.set_flex_align(
            lv.FLEX_ALIGN.SPACE_EVENLY, lv.FLEX_ALIGN.CENTER, lv.FLEX_ALIGN.CENTER
        )
        self.page.set_style_pad_all(10, lv.PART.MAIN)
        self.page.set_style_pad_gap(10, lv.PART.MAIN)
        self.chart = AnimatedChart(page, 100, 1000)
        self.chart.set_flex_grow(1)
        self.chart.set_height(lv.pct(100))
        self.series1 = self.chart.add_series(
            lv.color_hex(0xFF0000), self.chart.AXIS.PRIMARY_Y
        )
        self.chart.set_type(self.chart.TYPE.LINE)
        self.chart.set_style_line_width(3, lv.PART.ITEMS)
        self.chart.add_style(ColorStyle(0x055), lv.PART.ITEMS)
        self.chart.set_axis_range(self.chart.AXIS.PRIMARY_Y, 0, 100)
        self.chart.set_point_count(10)
        self.chart.set_series_ext_y_array(
            self.series1, [10, 20, 30, 20, 10, 40, 50, 90, 95, 90]
        )
        # self.chart.set_x_tick_texts("a\nb\nc\nd\ne", 2, lv.chart.AXIS.DRAW_LAST_TICK)
        # self.chart.set_x_tick_length(10, 5)
        # self.chart.set_y_tick_texts("1\n2\n3\n4\n5", 2, lv.chart.AXIS.DRAW_LAST_TICK)
        # self.chart.set_y_tick_length(10, 5)
        self.chart.set_div_line_count(5, 5)

        # Create a slider that controls the chart animation speed

        def on_slider_changed(event):
            self.chart.factor = self.slider.get_value()

        self.slider = lv.slider(page)
        self.slider.set_size(10, lv.pct(100))
        self.slider.set_range(10, 200)
        self.slider.set_value(self.chart.factor, 0)
        self.slider.add_event_cb(on_slider_changed, lv.EVENT.VALUE_CHANGED, None)

class Screen_Main(lv.obj):
    def __init__(self, app, *args, **kwds):
        print("Screen Main")
        self.app = app
        super().__init__(*args, **kwds)
        self.theme = AdvancedDemoTheme()
        self.tabview = lv.tabview(self)
        self.page_simple = Page_Simple(self.app, self.tabview.add_tab("Simple"))
        self.page_buttons = Page_Buttons(self.app, self.tabview.add_tab("Buttons"))
        self.page_text = Page_Text(self.app, self.tabview.add_tab("Text"))
        self.page_chart = Page_Chart(self.app, self.tabview.add_tab("Chart"))

class AdvancedDemoApplication:


    def __init__(self):
        self.screen_main = Screen_Main(self)
        lv.screen_load(self.screen_main)


app = AdvancedDemoApplication()

###################################################
def screen_exit(event):
    code = event.get_code()
    # display closed event
    if code == 41:
        import os
        os.system("stty echo")

disp.add_event_cb(screen_exit, lv.EVENT.ALL, None)

