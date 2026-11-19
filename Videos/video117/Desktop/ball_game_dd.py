# ball_game_dd.py
#
# Created: 16 November 2026
#
# Copyright (C) 2026 KW Services.
# MIT License
#
# Verified on:
# MicroPython v1.29.0-dirty on 2026-10-24
# Raspberry Pi Pico 2 W with RP2350
# LVGL 9.6
#
import machine
import math
import utime
import lvgl as lv
import random
import gc
from mpu9250 import MPU9250
from machine import reset, Pin
from dd import disp, touch, backlight

# --- Hardware Configuration ---
I2C_SCL = machine.Pin(9)
I2C_SDA = machine.Pin(8)
i2c = machine.I2C(0, scl=I2C_SCL, sda=I2C_SDA, freq=400000)

# Initialize MPU9250
try:
    sensor = MPU9250(i2c)
except Exception as e:
    print("Sensor Error:", e)

# --- Colors ---
COLOR_CYAN    = lv.color_hex(0x00FFFF)
COLOR_MAGENTA = lv.color_hex(0xFF00FF)
COLOR_GREEN   = lv.color_hex(0x39FF14)
COLOR_RED     = lv.color_hex(0xFF3131)
COLOR_BLUE    = lv.color_hex(0x0A2472)
COLOR_BLACK   = lv.color_hex(0x000000)
COLOR_WHITE   = lv.color_hex(0xFFFFFF)

# --- Game Constants ---
BALL_SIZE = 40
RADIUS = BALL_SIZE // 2
FRICTION = 0.98
SENSOR_SENSITIVITY = 0.8
#### Landscape Orientation
BOX_W = 320  #### disp.width
BOX_H = 240  #### disp.height
BORDER = 4
ALPHA = 0.15  # Low-Pass Filter constant

#### Safe Zone to make ball does not go past borders
SAFE_X_MIN = RADIUS
SAFE_X_MAX = BOX_W - RADIUS
SAFE_Y_MIN = RADIUS
SAFE_Y_MAX = BOX_H - RADIUS

#### Game Globals ####
score = 0
lost_balls = 0
max_balls = 3
balls = [] # List of ball_obj
goal_pos = [0, 0]
trap_pos = [0, 0]
game_active = False
waiting_for_spawn = False
spawn_x, spawn_y = 160, 120
num = 0
done = False
#### Sensor Filter
prev_roll = 0.0
prev_pitch = 0.0

def start_cb(e):
    global game_active
    start.add_flag(lv.obj.FLAG.HIDDEN)
    game_active = True
    utime.sleep_ms(200)

class BALL:
    def __init__(self,obj,x,y):
        self.obj = obj   # lvgl obj
        self.x = x       # x position
        self.y = y       # y position
        self.vx = 0      # x speed
        self.vy = 0      # y speed

#### UI ##################
scr = lv.screen_active()
scr.set_style_pad_all(0, lv.PART.MAIN)
scr.set_style_text_font(lv.font_montserrat_16, lv.PART.MAIN)
scr.remove_flag(lv.obj.FLAG.SCROLLABLE)
lv.screen_load(scr)

# Background
bg = lv.obj(scr)
bg.set_size(BOX_W, BOX_H)
bg.set_style_bg_color(COLOR_BLUE, lv.PART.MAIN)
bg.set_style_border_width(BORDER, lv.PART.MAIN)
bg.set_style_border_color(COLOR_CYAN, lv.PART.MAIN)
bg.set_style_pad_all(0, lv.PART.MAIN)
bg.remove_flag(lv.obj.FLAG.SCROLLABLE)

start = lv.button(bg)
start.set_size(BOX_W//3,BOX_H//3)
start.center()
startlbl = lv.label(start)
startlbl.set_text("Start")
startlbl.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN)
startlbl.center()
start.add_event_cb(start_cb, lv.EVENT.PRESSED, None)

#### Score Label
score_lbl = lv.label(bg)
score_lbl.set_style_text_color(COLOR_WHITE, lv.PART.MAIN)
score_lbl.set_text("Score: 0")
score_lbl.align(lv.ALIGN.TOP_LEFT, 10, 10)

#### Ball Count Label
balls_lbl = lv.label(bg)
balls_lbl.set_style_text_color(COLOR_CYAN, lv.PART.MAIN)
balls_lbl.set_text("Balls: "+str(max_balls))
balls_lbl.align(lv.ALIGN.TOP_RIGHT, -10, 10)

#### Lost Balls Label
lost_lbl = lv.label(bg)
lost_lbl.set_style_text_color(COLOR_RED, lv.PART.MAIN)
#lost_lbl.set_style_text_font(lv.font_montserrat_14, lv.PART.MAIN)
lost_lbl.set_text("Lost: 0")
lost_lbl.align(lv.ALIGN.TOP_MID, 0, 10)

#### Direction Symbol
dir_lbl = lv.label(bg)
dir_lbl.set_style_text_color(COLOR_WHITE, lv.PART.MAIN)
dir_lbl.set_text(f"{lv.SYMBOL.MINUS} FLAT")
dir_lbl.align(lv.ALIGN.CENTER, 0, 75)

