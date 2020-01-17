#!/usr/bin/env python3
#^^^^This line is required to tell the EV3 to run this file using Python|it is called a shebang line|it MUST be on the first line

# FLL 42, Pythonian Rabbotics's master program.

#---------------------------------------------------Imports and variable definitions-----------------------------------------------------------------
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor#gives us accses to everything we need to run EV3 dev
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from ev3dev2.display import Display
import time
import sys
btn = Button() # variable so we can get buttons pressed on EV3
color = ColorSensor(INPUT_4) # color sensor for checking attachment color
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)  # Creates a variable so we can control the drivetrain
motorA = MediumMotor(OUTPUT_A) # left medium motor
motorD = MediumMotor(OUTPUT_D) # right medium motor
gyro = GyroSensor(INPUT_1) # gyro variable
Sound_ = Sound() # beepity beep
Display_ = Display() # for displaying text
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
def cmToMillimeters(cm):
    return cm * 10 
def drive_cm(power, cm, brake=False):#when you call this you tell it how many centimeters to dive and it drives that far how ever we discovered
    #that it didn't work right
    rt = cmToRotations(cm)
    tank_drive.on_for_rotations(SpeedPercent(power), SpeedPercent(power), int(rt), brake=brake)
def drive_cm_new(power, cm, brake=False):#so instead of changing that one (and then all our code) we made this one so now we can use this more correct version
    rt = cmToRotations(cm)
    tank_drive.on_for_rotations(SpeedPercent(power), SpeedPercent(power), rt, brake=brake)
#---------------------------------------------------------------------------------------------------------------------------------------------

def gyroTurn(deg, speedL, speedR):
    startAng = gyro.angle # get current gyro angle
    if deg >= 0: # if we're turning right,
        while (gyro.angle-startAng) <= deg: # while the current turned angle is less than the angle we want to turn to,
            tank_drive.on(SpeedPercent(speedL), SpeedPercent(speedR)) # turn
    if deg < 0: # if we're turning left, 
        while (gyro.angle-startAng) >= deg: # while the current turned angle is greater than the angle we want to turn to,
            tank_drive.on(SpeedPercent(speedL), SpeedPercent(speedR)) # turn
    tank_drive.off() # stop turning at the end
#------------------------------------GyroStraight------------------------------------------------------------------------------------------------------#
def gyroStraight(rotations):#WARNING THIS DOENT WORK DO NOT PUT IT IN ROBOT NOTEBOOK
    startAng = gyro.angle
    if deg >= 0:
        while (gyro.angle-startAng) <= deg:
            tank_drive.on_for_rotations(SpeedPercent(30), SpeedPercent(40), rotations)
    if deg < 0:
        while (gyro.angle-startAng) <= deg:
            tank_drive.on_for_rotations(SpeedPercent(40), SpeedPercent(30), rotations)
    tank_drive.off()



#-----------------------------------yellow = swing and safety by Alan and Kunal---------------------------------------------------------------
def swing_and_safety():

    motorD.stop_action = motorD.STOP_ACTION_HOLD
    motorD.stop() # stall right motor so that it isn't pushed by the swing instead of pushing the swing

    tank_drive.on_for_rotations(SpeedPercent(50), SpeedPercent(50), 7.62000003141596253589) #moves foward from base into swing
    tank_drive.on_for_rotations(SpeedPercent(-30), SpeedPercent(-30), 0.45) #backs away from swing

    motorD.stop_action = motorD.STOP_ACTION_COAST
    motorD.stop() # unstall right motor so it can move when we need it to

    tank_drive.on_for_rotations(SpeedPercent(-30), SpeedPercent(0), 1.5) #turns to square on wall
    motorA.on_for_degrees(SpeedPercent(15), 150) #left arm turns out from behind the robot so that it is in position to score Elevator
    tank_drive.on_for_rotations(SpeedPercent(-25), SpeedPercent(-25), 0.58) # squares on the wall 
    tank_drive.on_for_rotations(SpeedPercent(45), SpeedPercent(45), 1.8) #drives up to the elevator
    tank_drive.on_for_rotations(SpeedPercent(30), SpeedPercent(0), 1) #turns right to face the elevator
    tank_drive.on_for_rotations(SpeedPercent(30), SpeedPercent(30), 1.25) #drives into elevator and flips it
    motorA.on_for_degrees(SpeedPercent(15), 200)#motor turns away to not unscore elevator
    drive_cm_new(20, -7) # back up so we get a better angle for safety factor
    gyroTurn(36, 30, -26) # turn toward safety factor
    motorD.on_for_degrees(SpeedPercent(30), 150) # move right attachment out of the way of safety factor
    tank_drive.on_for_rotations(SpeedPercent(15), SpeedPercent(15), 0.5) # move halfway to safety factor
    motorA.on_for_degrees(SpeedPercent(30), -350) # move left attachment out of the way of safety factor
    #was 1 instruction of 1.074242...
    tank_drive.on_for_rotations(SpeedPercent(15), SpeedPercent(15), 0.5742424242424242424242424242)#drives up to safety factor|sticking beam under safty factor
    tank_drive.on_for_rotations(SpeedPercent(12), SpeedPercent(-10), 0.2)#turns right to knock the middle two beams
    tank_drive.on_for_rotations(SpeedPercent(-15), SpeedPercent(-15), 0.25) # drives backwards
    tank_drive.on_for_rotations(SpeedPercent(-10), SpeedPercent(10), 0.5)#turns left to knock down the closest left beam
    tank_drive.on_for_rotations(SpeedPercent(-60), SpeedPercent(-65), 7) #drives back to home sweet home
    tank_drive.on_for_rotations(SpeedPercent(-50), SpeedPercent(-60), 5) #drives back to home sweet home
    motorA.stop_action = motorA.STOP_ACTION_COAST
    motorA.stop() # unstall left motor so that we can put the next atachment on without to much difficulty

    motorD.stop_action = motorD.STOP_ACTION_COAST
    motorD.stop() # unstall right motor so that we can put the next atachment on without to much difficulty
