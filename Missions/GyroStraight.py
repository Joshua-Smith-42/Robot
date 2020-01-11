#!/usr/bin/env python3

# FLL 42, Pythonian Rabbotics's master program. Copyright (c) 2019 FLL team 42

#---------------------------------------------------Imports and variable definitions-----------------------------------------------------------------
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from ev3dev2.display import Display
import time
import sys
btn = Button()
color = ColorSensor(INPUT_4)
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)  #This is the template whenever we code
motorA = MediumMotor(OUTPUT_A)
motorD = MediumMotor(OUTPUT_D)
gyro = GyroSensor(INPUT_1)
Sound_ = Sound()
Display_ = Display()
Sound_.play_tone(frequency=400, duration=0.5, volume=50) #plays a note so we know when the code starts
#------------------------------------------------------------------------------------------------------------------------------#
def gyroStraight(OUTPUT_B, OUTPUT_C, rotations):
    startAng = gyro.angle
    if deg >= 0:
        while (gyro.angle-startAng) <= deg:
            tank_drive.on_for_rotations(SpeedPercent(30), SpeedPercent(40),(rotations) )
    if deg < 0:
        while (gyro.angle-startAng) <= deg:
            tank_drive.on_for_rotations(SpeedPercent(40), SpeedPercent(30),(rotations) )
    tank_drive.off()
gyroStraight(30, 40, 5)