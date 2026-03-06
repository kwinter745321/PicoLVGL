# test_chart_display.py
#
# Created: 03 March 2026
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.27.0-dirty on 2026-03-02;
# Raspberry Pi Pico 2 W with RP2350
#
# This program uses data from the Open-Meteo web site
#

import lvgl as lv
from machine import reset, Pin
from display_driver import disp, touch
from secrets import ssid, password
import time
import requests
import json
import network

lv.init()

#### globals ################################
datamin = 0      # Chart data range low
datamax = 100    # Chart data range high
chrt_wd = 210    # Chart width
chrt_ht = 238    # Chart height
btnplot = None   # plot button
chart = None     # chart object
title = None     # chart title
title_size = 4   # length of title
xaxis = None     # xaxis
ser1 = None      # data series 1
ser2 = None      # data series 2
sta_if = None    # network object
response = None  # open-meteo response
hold = []        # holds a copy of open-meteo response
weather = None   # weather response
all_keys = []    # open-meteo weather items
mydata = []      # parsed weather data
index = 1        # index for mydata[]
index2 = 3       # index2 for mydata[]
################################################
#  REPLACE string below with your URL
#  only parses a request for HOURLY DATA
################################################
meteo = "https://api.open-meteo.com/v1/forecast?latitude=39.679&longitude=-75.747&hourly=temperature_2m,relative_humidity_2m,weather_code&timezone=America%2FNew_York&forecast_days=3&wind_speed_unit=mph&temperature_unit=fahrenheit&precipitation_unit=inch"
# meteo = "PasteHere"
#meteo = "https://api.open-meteo.com/v1/forecast?latitude=39.52&longitude=-76.41&hourly=temperature_2m,relative_humidity_2m,weather_code,pressure_msl,dew_point_2m,surface_pressure&forecast_days=3"

# weather code meaning:
# 0–49: No precipitation (e.g., 0=clear, 45=fog).
# 50–59: Drizzle.
# 60–69: Rain.
# 70–79: Solid precipitation (snow).
# 80–99: Showers and thunderstorms.

#### colors ####################################
RED = lv.palette_main(lv.PALETTE.RED)
GREEN = lv.palette_main(lv.PALETTE.GREEN)
BLUE = lv.palette_main(lv.PALETTE.BLUE)
CYAN = lv.palette_main(lv.PALETTE.CYAN)
PURPLE = lv.palette_main(lv.PALETTE.PURPLE)

#### Network connection ################

def do_disconnect():
    global sta_if
    if sta_if == None:
        return "Not connected."
    if sta_if.isconnected():
        print("Connected to network. Disconnecting...")
        sta_if.disconnect()
        sta_if.active(False)
        msg = "Disconnected."
        print(msg)
        return msg
    else:
        return "Not connected now."
    
def do_connect():
    global sta_if, c_status
    print("do_connect() started")
    count = 0
    sta_if = network.WLAN(network.WLAN.IF_STA)
    if not sta_if.isconnected():
        msg = "Connecting to network... Please wait..."
        print(msg)
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            count += 1
            if count > 100_000:
                print(".", end="")
                count = 0
    print()
    if sta_if:
        msg = "Network connected as: " + str(sta_if.ipconfig('addr4'))
    else:
        msg = "Failed to connect."
    print(msg)
    return msg

def show_connect():
    global sta_if
    if sta_if:
        msg = "Network connected as:" + str(sta_if.ipconfig('addr4'))
    else:
        msg = "Not connected."
    print(msg)
    return(msg)

##### Open Meteo Request ############################################

def do_request(x):
    global hold, response
    response = None
    w = []
    try:
        response = requests.get(x)
        if response.status_code == 200:
            #print(response.status_code)
            #print(response.text)
            hold = response.text
            w = json.loads(hold)
    except Exception as e:
        print(f"do_request() Failed, exception: {e}")
        print("Are you connected to the network?")
    finally:
        if response != None:
            response.close()
    return w

