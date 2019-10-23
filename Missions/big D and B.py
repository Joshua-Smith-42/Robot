#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from time import sleep

colorR = ColorSensor(INPUT_2)
colorL = ColorSensor(INPUT_3)
color = ColorSensor(INPUT_4)
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
motorD = MediumMotor(OUTPUT_D)

wheelDiameter_mm = 56
wheelCircumference_cm = (wheelDiameter_mm/10) * 3.14159265358979323846284338
wheelCircumference_in = (wheelDiameter_mm/25.4) * 3.14159265358979323846284338

def inToRotations(inches):
    return inches/wheelCircumference_in

def cmToRotations(cm):
    return cm/wheelCircumference_cm

def inToMillimeters(inches):
    return inches * 25.4

def cmToMillimeters(cm):
    return cm * 10

def drive_cm(power, cm):
    rt = cmToRotations(cm)
    tank_drive.on_for_rotations(SpeedPercent(power), SpeedPercent(power), int(rt) )

drive_cm(50, 65)
drive_cm(-50, 65)