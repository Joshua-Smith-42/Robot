#!/usr/bin/env python3

# FLL 42, Pythonian Rabbotics's master program. Copyright (c) 2019 FLL team 42

#---------------------------------------------------Imports and variable definitions-----------------------------------------------------------------
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
gyro = GyroSensor(INPUT_1)
Sound_ = Sound()
Display_ = Display()
Sound_.play_tone(frequency=400, duration=0.5, volume=50) #plays a note so we know when the code starts
#---------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------Distance conversion--------------------------------------------------------------------------------
wheelDiameter_mm = 56 # Look at the first number on the NUMBERxNUMBER on wheel
wheelCircumference_cm = (wheelDiameter_mm/10) * 3.14159265358979323846284338 # Convert to cm and multiply by pi for circumference
wheelCircumference_in = (wheelDiameter_mm/25.4) * 3.14159265358979323846284338 # Convert to in and multiply by pi for circumference
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
def cmToMillimeters(cm): #hhm it works... questionable -- no syntax errors!
    return cm * 10 # Yay, no syntax errors!
def drive_cm(power, cm):
    rt = cmToRotations(cm)
    tank_drive.on_for_rotations(SpeedPercent(power), SpeedPercent(power), int(rt) )
def drive_cm_new(power, cm):
    rt = cmToRotations(cm)
    tank_drive.on_for_rotations(SpeedPercent(power), SpeedPercent(power), rt)
#---------------------------------------------------------------------------------------------------------------------------------------------

def gyroTurn(deg, speedL, speedR):
    startAng = gyro.angle
    if deg >= 0:
        while (gyro.angle-startAng) <= deg:
            tank_drive.on(SpeedPercent(speedL), SpeedPercent(speedR))
    if deg < 0:
        while (gyro.angle-startAng) >= deg:
            tank_drive.on(SpeedPercent(speedL), SpeedPercent(speedR))
    tank_drive.off()
    #------------------------------------GyroStraight------------------------------------------------------------------------------------------------------#
def gyroStraight(rotations):
    startAng = gyro.angle
    if deg >= 0:
        while (gyro.angle-startAng) <= deg:
            tank_drive.on_for_rotations(SpeedPercent(30), SpeedPercent(40),int(rotations) )
    if deg < 0:
        while (gyro.angle-startAng) <= deg:
            tank_drive.on_for_rotations(SpeedPercent(40), SpeedPercent(30),int(rotations) )
    tank_drive.off()

#------------------------Small D&B--------------------------------------------------------------------------------
drive_cm_new(50,45) # forward
gyroTurn(-26,0,50) # turn toward tan
drive_cm_new(50,75) # wheeeeee
drive_cm_new(50,-46) # drop tan
motorD.on_for_degrees(25,80) # opens gate
drive_cm_new(50, -10) # go back (was -5) 
gyroTurn(35,50,0) # turn
drive_cm_new(70,-110) # back to home sweet home