def get_weather():
    global meteo
    w = do_request(meteo)
    return w

#### Parse ########################################################################

def get_all_keys(data):
    if isinstance(data, dict):
        for key, value in data.items():
            yield key
            yield from get_all_keys(value) 
    elif isinstance(data, list):
        for item in data:
            yield from get_all_keys(item) 

def get_data(data,find):
    if isinstance(data, dict):
        for key, value in data.items():
            if find in key:
                yield value
            yield from get_data(value,find)
    elif isinstance(data, list):
        for item in data:
            yield from get_data(item,find) 

def load_data(data):
    global all_keys, mydata
    all_keys = list(get_all_keys(data["hourly_units"]))
    print(50*'-')
    print("%10s %30s %5s" % ("Units", "Item", "Index"))
    print(50*'-')
    mydata = []
    idx = 0
    for itemkey in all_keys:
        if itemkey == 'time':
            mydata.append(list(get_data(data,itemkey))[3])
            units = list(get_data(data,itemkey))[1]
        else:
            mydata.append(list(get_data(data,itemkey))[1])
            units = list(get_data(data,itemkey))[0]
        print("%10s %30s %5d" % (units, itemkey, idx))
        idx += 1
    print(50*'-')

#### UI ######################################################################
scr = lv.obj()
lv.screen_load(scr)
scr.set_style_bg_color(lv.color_black(),0)

cont = lv.obj(scr)
cont.set_size(320,240)
cont.set_layout(lv.LAYOUT.FLEX)
#cont.set_style_bg_color(lv.color_black(),0)
cont.set_flex_flow(lv.FLEX_FLOW.COLUMN_WRAP)
cont.set_flex_align(lv.FLEX_ALIGN.SPACE_EVENLY,lv.FLEX_ALIGN.CENTER,lv.FLEX_ALIGN.CENTER)
cont.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
#######
        
def setup_chart(scr):
    global datamin, datamax, chrt_wd, chrt_ht
    global chart, xaxis, ser1, ser2, title
    # chart
    chart = lv.chart(scr)
    chart.set_size(chrt_wd, chrt_ht)
    chart.set_pos(0,0)
    chart.set_div_line_count(10,10)
    chart.add_flag(lv.obj.FLAG.OVERFLOW_VISIBLE)
    chart.set_type(lv.chart.TYPE.LINE) # Use LINE type
    # lvgl 9.5
    chart.set_axis_range(lv.chart.AXIS.PRIMARY_X, datamin, datamax)
    # lvgl 9.0
    #chart.set_range(lv.chart.AXIS.PRIMARY_Y, datamin, datamax)
    #### pad chart for scales ##########################
    chart.set_style_pad_left(35, lv.PART.MAIN)
    chart.set_style_pad_bottom(25, lv.PART.MAIN)
    chart.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
    #title = lv.label(chart)
    #title.set_text("New")
    # Data Series
    ser1 = chart.add_series(RED, lv.chart.AXIS.PRIMARY_Y)
    ser2 = chart.add_series(GREEN, lv.chart.AXIS.PRIMARY_Y)
    # style
    style = lv.style_t()
    style.init()
    style.set_line_width(2)
    style.set_line_color(BLUE)
    style.set_line_rounded(True) 
    chart.add_style(style, lv.PART.ITEMS)

    # Add ticks and label to every axis
    xaxis = lv.scale(chart)
    #xaxis.set_size( chrt_ht+50, lv.pct(100) )
    xaxis.set_size( chrt_wd-50, chrt_ht-20 )
    xaxis.set_style_line_width(1, lv.PART.MAIN)
    xaxis.set_mode(lv.scale.MODE.HORIZONTAL_BOTTOM)
    xaxis.set_align(lv.ALIGN.BOTTOM_MID)
    xaxis.set_y(chrt_ht-20)
    #xaxis.set_range(0,datacount)
    xaxis.set_total_tick_count(13)  
    xaxis.set_major_tick_every(2)
    xaxis.set_style_text_color(PURPLE, lv.PART.INDICATOR)
    xaxis.set_style_text_font(lv.font_montserrat_16, lv.PART.INDICATOR)

    yaxis = lv.scale(chart)
    yaxis.set_range(datamin, datamax)
    #yaxis.set_size( lv.pct(100), chrt_ht)
    yaxis.set_size( chrt_wd-25, chrt_ht-35 )
    yaxis.set_style_line_width(1, lv.PART.MAIN)
    yaxis.set_mode(lv.scale.MODE.VERTICAL_LEFT)
    yaxis.set_align(lv.ALIGN.LEFT_MID)
    yaxis.set_x(25-chrt_wd)
    yaxis.set_style_length(5, lv.PART.ITEMS)
    yaxis.set_total_tick_count(11)
    yaxis.set_major_tick_every(2)
    yaxis.set_style_text_color(PURPLE, lv.PART.INDICATOR)
    yaxis.set_style_text_font(lv.font_montserrat_16, lv.PART.INDICATOR)

