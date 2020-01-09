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



#-----------------------------------yellow = swing and safety by Alan and Kunal---------------------------------------------------------------
def swing_and_safety():

    motorD.stop_action = motorD.STOP_ACTION_HOLD
    motorD.stop() # stall right motor

    tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 6.67) #ROBOT MOVES FORWARD FROM BASE
    tank_drive.on_for_rotations(SpeedPercent(20), SpeedPercent(20), .8) # ROBOT MOVES INTO SWING
    tank_drive.on_for_rotations(SpeedPercent(-30), SpeedPercent(-30), 0.4) #ROBOT MOVES AWAY FROM SWING

    motorD.stop_action = motorD.STOP_ACTION_COAST
    motorD.stop() # unstall right motor

    tank_drive.on_for_rotations(SpeedPercent(-30), SpeedPercent(0), 1.5) #ROBOT TURNS TO SQUARE ON WALL
    motorA.on_for_degrees(SpeedPercent(15), 150) #LEFT ARM TURNS FOR ELEVATOR
    tank_drive.on_for_rotations(SpeedPercent(-15), SpeedPercent(-15), 0.666666666666666666) # ROBOT MOVES BACK INTO WALL
    tank_drive.on_for_rotations(SpeedPercent(30), SpeedPercent(30), 1.8) #ROBOT MOVES FORWARD TO ELEVATOR
    tank_drive.on_for_rotations(SpeedPercent(30), SpeedPercent(0), 1) #ROBOT TURNS CLOCKWISE TO FACE ELEVATOR
    tank_drive.on_for_rotations(SpeedPercent(30), SpeedPercent(30), 1.25) #ROBOT MOVES FORWARD AND HITS ELEVATOR
    motorA.on_for_degrees(SpeedPercent(15), 200)#MEDIUM MOTOR TURNS AWAY SO IT DOESN'T UNDO ELEVATOR
    tank_drive.on_for_rotations(SpeedPercent(0), SpeedPercent(-30), 0.72000003141596253589)#ROBOT TURNS TO SAFETY FACTOR
    tank_drive.on_for_rotations(SpeedPercent(15), SpeedPercent(15), 1.03)#ROBOT MOVES INTO SAFETY FACTOR
    tank_drive.on_for_rotations(SpeedPercent(10), SpeedPercent(-10), 0.3)#ROBOT TURNS TO KNOCK DOWN BEAMS
    tank_drive.on_for_rotations(SpeedPercent(-15), SpeedPercent(-15), 0.3) # ROBOT MOVES BACK TO NOT KNOCK DOWN THE BUILDING IN SAFETY FACTOR
    tank_drive.on_for_rotations(SpeedPercent(-10), SpeedPercent(10), 0.5)#ROBOT TURNS TO KNOCK DOWN BEAMS
    tank_drive.on_for_rotations(SpeedPercent(-60), SpeedPercent(-60), 12) # ROBOT MOVES BACK TO BASE
    motorA.stop_action = motorA.STOP_ACTION_COAST
    motorA.stop() # unstall left motor
#------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------- Big Design and Build is green ----------------------------------------------------------

def big_design_and_build():
    drive_cm(50, 65)
    tank_drive.on_for_seconds(SpeedPercent(-10), SpeedPercent(-50), 2)
    drive_cm(-20, 65)

#--------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------ red = Design & Build 1 --------------------------------------------------------

def design_and_build_one():
    # #go forward
    # tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), cmToRotations(17)) # was 17.5929188601
    # #turn right
    # gyroTurn(75, 50, 0)
    # #move forward
    # tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), cmToRotations(64.60510759181166))
    # #turn left
    # #tank_drive.on_for_degrees(SpeedPercent(0), SpeedPercent(50), 253)
    # gyroTurn(-16, 0, 40) # was -15 was -14 orig -13
    # #go forward
    # tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), 700) # was 669
    # # turn slightly left to target red
    # #gyroTurn(3, 20, 10) # was #gyroTurn(-2,10,20)
    # #go backward after leaving tan load, dropping off red load
    # tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), -729)
    # #turn 
    # tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(0), -350)
    # tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), -800)
    # tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), 843)
    # tank_drive.on_for_degrees(SpeedPercent(0), SpeedPercent(50), 450)
    # tank_drive.on_for_degrees(25,25,75)

    #go forward
    tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), cmToRotations(16)) # was 17.5929188601
    #turn right
    gyroTurn(80, 27, -27)
    #move forward
    tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), cmToRotations(64.60510759181166))
    #turn left
    #tank_drive.on_for_degrees(SpeedPercent(0), SpeedPercent(50), 253)
    gyroTurn(-15, -40, 40) # was -15 was -14 orig -13
    #go forward
    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), 850) # was 669
    # turn slightly left to target red
    #gyroTurn(3, 20, 10) # was #gyroTurn(-2,10,20)
    #go backward after leaving tan load, dropping off red load
    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), -729)
    #turn 
    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(0), -350)
    tank_drive.on_for_degrees(SpeedPercent(30), SpeedPercent(30), -800)
    tank_drive.on_for_degrees(SpeedPercent(50), SpeedPercent(50), 843)
    tank_drive.on_for_degrees(SpeedPercent(0), SpeedPercent(50), 450)
    tank_drive.on_for_degrees(25,25,75)


#--------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------blue = crane & innovative architecture by Yash and Alan--------------------------------------------------------------------
def crane():
    drive_cm_new(50,42)
    drive_cm_new(50,-23) #drops off wabbit
    gyroTurn(-39, 0 ,50)
    drive_cm_new(35,30) #drops crane
    drive_cm_new(50,-51)
    gyroTurn(90, 50,0)
    drive_cm_new(70,-60)
#--------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------black = Elevated Places/Bridge - Ben & Joshua-------------------------------------------------------------
def elevated_places():
    drive_cm_new(65,-127.5) # 65% speed -- fast whoosh (was -126)
    gyroTurn(-90,-15,15)
    drive_cm_new(60,30) # square
    drive_cm_new(30,-20) # go back (was -18)
    gyroTurn(-20,-15,15) # was -19
    drive_cm_new(30,-119) # drive up bridge (was 20, -46) then (30, -90) them (30, -113)
    tank_drive.off() # stall drivetrain
    while True:
        if (btn.enter):
            tank_drive.off(brake=False) # Unstall motors
            break
        time.sleep(0.25)
#--------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------- creating the function ColorChecking ---------------------------------------------------------------
def ColorChecking():
    if color.color == color.COLOR_YELLOW: #if yellow
        swing_and_safety()
    elif color.color == color.COLOR_GREEN: #if green
        big_design_and_build()
    elif color.color == color.COLOR_RED: #if red
        design_and_build_one()
    elif color.color == color.COLOR_BLUE: #if blue
        crane()
    elif color.color == color.COLOR_BLACK: # if black
        elevated_places()
#--------------------------------------------------------------------------------------------------------------------------------------------

#This is where the movement happens. the function "ColorChecking" is a function to decide what to do based on color.

#--------------- failsafe -------------
def failsafe():
    sys.exit()
#--------------------------------------

#now whenever we touch enter (or the middle button) then it will call ColorChecking().
Sound_.play_tone(frequency=400, duration=0.5, volume=50)
start = time.time()
btn.on_backspace = failsafe

while True: #this code essentially color checks forever
    if (btn.down):
        break
    pass
    btn.wait_for_released('enter')
    ColorChecking()

# Beepity beep!
Sound_.play_tone(frequency=400, duration=0.5, volume=50)