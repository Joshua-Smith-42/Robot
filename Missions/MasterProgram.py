#!/usr/bin/env python3

#---------------------------------------------------Imports and variable definitions-----------------------------------------------------------------
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from ev3dev2.display import Display
import time
btn = Button()
color = ColorSensor(INPUT_4)
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)  #This is the template whenever we code
Sound_ = Sound()
Display_ = Display()
Sound_.play_tone(frequency=400, duration=0.5, volume=50) #plays a note so we know when the code starts
motorA = MediumMotor(OUTPUT_A)
motorD = MediumMotor(OUTPUT_D)
#---------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------Distance conversion--------------------------------------------------------------------------------
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
    return cm * 10 # Yay, no syntax errors!
#--------------------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------yellow = swing and safety by Alan and Kunal--------------------------------------------------------------------
def swing_and_safety():
    tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 6.67) #ROBOT MOVES FORWARD FROM BASE
    tank_drive.on_for_rotations(SpeedPercent(20), SpeedPercent(20), .8) # ROBOT MOVES INTO SWING
    tank_drive.on_for_rotations(SpeedPercent(-30), SpeedPercent(-30), 0.4) #ROBOT MOVES AWAY FROM SWING
    tank_drive.on_for_rotations(SpeedPercent(-30), SpeedPercent(0), 1.5) #ROBOT TURNS TO SQUARE ON WALL
    motorA.on_for_degrees(SpeedPercent(15), 150) #LEFT ARM TURNS FOR ELEVATOR
    tank_drive.on_for_rotations(SpeedPercent(-15), SpeedPercent(-15), 0.3) # ROBOT MOVES BACK INTO WALL
    tank_drive.on_for_rotations(SpeedPercent(30), SpeedPercent(30), 1.8) 
    tank_drive.on_for_rotations(SpeedPercent(30), SpeedPercent(0), 1) #
    tank_drive.on_for_rotations(SpeedPercent(30), SpeedPercent(30), 1.25) 
    motorA.on_for_degrees(SpeedPercent(15), 50)
    motorA.on_for_degrees(SpeedPercent(15), 150)
    tank_drive.on_for_rotations(SpeedPercent(0), SpeedPercent(-30), 0.8)
    tank_drive.on_for_rotations(SpeedPercent(15), SpeedPercent(15), 1.05)
    tank_drive.on_for_rotations(SpeedPercent(-10), SpeedPercent(10), 0.25)
    tank_drive.on_for_rotations(SpeedPercent(-30), SpeedPercent(0), 0.5) 
    tank_drive.on_for_rotations(SpeedPercent(-30), SpeedPercent(-30), 10) 
#--------------------------------------------------------------------------------------------------------------------------------------------------

#green = backwards
def green():
    tank_drive.on_for_rotations(SpeedPercent(-50), SpeedPercent(-50), 1)

#red = turn *
def red():
    tank_drive.on_for_rotations(SpeedPercent(0), SpeedPercent(50), 1)

#----------------------------------------blue = crane by Ben and Joshua *----------------------------------------------------------------
def crane():
    # 22 1/4 in forward
    tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), inToRotations(22.25))
    # Move attachment down
    motorD.on_for_seconds(SpeedPercent(-8), 1.8)
    # Drive forward a bit
    tank_drive.on_for_seconds(SpeedPercent(20), SpeedPercent(15), 0.3)
    tank_drive.on_for_rotations(SpeedPercent(10), SpeedPercent(10), inToRotations(2.5)) 
    tank_drive.on_for_seconds(SpeedPercent(21), SpeedPercent(17), 0.1)
    tank_drive.on_for_rotations(SpeedPercent(10), SpeedPercent(10), inToRotations(2.25))
    # Drive back a bit
    tank_drive.on_for_rotations(SpeedPercent(10), SpeedPercent(10), inToRotations(-3))
    motorD.on_for_seconds(SpeedPercent(8), 1.6)
    # Push it down fully
    tank_drive.on_for_rotations(SpeedPercent(12), SpeedPercent(12), inToRotations(1.5))
    motorD.on_for_seconds(SpeedPercent(-15), 1.5)
#-----------------------------------------------------------------------------------------------------------------------------------------

#-----------------------------------------definning what "ColorChecking" is---------------------------------------------------------------
def ColorChecking():
    if color.color == color.COLOR_YELLOW: #if yellow
        swing_and_safety()
    elif color.color == color.COLOR_GREEN: #if green
        green()
    elif color.color == color.COLOR_RED: #if red
        red()
    elif color.color == color.COLOR_BLUE: #if blue
        crane()
#-----------------------------------------------------------------------------------------------------------------------------------------

#This is where the movement happens. the function "ColorChecking" is a function to decide what to do based on color.

#now whenever we touch enter (or the mibble button) then it will call ColorChecking().
Sound_.play_tone(frequency=400, duration=0.5, volume=50)
start = time.time()

while (time.time() - start) <= 160: #this code essentially waits the duration of the match
    pass
    btn.wait_for_released('right')
    ColorChecking()

Sound_.play_tone(frequency=400, duration=0.5, volume=50)