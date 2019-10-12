#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import GyroSensor
color = ColorSensor(INPUT_1)
gyro = GyroSensor(INPUT_3)
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)  #This is the template whenever we code

tank_drive.on_for_seconds(SpeedPercent(40), SpeedPercent(40), 2) #move robot forward and backward to do swing
tank_drive.on_for_seconds(SpeedPercent(-40), SpeedPercent(-40), 2)
tank_drive.on_for_rotations(SpeedPercent(0), SpeedPercent(50), 3) #Turn Robot to elevator
