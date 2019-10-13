#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor

mt = MoveTank(OUTPUT_B, OUTPUT_C)

#go forward
mt.on_for_degrees(SpeedPercent(50), SpeedPercent(50), 405)
#turn right
mt.on_for_degrees(SpeedPercent(50), SpeedPercent(0), 496)
#move forward
mt.on_for_degrees(SpeedPercent(50), SpeedPercent(50), 1322)
#turn left
mt.on_for_degrees(SpeedPercent(0), SpeedPercent(50), 253)
#go forward
mt.on_for_degrees(SpeedPercent(50), SpeedPercent(50), 669)
#go backward after leaving tan load
mt.on_for_degrees(SpeedPercent(50), SpeedPercent(50), -726)
#turn 
mt.on_for_degrees(SpeedPercent(50), SpeedPercent(0), 137)
mt.on_for_degrees(SpeedPercent(0), SpeedPercent(50), 852)
mt.on_for_degrees(SpeedPercent(50), SpeedPercent(50), 2000)
