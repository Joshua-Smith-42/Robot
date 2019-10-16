#!/usr/bin/env python3

# This is the blue attachment.

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
color = ColorSensor(INPUT_2)
gyro = GyroSensor(INPUT_1)
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
motorD = MediumMotor(OUTPUT_D)
# Move there
# 22 1/4 in forward
tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), inToRotations(22.25))
# Move attachment down
motorD.on_for_seconds(SpeedPercent(-8), 1.8)
# Drive forward a bit
tank_drive.on_for_seconds(SpeedPercent(20), SpeedPercent(15), 0.3)
tank_drive.on_for_rotations(SpeedPercent(10), SpeedPercent(10), inToRotations(2.5)) # Yay, no syntax errors!
tank_drive.on_for_seconds(SpeedPercent(21), SpeedPercent(17), 0.1)
tank_drive.on_for_rotations(SpeedPercent(10), SpeedPercent(10), inToRotations(2.25))
# Drive back a bit
tank_drive.on_for_rotations(SpeedPercent(10), SpeedPercent(10), inToRotations(-3))
motorD.on_for_seconds(SpeedPercent(8), 1.6)
# Push it down fully
tank_drive.on_for_rotations(SpeedPercent(12), SpeedPercent(12), inToRotations(1.5))
motorD.on_for_seconds(SpeedPercent(-15), 1.5)
# Turn left 90°

# Go forward a bit

# Turn right