#### Updates x Axis
def set_hours(x):
    global chart, xaxis
    chart.set_point_count(x)
    xaxis.set_range(0,x)

#### if data values are > 100 then scale to 0-100
def scale_data(data):
    if not data:
        return []
    min_val = min(data)
    max_val = max(data)
    # Avoid division by zero
    if min_val == max_val:
        return [0.0] * len(data)
    scaled_data = []
    for item in data:
        # change 100 to datamax if different
        scaled_item = ((item - min_val) / (max_val - min_val)) * 100
        scaled_data.append(scaled_item)
    return scaled_data    

def plot_data():
    global chart, xaxis, mydata, title, title_size
    global index, index2
    #############################################
    if mydata == []:
        print("Fetch data.\n")
    #### use item choices ############################
    title_text = "Legend\n_______\n"
    #points = scale_data(mydata[idx])  
    points = mydata[index]
    title_text += "R:" + all_keys[index][:title_size] + "\n" 
    ##########
    #points2 = scale_data(mydata[idx2])
    points2 = mydata[index2]
    title_text += "G:" + all_keys[index2][:title_size] 
    ##### Convert data to int #######################
    pt = []
    for p in points:
        pt.append(int(p))
    pt2 = []
    for p in points2:
        pt2.append(int(p))
    datacount = len(points)
    set_hours(datacount)
    #pt.reverse()  #in case you prefer to reverse direction of data
    ##### Plot Data Series ###########################################
    # lvgl 9.5
    chart.set_series_ext_y_array(ser1, pt)
    # lvgl 9.0
    #chart.set_ext_y_array(ser1, pt)
    ###########
    # lvgl 9.5
    chart.set_series_ext_y_array(ser2, pt2)
    # lvgl 9.0
    #chart.set_ext_y_array(ser2, pt2)
    ################################################
    title.set_text("    \n    ")
    title.set_text(title_text)
    chart.refresh()

def draw_title():
    global title
    title = lv.label(cont)
    title.set_size(86,80)
    title.set_text("")

def btnplot_cb(event):
    print("Plot data--please wait.\n")
    plot_data()

def draw_btnplot():
    global btnplot
    btnplot = lv.button(cont)
    btnplot.set_size(86,40)
    #btnplot.set_style_bg_color(CYAN,lv.PART.MAIN)
    lblplot = lv.label(btnplot)
    lblplot.set_text("Plot")
    lblplot.center
    #lblplot.set_style_text_color(lv.color_black(), lv.PART.MAIN)
    lblplot.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN)
    btnplot.add_event_cb(btnplot_cb, lv.EVENT.CLICKED, None)

