#!/usr/bin/env python3
#^^^^This line is required to tell the EV3 to run this file using Python|it is called a shebang line|it MUST be on the first line

# FLL 42, Pythonian Rabbotics's master program.

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MediumMotor#gives us accses to everything we need to run EV3 dev
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import GyroSensor
from ev3dev2.button import Button
from ev3dev2.sound import Sound
from ev3dev2.display import Display
from robotClass import Robot
import time


btn = Button() # variable so we can get buttons pressed on EV3
color = ColorSensor(INPUT_4) # color sensor for checking attachment color
tank_drive = MoveTank(OUTPUT_B, OUTPUT_C)  # Creates a variable so we can control the drivetrain
motorA = MediumMotor(OUTPUT_A) # left medium motor
motorD = MediumMotor(OUTPUT_D) # right medium motor
gyro = GyroSensor(INPUT_1) # gyro variable
Sound_ = Sound() # beepity beep
Display_ = Display() # for displaying text



Sound_.play_tone(frequency=400, duration=0.5, volume=50)#there is a 15-20 second lag when we start a program so this tells us that master has alreafy started by beeping
start = time.time() #this makes it so that when we call start it is equal to what ever far the robot is in the code (IE: 00:12 if it was 12 seconds in)
btn.on_backspace = failsafe

while True: #the code that is indented repetes forever untill we stop the program
    if (btn.down):#if the down button is pressed: 
        break#leave the loop
    pass
    btn.wait_for_released('enter')#waits untill the enter(middle) button is pressed
    Robot.colorChecking #calls the function color checking

# Beepity beep!
Sound_.play_tone(frequency=400, duration=0.5, volume=50)

#line 42 yeeeet