#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, GyroSensor

gyro = GyroSensor(INPUT_1)

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

mt = MoveTank(OUTPUT_B, OUTPUT_C)

def gyroTurn(deg, speedL, speedR):
    startAng = gyro.angle
    if deg >= 0:
        while (gyro.angle-startAng) <= deg:
            mt.on(SpeedPercent(speedL), SpeedPercent(speedR))
    if deg < 0:
        while (gyro.angle-startAng) >= deg:
            mt.on(SpeedPercent(speedL), SpeedPercent(speedR))
    mt.off()

#go forward
mt.on_for_rotations(SpeedPercent(50), SpeedPercent(50), cmToRotations(17.5929188601))
#turn right
#mt.on_for_rotations(SpeedPercent(50), SpeedPercent(0), cmToRotations(26.633724385429165))
gyroTurn(75, 50, 0)
#move forward
mt.on_for_rotations(SpeedPercent(50), SpeedPercent(50), cmToRotations(64.60510759181166))
#turn left
#mt.on_for_degrees(SpeedPercent(0), SpeedPercent(50), 253)
gyroTurn(-11, 0, 40)
#go forward
mt.on_for_degrees(SpeedPercent(50), SpeedPercent(50), 669)
# turn slightly left to target red
gyroTurn(-2, 10, 20)
#go backward after leaving tan load, dropping off red load
mt.on_for_degrees(SpeedPercent(50), SpeedPercent(50), -726)
#turn 
mt.on_for_degrees(SpeedPercent(50), SpeedPercent(0), -350)
mt.on_for_degrees(SpeedPercent(50), SpeedPercent(50), -600)
mt.on_for_degrees(SpeedPercent(50), SpeedPercent(50), 843)
mt.on_for_degrees(SpeedPercent(0), SpeedPercent(50), 450)