#### Goal (Green)
goal_obj = lv.obj(bg)
goal_obj.set_size(BALL_SIZE+10, BALL_SIZE+10)
goal_obj.set_style_bg_color(COLOR_GREEN, lv.PART.MAIN)
goal_obj.set_style_radius(RADIUS, lv.PART.MAIN)
goal_obj.set_style_bg_opa(lv.OPA.TRANSP, lv.PART.MAIN)
goal_obj.set_style_border_width(4, lv.PART.MAIN)
goal_obj.set_style_border_color(COLOR_GREEN, lv.PART.MAIN)
goal_obj.add_flag(lv.obj.FLAG.HIDDEN)
goal_obj.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
goal_lbl = lv.label(goal_obj)
goal_lbl.set_text("Goal")
goal_lbl.set_style_text_font(lv.font_montserrat_14, lv.PART.MAIN)
goal_lbl.set_style_text_color(COLOR_GREEN,lv.PART.MAIN)
goal_lbl.center()

#### Trap (Red)
trap_obj = lv.obj(bg)
trap_obj.set_size(BALL_SIZE+10, BALL_SIZE+10)
trap_obj.set_style_bg_color(COLOR_RED, lv.PART.MAIN)
trap_obj.set_style_radius(RADIUS, lv.PART.MAIN)
trap_obj.set_style_bg_opa(lv.OPA.TRANSP, lv.PART.MAIN)
trap_obj.set_style_border_width(4, lv.PART.MAIN)
trap_obj.set_style_border_color(COLOR_RED, lv.PART.MAIN)
trap_obj.add_flag(lv.obj.FLAG.HIDDEN)
trap_obj.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
trap_lbl = lv.label(trap_obj)
trap_lbl.set_text("Trap")
trap_lbl.set_style_text_font(lv.font_montserrat_14, lv.PART.MAIN)
trap_lbl.set_style_text_color(COLOR_RED,lv.PART.MAIN)
trap_lbl.center()

#### Instruction Label
instr_lbl = lv.label(bg)
instr_lbl.set_style_text_color(COLOR_WHITE, lv.PART.MAIN)
instr_lbl.set_style_text_font(lv.font_montserrat_14, lv.PART.MAIN)
instr_lbl.set_text("Press Start Button")
instr_lbl.align(lv.ALIGN.BOTTOM_MID, 0, -10)

def spawn_ball(num):
    global waiting_for_spawn, spawn_x, spawn_y
    if not waiting_for_spawn:
        # Ensure ball spawns 150 pixels away from trap
        for i in range(50):
            pos_x = random.randint(SAFE_X_MIN, SAFE_X_MAX - BALL_SIZE)
            pos_y = random.randint(SAFE_Y_MIN, SAFE_Y_MAX - BALL_SIZE)
            distance =  math.sqrt((trap_pos[0]-pos_x)**2 + (trap_pos[1]-pos_y)**2)
            if distance > 150:
                spawn_x = pos_x
                spawn_y = pos_y
                break
    
    ball_obj = lv.obj(bg)
    ball_obj.set_size(BALL_SIZE, BALL_SIZE)
    ball_obj.set_style_bg_color(COLOR_MAGENTA, lv.PART.MAIN)
    ball_obj.set_style_border_color(COLOR_MAGENTA, lv.PART.MAIN)
    ball_obj.set_style_radius(20, lv.PART.MAIN)
    ball_obj.set_style_bg_opa(lv.OPA._80, lv.PART.MAIN)
    ball_obj.add_flag(lv.obj.FLAG.HIDDEN)
    ball_obj.set_scrollbar_mode(lv.SCROLLBAR_MODE.OFF)
    lbl = lv.label(ball_obj)
    lbl.set_text(str(num))
    lbl.set_style_text_font(lv.font_montserrat_24, lv.PART.MAIN)
    lbl.set_style_text_color(COLOR_BLACK, lv.PART.MAIN)
    lbl.center()
    balls.append( BALL(ball_obj, spawn_x, spawn_y) )
    gc.collect()
    waiting_for_spawn = False

