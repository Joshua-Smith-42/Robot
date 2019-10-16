#!/usr/bin/env python3
from DistanceConversion import *
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4, ColorSensor, GyroSensor
m0veTank = MoveTank(OUTPUT_B, OUTPUT_C)
m0veTank.on_for_rotations(SpeedPercent(50), SpeedPercent(50), cmToRotations(115))
m0veTank.on_for_rotations(SpeedPercent(75), SpeedPercent(75), cmToRotations(8))
m0veTank.on_for_rotations(SpeedPercent(-30), SpeedPercent(-30), cmToRotations(8))
    
