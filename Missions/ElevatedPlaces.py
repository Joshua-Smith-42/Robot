#!/usr/bin/env python3

# FLL 42 - Elevated Places mission

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
colorL = ColorSensor(INPUT_2)
colorR = ColorSensor(INPUT_3)
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)  #This is the template whenever we code
motorA = MediumMotor(OUTPUT_A)
motorD = MediumMotor(OUTPUT_D)
gyro = GyroSensor(INPUT_1)
Sound_ = Sound()
Display_ = Display()
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
def cmToMillimeters(cm): #hhm it works... questionable -- no syntax errors!
    return cm * 10 # Yay, no syntax errors!
def drive_cm(power, cm):
    rt = cmToRotations(cm)
    tank_drive.on_for_rotations(SpeedPercent(power), SpeedPercent(power), rt )
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

def squareOnLine(speed):
    while not (colorL.color == colorL.COLOR_BLACK and colorR.color == colorR.COLOR_BLACK):
        tank_drive.on(speed, speed)
    tank_drive.off()

def elevatedPlaces():
    Sound_.play_tone(frequency=400, duration=0.5, volume=50) #plays a note so we know when the code starts
    # drive_cm(65,121) # 65% speed -- fast whoosh
    # gyroTurn(-90,-15,15)
    # drive_cm(50,-20)
    # drive_cm(25,15)
    # gyroTurn(-25,-25,25)
    # # gyroTurn(-112,-25,25) # turn left
    # # drive_cm(50,48) # get away from misleading black
    # squareOnLine(50)
    # drive_cm(20,46) # drive up bridge
    # tank_drive.off() # stall drivetrain
    # while True:
    #     if (btn.enter):
    #         tank_drive.off(brake=False) # Unstall motors
    #         break
    #     time.sleep(0.25)
    drive_cm(65,-126) # 65% speed -- fast whoosh
    gyroTurn(-90,-15,15)
    drive_cm(50,30) # square
    drive_cm(25,-15)
    gyroTurn(-19,-25,25) # was -17
    # gyroTurn(-112,-25,25) # turn left
    # drive_cm(50,48) # get away from misleading black
    # squareOnLine(-50)
    drive_cm(30,-119) # drive up bridge (was 20, -46) then (30, -90) them (30, -113)
    tank_drive.off() # stall drivetrain
    while True:
        if (btn.enter):
            tank_drive.off(brake=False) # Unstall motors
            break
        time.sleep(0.25)

elevatedPlaces()
