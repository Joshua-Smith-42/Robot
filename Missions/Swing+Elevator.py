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
mt.on_for_rotations(SpeedPercent(-15), SpeedPercent(-15), 0.45) # ROBOT MOVES BACK INTO WALL
mt.on_for_rotations(SpeedPercent(30), SpeedPercent(30), 1.8) #ROBOT MOVES FORWARD TO ELEVATOR
mt.on_for_rotations(SpeedPercent(30), SpeedPercent(0), 1) #ROBOT TURNS CLOCKWISE TO FACE ELEVATOR
mt.on_for_rotations(SpeedPercent(30), SpeedPercent(30), 1.25) #ROBOT MOVES FORWARD AND HITS ELEVATOR
motorA.on_for_degrees(SpeedPercent(15), 200)#MEDIUM MOTOR TURNS AWAY SO IT DOESENT UNDO ELEVATOR
mt.on_for_rotations(SpeedPercent(0), SpeedPercent(-30), 0.8)#ROBOT TURNS TO SAFETY FACTOR
mt.on_for_rotations(SpeedPercent(15), SpeedPercent(15), 1.13)#ROBOT MOVES INTO SAFETY FACTOR
mt.on_for_rotations(SpeedPercent(10), SpeedPercent(-10), 0.2)#ROBOT TURNS TO KNOCK DOWN BEAMS
mt.on_for_rotations(SpeedPercent(-15), SpeedPercent(-15), 0.1) # ROBOT MOVES BACK INTO WALL
mt.on_for_rotations(SpeedPercent(-10), SpeedPercent(10), 0.5)#ROBOT TURNS TO KNOCK DOWN BEAMS
mt.on_for_rotations(SpeedPercent(-30), SpeedPercent(0), 0.1) #ROBOT TURNS BACK TO BASE
mt.on_for_rotations(SpeedPercent(-60), SpeedPercent(-60), 12) # ROBOT MOVES BACK TO BASE
