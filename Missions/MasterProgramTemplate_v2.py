#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from ev3dev2.display import Display
import time
btn = Button()
color = ColorSensor(INPUT_4)
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)  #This is the template whenever we code
Sound_ = Sound()
Display_ = Display()
Sound_.play_tone(frequency=400, duration=0.5, volume=50) #plays a note so we know when the code starts

#yellow = forwards
def yellow():
    tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 1)

#green = backwards
def green():
    tank_drive.on_for_rotations(SpeedPercent(-50), SpeedPercent(-50), 1)

#red = turn *
def red():
    tank_drive.on_for_rotations(SpeedPercent(0), SpeedPercent(50), 1)

#blue = turn *
def blue():
    tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(0), 1)

#definning what "ColorChecking" is
def ColorChecking():
    if color.color == color.COLOR_YELLOW: #if yellow
        yellow()
    elif color.color == color.COLOR_GREEN:#if green
        green()
    elif color.color == color.COLOR_RED:#if red
        red()
    elif color.color == color.COLOR_BLUE: 
        blue()

#This is where the movement happens. the function "ColorChecking" is a function to decide what to do based on color.

#not whenever we touch enter (or the mibble button) then it will call ColorChecking(). Not just when this line happens
Sound_.play_tone(frequency=400, duration=0.5, volume=50)
start = time.time()

while (time.time() - start) <= 30: #this code essentially waits 30 seconds
    pass
    btn.wait_for_released('right')
    ColorChecking()
#hello
#
Sound_.play_tone(frequency=400, duration=0.5, volume=50)