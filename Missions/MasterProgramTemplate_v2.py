#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from ev3dev2.display import Display
import time
import sys
btn = Button()
color = ColorSensor(INPUT_4)
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)  #This is the template whenever we code
motorA = MediumMotor(OUTPUT_A)
motorD = MediumMotor(OUTPUT_D)
Sound_ = Sound()
Display_ = Display()
Sound_.play_tone(frequency=400, duration=0.5, volume=50) #plays a note so we know when the code starts

#yellow = forwards
def swing_and_safety():
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    motorA = MediumMotor(OUTPUT_A)
    motorD = MediumMotor(OUTPUT_D)
    tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 6.67) #ROBOT MOVES FORWARD FROM BASE
    tank_drive.on_for_rotations(SpeedPercent(20), SpeedPercent(20), .8) # ROBOT MOVES INTO SWING
    tank_drive.on_for_rotations(SpeedPercent(-30), SpeedPercent(-30), 0.4) #ROBOT MOVES AWAY FROM SWING
    tank_drive.on_for_rotations(SpeedPercent(-30), SpeedPercent(0), 1.5) #ROBOT TURNS TO SQUARE ON WALL
    motorA.on_for_degrees(SpeedPercent(15), 150) #LEFT ARM TURNS FOR ELEVATOR
    tank_drive.on_for_rotations(SpeedPercent(-15), SpeedPercent(-15), 0.45) # ROBOT MOVES BACK INTO WALL
    tank_drive.on_for_rotations(SpeedPercent(30), SpeedPercent(30), 1.8) #ROBOT MOVES FORWARD TO ELEVATOR
    tank_drive.on_for_rotations(SpeedPercent(30), SpeedPercent(0), 1) #ROBOT TURNS CLOCKWISE TO FACE ELEVATOR
    tank_drive.on_for_rotations(SpeedPercent(30), SpeedPercent(30), 1.25) #ROBOT MOVES FORWARD AND HITS ELEVATOR
    motorA.on_for_degrees(SpeedPercent(15), 200)#MEDIUM MOTOR TURNS AWAY SO IT DOESENT UNDO ELEVATOR
    tank_drive.on_for_rotations(SpeedPercent(0), SpeedPercent(-30), 0.8)#ROBOT TURNS TO SAFETY FACTOR
    tank_drive.on_for_rotations(SpeedPercent(15), SpeedPercent(15), 1.13)#ROBOT MOVES INTO SAFETY FACTOR
    tank_drive.on_for_rotations(SpeedPercent(10), SpeedPercent(-10), 0.2)#ROBOT TURNS TO KNOCK DOWN BEAMS
    tank_drive.on_for_rotations(SpeedPercent(-15), SpeedPercent(-15), 0.3) # ROBOT MOVES BACK TO NOT KNOCK DOWN THE BUILDING IN SAFETY FACTOR
    tank_drive.on_for_rotations(SpeedPercent(-10), SpeedPercent(10), 0.5)#ROBOT TURNS TO KNOCK DOWN BEAMS
    tank_drive.on_for_rotations(SpeedPercent(-60), SpeedPercent(-60), 12) # ROBOT MOVES BACK TO BASE


#blue = turn *
def crane():
    tank_drive.on_for_rotations(SpeedPercent(35), SpeedPercent(35), inToRotations(27))
    tank_drive.on_for_rotations(SpeedPercent(20), SpeedPercent(20), inToRotations(-5))
    tank_drive.on_for_seconds(SpeedPercent(10), SpeedPercent(20), 2.5)
    tank_drive.on_for_rotations(SpeedPercent(20), SpeedPercent(20), inToRotations(3))
    tank_drive.on_for_seconds(SpeedPercent(10), SpeedPercent(7), 1.5)

def design_and_build_one():
    #go forward
    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), 360)
    #turn right
    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(0), 545)
    #move forward
    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), 1322)
    #turn left
    tank_drive.on_for_degrees(SpeedPercent(0), SpeedPercent(50), 253)
    #go forward
    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), 669)
    #go backward after leaving tan load, dropping off red load
    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), -726)
    #turn 
    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(0), 839)
    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), 600)
    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(0), 510)

wheelDiameter_mm = 56
wheelCircumference_cm = (wheelDiameter_mm/10) * 3.14159265358979323846284338
wheelCircumference_in = (wheelDiameter_mm/25.4) * 3.14159265358979323846284338

def inToRotations(inches):
    return inches/wheelCircumference_in

def cmToRotations(cm):
    return cm/wheelCircumference_cm

def inToMillimeters(inches):
    return inches * 25.4

def cmToMillimeters(cm):
    return cm * 10

def drive_cm(power, cm):
    rt = cmToRotations(cm)
    tank_drive.on_for_rotations(SpeedPercent(power), SpeedPercent(power), int(rt) )

def big_design_and_build():
    drive_cm(50, 65)
    tank_drive.on_for_seconds(SpeedPercent(-10), SpeedPercent(-50), 2)
    drive_cm(-20, 65)

#defining what "ColorChecking" is
def ColorChecking():
    if color.color == color.COLOR_YELLOW: #if yellow
        swing_and_safety()
    elif color.color == color.COLOR_GREEN: #if green
        big_design_and_build()
    elif color.color == color.COLOR_RED: #if red
        design_and_build_one()
    elif color.color == color.COLOR_BLUE: #if blue
        crane()

def failsafe():
    sys.exit()

#This is where the movement happens. the function "ColorChecking" is a function to decide what to do based on color.

#not whenever we touch enter (or the mibble button) then it will call ColorChecking(). Not just when this line happens
Sound_.play_tone(frequency=400, duration=0.5, volume=50)
start = time.time()
btn.on_backspace = failsafe

while True: #this code essentially color checks for 30 seconds
    if (btn.down):
        break
    pass
    btn.wait_for_released('right')
    ColorChecking()
#hello
#
Sound_.play_tone(frequency=400, duration=0.5, volume=50)