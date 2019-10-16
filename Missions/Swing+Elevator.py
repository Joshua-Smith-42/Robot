#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from time import sleep
mt = MoveTank(OUTPUT_B, OUTPUT_C)
mt.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 6.67)
mt.on_for_rotations(SpeedPercent(20), SpeedPercent(20), .8)
mt.on_for_rotations(SpeedPercent(-30), SpeedPercent(-30), 0.4)
mt.on_for_rotations(SpeedPercent(-30), SpeedPercent(0), 1.5)
mt.on_for_rotations(SpeedPercent(-40), SpeedPercent(-40), .5)
mt.on_for_rotations(SpeedPercent(30), SpeedPercent(30), 1.8)
mt.on_for_rotations(SpeedPercent(30), SpeedPercent(0), 1)
mt.on_for_rotations(SpeedPercent(30), SpeedPercent(30), 1)