################################################################
#### MAIN CODE
################################################################
#### Setup
setup_chart(cont)
draw_btnplot()
draw_title()
#### Operate
use_test_data = False
index = 1
index2 = 3
if use_test_data == True:
    w = '{"latitude":52.52,"longitude":13.41,"generationtime_ms":0.34737586975097656,"utc_offset_seconds":-18000,"timezone":"America/New_York","timezone_abbreviation":"GMT-5","elevation":35.0,"hourly_units":{"time":"iso8601","temperature_2m":"°F","relative_humidity_2m":"%","weather_code":"wmo code"},"hourly":{"time":["2026-03-03T00:00","2026-03-03T01:00","2026-03-03T02:00","2026-03-03T03:00","2026-03-03T04:00","2026-03-03T05:00","2026-03-03T06:00","2026-03-03T07:00","2026-03-03T08:00","2026-03-03T09:00","2026-03-03T10:00","2026-03-03T11:00","2026-03-03T12:00","2026-03-03T13:00","2026-03-03T14:00","2026-03-03T15:00","2026-03-03T16:00","2026-03-03T17:00","2026-03-03T18:00","2026-03-03T19:00","2026-03-03T20:00","2026-03-03T21:00","2026-03-03T22:00","2026-03-03T23:00","2026-03-04T00:00","2026-03-04T01:00","2026-03-04T02:00","2026-03-04T03:00","2026-03-04T04:00","2026-03-04T05:00","2026-03-04T06:00","2026-03-04T07:00","2026-03-04T08:00","2026-03-04T09:00","2026-03-04T10:00","2026-03-04T11:00","2026-03-04T12:00","2026-03-04T13:00","2026-03-04T14:00","2026-03-04T15:00","2026-03-04T16:00","2026-03-04T17:00","2026-03-04T18:00","2026-03-04T19:00","2026-03-04T20:00","2026-03-04T21:00","2026-03-04T22:00","2026-03-04T23:00","2026-03-05T00:00","2026-03-05T01:00","2026-03-05T02:00","2026-03-05T03:00","2026-03-05T04:00","2026-03-05T05:00","2026-03-05T06:00","2026-03-05T07:00","2026-03-05T08:00","2026-03-05T09:00","2026-03-05T10:00","2026-03-05T11:00","2026-03-05T12:00","2026-03-05T13:00","2026-03-05T14:00","2026-03-05T15:00","2026-03-05T16:00","2026-03-05T17:00","2026-03-05T18:00","2026-03-05T19:00","2026-03-05T20:00","2026-03-05T21:00","2026-03-05T22:00","2026-03-05T23:00"],"temperature_2m":[31.4,31.4,31.7,31.7,31.9,32.1,31.4,32.2,32.3,33.2,34.2,35.0,36.4,37.2,37.7,38.5,38.9,39.4,39.1,39.0,39.0,39.1,39.6,40.8,42.2,43.7,44.7,45.1,45.0,44.9,44.5,44.5,45.1,46.8,49.7,51.8,52.5,54.8,53.8,53.1,52.1,51.7,50.4,49.9,49.3,49.3,48.9,47.8,46.7,45.8,45.2,45.1,45.8,46.5,46.4,46.3,47.1,49.3,51.8,57.5,63.0,65.5,66.7,67.5,67.7,64.6,61.9,60.3,58.9,57.8,57.2,57.7],"relative_humidity_2m":[78,69,70,74,73,76,88,94,96,95,96,96,97,97,98,99,100,100,99,99,99,98,97,96,95,96,96,96,96,96,94,94,96,97,92,87,86,85,85,88,94,95,95,96,94,94,95,97,97,96,97,99,99,99,99,99,98,97,92,83,74,70,67,67,71,82,89,91,92,94,96,96],"weather_code":[3,3,3,3,3,3,71,73,53,53,53,53,51,3,51,45,45,45,45,51,51,53,53,3,3,3,3,55,55,3,3,3,3,3,3,3,3,3,3,51,53,3,3,3,3,3,3,3,45,45,3,3,51,51,51,51,45,51,3,3,3,3,3,2,1,3,3,2,3,51,53,80]}}'
    data = json.loads(w)
    load_data(data)
else:
    do_disconnect()
    do_connect()
    #### open-meteo URL defined above
    w = get_weather()
    load_data(w)