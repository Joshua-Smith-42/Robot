#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
mt = MoveTank(OUTPUT_B, OUTPUT_C)
motorA = MediumMotor(OUTPUT_A)
motorD = MediumMotor(OUTPUT_D)
mt.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 6.67) #ROBOT MOVES FORWARD FROM BASE
mt.on_for_rotations(SpeedPercent(20), SpeedPercent(20), .8) # ROBOT MOVES INTO SWING
mt.on_for_rotations(SpeedPercent(-30), SpeedPercent(-30), 0.4) #ROBOT MOVES AWAY FROM SWING
mt.on_for_rotations(SpeedPercent(-30), SpeedPercent(0), 1.5) #ROBOT TURNS TO SQUARE ON WALL
motorA.on_for_degrees(SpeedPercent(15), 150) #LEFT ARM TURNS FOR ELEVATOR
mt.on_for_rotations(SpeedPercent(-15), SpeedPercent(-15), 0.3) # ROBOT MOVES BACK INTO WALL
mt.on_for_rotations(SpeedPercent(30), SpeedPercent(30), 1.8) 
mt.on_for_rotations(SpeedPercent(30), SpeedPercent(0), 1) #
mt.on_for_rotations(SpeedPercent(30), SpeedPercent(30), 1.25) 
motorA.on_for_degrees(SpeedPercent(15), 50)
motorA.on_for_degrees(SpeedPercent(15), 150)
mt.on_for_rotations(SpeedPercent(0), SpeedPercent(-30), 0.8)
mt.on_for_rotations(SpeedPercent(15), SpeedPercent(15), 1.05)
mt.on_for_rotations(SpeedPercent(-10), SpeedPercent(10), 0.25)
mt.on_for_rotations(SpeedPercent(-30), SpeedPercent(0), 0.5) 
mt.on_for_rotations(SpeedPercent(-30), SpeedPercent(-30), 10) 
