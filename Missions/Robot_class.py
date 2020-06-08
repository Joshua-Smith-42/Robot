#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4, ColorSensor, GyroSensor
from ev3dev2.sensor.lego import ColorSensor, GyroSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from ev3dev2.display import Display
import time
import sys



class Robot():
    colorR = ColorSensor(INPUT_2)
    colorL = ColorSensor(INPUT_3)
    color = ColorSensor(INPUT_4)
    gyro = GyroSensor(INPUT_1)
    tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)
    motorA = MediumMotor(OUTPUT_A)
    motorD = MediumMotor(OUTPUT_D)
    btn = Button()
    Sound_ = Sound()
    Display_ = Display()
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

        def squareOnLine(speed):
            while not (colorL.color == colorL.COLOR_BLACK and colorR.color == colorR.COLOR_BLACK):
                tank_drive.on(speed, speed)
            tank_drive.off()

    class Missions():
        class d_And_B():
            def big():
                Robot.Move.drive_cm(50, 65)#pushes building to black circle
                Robot.Move.drive_cm(-50, 65)#back to home

            def small():
                drive_cm_new(50,45) # forward
                gyroTurn(-26,0,50) # turn toward tan
                drive_cm_new(50,75) # wheeeeee
                drive_cm_new(50,-46) # drop tan
                motorD.on_for_degrees(25,80) # opens gate
                drive_cm_new(50, -10) # go back
                gyroTurn(35,50,0) # turn
                drive_cm_new(70,-110) # back to home sweet home


        def craneAndWabbit():
            Robot.Move.drive_cm(50,40)#drives Wabbit out
            Robot.Move.drive_cm(50,-21) #drops off wabbit
            Robot.Move.gyroTurn(-39, 0 ,50)#turns toward crane
            Robot.Move.drive_cm(35,30) #drops crane
            Robot.Move.drive_cm(50,-51)#backs away from crane
            Robot.Move.gyroTurn(90, 50,0)#turns away from home
            Robot.Move.drive_cm(50,-50)#backs up to home

        def bridge():
            drive_cm(65,-127.5) # 65% speed -- fast whoosh (was -126)
            gyroTurn(-90,-15,15)
            drive_cm(60,30) # square
            drive_cm(30,-20) # go back
            gyroTurn(-20,-15,15)
            drive_cm(30,-119) # drive up bridge
            tank_drive.off() # stall drivetrain
            while True:
                if (btn.enter):
                    tank_drive.off(brake=False) # Unstall motors
                    break
                

        

        