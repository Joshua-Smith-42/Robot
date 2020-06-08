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



#-----------------------------------yellow = swing and safety by Alan and Kunal---------------------------------------------------------------

#------------------------------------------------- Big Design and Build is green ----------------------------------------------------------

#------------------------------------------------------------ red = Design & Build 1 --------------------------------------------------------

#----------------------------------------blue = crane & innovative architecture by Yash and Alan--------------------------------------------------------------------

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