####  Update game
def update_game():
    global score, lost_balls, max_balls, waiting_for_spawn
    global prev_roll, prev_pitch, num, done
    global goal_pos, trap_pos

    if game_active:
        # Access acceleration and 
        accel = sensor.acceleration
        raw_roll = accel[1]
        raw_pitch = accel[0]
        #apply Low-Pass Filter (alpha = 0.15)
        roll = (ALPHA * raw_roll) + ((1 - ALPHA) * prev_roll)
        pitch = (ALPHA * raw_pitch) + ((1 - ALPHA) * prev_pitch)
        prev_roll = roll
        prev_pitch = pitch
        for b in balls[:]:
            b.vx += roll * SENSOR_SENSITIVITY
            b.vy += pitch * SENSOR_SENSITIVITY
            b.vx *= FRICTION
            b.vy *= FRICTION
            b.x += b.vx
            b.y += b.vy
            #### Wall Bounds: Ensure ball stays entirely inside region
            if b.x <= 0 or b.x >= BOX_W - BALL_SIZE - BORDER*2:
                b.vx *= -0.8
                b.x = max(0, min(b.x, BOX_W - BALL_SIZE - BORDER*2))
            if b.y <= 0 or b.y >= BOX_H - BALL_SIZE - BORDER*2:
                b.vy *= -0.8
                b.y = max(0, min(b.y, BOX_H - BALL_SIZE - BORDER*2))
            #### Update Position
            b.obj.set_pos(int(b.x), int(b.y))
            b.obj.remove_flag(lv.obj.FLAG.HIDDEN)
            #### Collision Detection
            dist_goal = math.sqrt((b.x - goal_pos[0])**2 + (b.y - goal_pos[1])**2)
            dist_trap = math.sqrt((b.x - trap_pos[0])**2 + (b.y - trap_pos[1])**2)

            if dist_goal < 30:
                score += num
                score_lbl.set_text("Score: {}".format(score))
                b.obj.delete()
                balls.remove(b)
                if lost_balls < 3:
                    setup_targets()
                    waiting_for_spawn = True
                    utime.sleep_ms(100)
                else:
                    done = True
                continue 

            elif dist_trap < 30:
                max_balls -= 1
                lost_balls += 1
                lost_lbl.set_text("Lost: {}".format(lost_balls))
                b.obj.delete()
                balls.remove(b)
                if lost_balls < 3:
                    setup_targets()
                    waiting_for_spawn = True
                else:
                    done = True
                    instr_lbl.set_text("GAME OVER")
                continue 

        balls_lbl.set_text(f"Balls: {max_balls}")
        if waiting_for_spawn and len(balls) == 0 and max_balls > 0:
            num += 1
            spawn_ball(num)
        if balls:
            ref_vx = balls[0].vx
            ref_vy = balls[0].vy
            if abs(ref_vx) > 0.2 and abs(ref_vx) > abs(ref_vy):
                if ref_vx > 0:
                    dir_lbl.set_text(f"{lv.SYMBOL.RIGHT} RIGHT")
                    dir_lbl.set_style_text_color(COLOR_CYAN, lv.PART.MAIN)
                else:
                    dir_lbl.set_text(f"{lv.SYMBOL.LEFT} LEFT")
                    dir_lbl.set_style_text_color(COLOR_MAGENTA, lv.PART.MAIN)
            elif abs(ref_vy) > 0.2 and abs(ref_vy) > abs(ref_vx):
                if ref_vy > 0:
                    dir_lbl.set_text(f"{lv.SYMBOL.UP} UP")
                    dir_lbl.set_style_text_color(COLOR_CYAN, lv.PART.MAIN)
                else:
                    dir_lbl.set_text(f"{lv.SYMBOL.DOWN} DOWN")
                    dir_lbl.set_style_text_color(COLOR_MAGENTA, lv.PART.MAIN)
            else:
                dir_lbl.set_text(f"{lv.SYMBOL.MINUS} FLAT")
                dir_lbl.set_style_text_color(COLOR_WHITE, lv.PART.MAIN)
            
        utime.sleep_ms(20)
    else:
        utime.sleep_ms(100)

####  Position Goal and Trap
def setup_targets():
    global goal_pos, trap_pos
    goal_obj.remove_flag(lv.obj.FLAG.HIDDEN)
    trap_obj.remove_flag(lv.obj.FLAG.HIDDEN)
    for i in range(50):
        goal_pos = [random.randint(SAFE_X_MIN, SAFE_X_MAX - (BALL_SIZE+10)), random.randint(SAFE_Y_MIN, SAFE_Y_MAX - (BALL_SIZE+10))]
        tx = random.randint(SAFE_X_MIN, SAFE_X_MAX - (BALL_SIZE+10))
        ty = random.randint(SAFE_Y_MIN, SAFE_Y_MAX - (BALL_SIZE+10))
        distance =  math.sqrt((tx - goal_pos[0])**2 + (ty - goal_pos[1])**2)
        if distance > 150:
            trap_pos = [tx, ty]
            # print(f"iterated: {i} to place trap")
            break
        # elif i == 50:
        #     print(f"iterated: {i} to place trap")

    goal_obj.set_pos(goal_pos[0], goal_pos[1])
    trap_obj.set_pos(tx, ty)

####  Main Loop
print("Ball Game Ready. Press Button to Start.")
setup = False
num = 1
score = 0
score_lbl.set_text("Score: 0")
balls = []
max_balls = 3
lost_balls = 0
lost_lbl.set_text("Lost: 0")
utime.sleep_ms(200)
#### done begins as False
while not done:
    if setup == False and game_active == True:
        setup_targets()
        instr_lbl.set_text("Playing...")
        spawn_ball(num)
        setup = True
        utime.sleep_ms(200)
        instr_lbl.set_text("")
    update_game()
#### when done is true
print("Game Statistics\n"+"="*40)
print(f"Score: {score} with: {num} ball spawns.")
#
print("Thanks for playing.")