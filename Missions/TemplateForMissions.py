#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4, ColorSensor, GyroSensor
m0vetank = MoveTank(OUTPUT_B, OUTPUT_C)
wheelCircumference_cm = 5.6 * 3.14159265358979323846284338
def cmToRotations(cm):
    return cm/wheelCircumference_cm



