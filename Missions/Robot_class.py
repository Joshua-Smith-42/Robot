#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4, ColorSensor, GyroSensor
from time import sleep
colorR = ColorSensor(INPUT_2)
colorL = ColorSensor(INPUT_3)
color = ColorSensor(INPUT_4)
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
motorD = MediumMotor(OUTPUT_D)



class Robot():
    class Conversions():
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

    class Move():
        def drive_cm(power, cm):
            rt = Robot.Conversions.cmToRotations(cm)
            tank_drive.on_for_rotations(SpeedPercent(power), SpeedPercent(power), float(rt) )

        def gyroTurn(degeres, speedL, speedR):
            startAng = gyro.angle
            if degeres >= 0:
                while (gyro.angle-startAng) <= degeres:
                    tank_drive.on(SpeedPercent(speedL), SpeedPercent(speedR))
            if degeres < 0:
                while (gyro.angle-startAng) >= degeres:
                    tank_drive.on(SpeedPercent(speedL), SpeedPercent(speedR))
            tank_drive.off()

    class Missions():
        def big_D_And_B():
            Robot.Move.drive_cm(50, 65)#pushes building to black circle
            Robot.Move.drive_cm(-50, 65)#back to home

        def crane_and_wabbit():
            Robot.Move.drive_cm(50,40)#drives Wabbit out
            Robot.Move.drive_cm(50,-21) #drops off wabbit
            Robot.Move.gyroTurn(-39, 0 ,50)#turns toward crane
            Robot.Move.drive_cm(35,30) #drops crane
            Robot.Move.drive_cm(50,-51)#backs away from crane
            Robot.Move.gyroTurn(90, 50,0)#turns away from home
            Robot.Move.drive_cm(50,-50)#backs up to home

        