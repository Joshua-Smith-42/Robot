#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
mt = MoveTank(OUTPUT_B, OUTPUT_C)
motorA = MediumMotor(OUTPUT_A)
mt.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 6.67)
mt.on_for_rotations(SpeedPercent(20), SpeedPercent(20), .8)
mt.on_for_rotations(SpeedPercent(-30), SpeedPercent(-30), 0.4)
mt.on_for_rotations(SpeedPercent(-30), SpeedPercent(0), 1.5)
motorA.on_for_degrees(SpeedPercent(15), 150)
mt.on_for_rotations(SpeedPercent(-40), SpeedPercent(-40), 1.2)
mt.on_for_rotations(SpeedPercent(30), SpeedPercent(30), 1.8)
mt.on_for_rotations(SpeedPercent(30), SpeedPercent(0), 1)
mt.on_for_rotations(SpeedPercent(30), SpeedPercent(30), 1.25)
motorA.on_for_degrees(SpeedPercent(15), 50)
mt.on_for_rotations(SpeedPercent(0), SpeedPercent(-30), 0.8)
mt.on_for_rotations(SpeedPercent(30), SpeedPercent(30), 1.2)
mt.on_for_rotations(SpeedPercent(-30), SpeedPercent(30), 0.15)