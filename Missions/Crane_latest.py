#!/usr/bin/env python3
# Distance Conversion
wheelDiameter_mm = 56 # Look at the first number on the NUMBERxNUMBER on wheel
wheelCircumference_cm = (wheelDiameter_mm/10) * 3.14159265358979323846284338 # Convert to cm and multiply by pi for circumference
wheelCircumference_in = (wheelDiameter_mm/25.4) * 3.14159265358979323846284338 # Convert to in and multiply by pi for circumference
# inches to rotations:
# example: drive.on_for_rotations(SpeedPercent(100), SpeedPrecent(100), inToRotations(5))
# to go 5 inches
def inToRotations(inches):
    return inches/wheelCircumference_in
# centimeters to rotations:
# example: drive.on_for_rotations(SpeedPercent(100), SpeedPrecent(100), cmToRotations(5))
# to go 5 centimeters
def cmToRotations(cm):
    return cm/wheelCircumference_cm
# inches to millimeters:
def inToMillimeters(inches):
    return inches * 25.4
# centimeters to millimeters:
def cmToMillimeters(cm):
    return cm * 10

from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import GyroSensor
import time
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)

tank_drive.on_for_rotations(SpeedPercent(35), SpeedPercent(35), inToRotations(27))
tank_drive.on_for_rotations(SpeedPercent(20), SpeedPercent(20), inToRotations(-5))
tank_drive.on_for_seconds(SpeedPercent(10), SpeedPercent(20), 2.5)
tank_drive.on_for_rotations(SpeedPercent(20), SpeedPercent(20), inToRotations(3))
tank_drive.on_for_seconds(SpeedPercent(10), SpeedPercent(7), 1.5)