#------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------- Big Design and Build is green ----------------------------------------------------------

def big_design_and_build():
    drive_cm(50, 65) # goes forward to drop off a big hunk of designand build blocks
    tank_drive.on_for_seconds(SpeedPercent(-10), SpeedPercent(-50), 2) # turns right to angle back towards home as it backs away from the design and build
    drive_cm(-20, 65) # back into home sweet home

#--------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------ red = Design & Build 1 --------------------------------------------------------

def design_and_build_one(): #small design and build
    drive_cm_new(50,45) #drives forward out just past the red circle
    gyroTurn(-27,0,50) # turns toward tan
    drive_cm_new(50,68) #drives up to tan wheeeeee
    drive_cm_new(50,-42) # drops off tan block by driving backwards|goes all the way to the red circle
    motorD.on_for_degrees(25,80) # opens gate holding red block
    drive_cm_new(50, -15) # goes back in order to drop off the red block
    gyroTurn(35,50,0) # turns to angle towards home
    drive_cm_new(70,-110) # back to home sweet home


#--------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------blue = crane & innovative architecture by Yash and Alan--------------------------------------------------------------------
def crane():
    drive_cm_new(50,40.42) # drives forward out to the wabbit hole
    drive_cm_new(50,-19.42) # drives back (drops off wabbit)
    gyroTurn(-37, 0, 50) # turns toward crane
    drive_cm_new(35,30) #drops crane
    drive_cm_new(50,-51) # drives back so we don't run into big D&B
    gyroTurn(90, 50, 0) # turn right
    drive_cm_new(70,-60) # drive back into home sweet home
#--------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------black = Elevated Places/Bridge - Ben & Joshua-------------------------------------------------------------
def elevated_places():# the bridge mission
    drive_cm_new(65,-127.5) #drive out(backwards so that it can fit up the bridge better) and stop just before the swing | 65% speed -- fast whoosh
    gyroTurn(-90,-15,15)#turns so that the front of the robot faces the wall
    drive_cm_new(60,30) #drives forwards and square on the front of the robot (back of the robot facing bridge)
    drive_cm_new(30,-20) #drives backwards to get in a better postion to drive up the bridge
    gyroTurn(-20,-15,15) # final positioning turn 
    drive_cm_new(30,-119) # drives backwards up bridge
    tank_drive.off() # stalls drivetrain
    while True:
        if (btn.enter): #if the middle button is pressed
            tank_drive.off(brake=False) # Unstall motors
            break
        time.sleep(0.25)
#--------------------------------------------------------------------------------------------------------------------------------------------

#---------------------------------------- creating the function ColorChecking ---------------------------------------------------------------
def ColorChecking():
    if color.color == color.COLOR_YELLOW: #if yellow is seen
        swing_and_safety()#do swing and safty mission
    elif color.color == color.COLOR_GREEN: #if green is seen
        big_design_and_build()#do the big design and buil mission
    elif color.color == color.COLOR_RED: #if red is seen
        design_and_build_one()# do the small design and build mission
    elif color.color == color.COLOR_BLUE: #if blue is seen
        crane()#do the crane mission
    elif color.color == color.COLOR_BLACK: # if black is seen
        elevated_places()#do the bridge mission

#code for all the missions mentioned are up
#--------------------------------------------------------------------------------------------------------------------------------------------

#This is where the movement happens. the function "ColorChecking" is a function to decide what to do based on color.

#--------------- failsafe -------------
def failsafe():
    sys.exit()
#--------------------------------------

#this is when the code accually starts
Sound_.play_tone(frequency=400, duration=0.5, volume=50)#there is a 15-20 second lag when we start a program so this tells us that master has alreafy started by beeping
start = time.time() #this makes it so that when we call start it is equal to what ever far the robot is in the code (IE: 00:12 if it was 12 seconds in)
btn.on_backspace = failsafe

while True: #the code that is indented repetes forever untill we stop the program
    if (btn.down):#if the down button is pressed: 
        break#leave the loop
    pass
    btn.wait_for_released('enter')#waits untill the enter(middle) button is pressed
    ColorChecking() #calls the function color checking see above

# Beepity beep!
Sound_.play_tone(frequency=400, duration=0.5, volume=50)