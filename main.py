# This file combines code from files 2 and 3 in order to be able to move the robot and change the angle of the robot arm simultaneously
import pygame
import sys
import time

import RPi.GPIO as GPIO
from _XiaoRGEEK_SERVO_ import XR_Servo

# Variable and Constant Assignment

Servo = XR_Servo()

#Set PWM to 1000 Hz

Frequency=1000
Speed=50

# Initialise angles for each servo

servoAngle1 = 70
servoAngle2 = 20
servoAngle3 = 20
servoAngle4 = 20
selectedServo = 1

upOffset = 10
downOffset = -10

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define port and default duty cycle of PWM

ENA=13
ENB=20
IN1=19
IN2=16
IN3=21
IN4=26

GPIO.setup(ENA,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(ENB,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN1,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN2,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN3,GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(IN4,GPIO.OUT, initial=GPIO.LOW)
                                     
# Specify the PWM control port and the frequency of the PWM signal
PWMA=GPIO.PWM(ENA,Frequency)
PWMB=GPIO.PWM(ENB,Frequency)

PWMA.start(0)
PWMB.start(0)

pygame.init()
pygame.display.set_mode((80,80))


# Restore all servo angles to their saved default values
Servo.XiaoRGEEK_ReSetServo()

# Set pins to the correct true or false settings for each type of motion

def Move_Forward():
    
    GPIO.output(ENA,True)
    GPIO.output(ENB,True)
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)

def Move_Backward():
    
    GPIO.output(ENA,True)
    GPIO.output(ENB,True)
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)
    
    
def Turn_Left():
    
    PWMA.ChangeDutyCycle(50)
    PWMB.ChangeDutyCycle(0)
    GPIO.output(ENA,True)
    GPIO.output(ENB,True)
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)
    
def Turn_Right():

    PWMA.ChangeDutyCycle(50)
    PWMB.ChangeDutyCycle(50)
    GPIO.output(ENA,True)
    GPIO.output(ENB,True)
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)  

# Functions to change the speed of the motors

def Increase_Speed(Speed):
    print("speed is initially " + str(Speed))
    if Speed != 100:
        Speed+=10
        PWMA.ChangeDutyCycle(Speed)
        PWMB.ChangeDutyCycle(Speed)
        print("speed is now " + str(Speed))
    else:
        print("speed is at MAX!")

    return Speed

def Decrease_Speed(Speed):
    print("speed is initially " + str(Speed))
    if Speed > 0:
        Speed-=10
        PWMA.ChangeDutyCycle(Speed)
        PWMB.ChangeDutyCycle(Speed)
        print("speed is now " + str(Speed))
    else:
        print("speed is at MIN!")

    return Speed


def Stop():
    
    PWMA.ChangeDutyCycle(0)
    PWMB.ChangeDutyCycle(0)

    GPIO.output(ENA,True)
    GPIO.output(ENB,True)
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, False)


# Limiting Angles: 1) 0-170 2)0-180 3) 0-180 4) 20-80


def moveServo1(angle, offset):

    temp = angle + offset
    if (temp <= 170):
        if (temp >= 0):
            Servo.XiaoRGEEK_SetServoAngle(1, angle)
            Servo.XiaoRGEEK_SaveServo()
        else:
            print("Limiting angle reached on servo" + str(angle))
            return angle
    else: 
        print("Limiting angle reached on servo" + str(angle))
        return angle
    return temp
    


def moveServo2(angle, offset):

    temp = angle + offset
    if (temp <= 180):
        if (temp >= 0):
          Servo.XiaoRGEEK_SetServoAngle(2, angle)
          Servo.XiaoRGEEK_SaveServo()
        else:
            print("Limiting angle reached on servo " + str(angle))
            return angle
    else: 
        print("Limiting angle reached on servo" + str(angle))
        return angle
    return temp

def moveServo3(angle, offset):

    temp = angle + offset
    if (temp <= 180):
        if (temp >= 0):
         Servo.XiaoRGEEK_SetServoAngle(3, angle)
         Servo.XiaoRGEEK_SaveServo()
        else:
            print("Limting angle reached on servo " + str(angle))
            return angle
    else: 
        print("Limiting angle reached on servo" + str(angle)) 
        return angle
    return temp

def moveServo4(angle, offset):
    temp = angle + offset
    if (temp <= 80):
        if (temp >= 0):
         Servo.XiaoRGEEK_SetServoAngle(4, angle)
         Servo.XiaoRGEEK_SaveServo()
        else:
            print("Limting angle reached on servo " + str(angle))
            return angle

    else: 
        print("Limiting angle reached on servo" + str(angle))
        return angle
    return temp

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break
            
    keyInput= pygame.key.get_pressed()
    
    if keyInput[pygame.K_UP]:
        Move_Forward()
        print("Forward")
        time.sleep(0.3)
          

    if keyInput[pygame.K_DOWN]:
        print("Reverse")
        Move_Backward()
        time.sleep(0.3)
        
    if keyInput[pygame.K_LEFT]:
        print("Left pressed")
        Turn_Left()
        time.sleep(0.3)
    
    if keyInput[pygame.K_RIGHT]:
        print("Right pressed")
        Turn_Right()
        time.sleep(0.3)

    if keyInput[pygame.K_w]:
        print("Increase speed")    
        Speed = Increase_Speed(Speed)
        time.sleep(0.3)


    if keyInput[pygame.K_s]:
        print("Decrease speed")
        Speed = Decrease_Speed(Speed)
        time.sleep(0.3)
       
    if keyInput[pygame.K_q]:
        print("Stop")
        Stop()

        # Select an appropriate servo
    
    if keyInput[pygame.K_1]:
        print("Servo One Accessed")
        selectedServo = 1

    if keyInput[pygame.K_2]:
        print("Servo Two Accessed")
        selectedServo = 2
        
    if keyInput[pygame.K_3]:
        print("Servo Three Accessed")
        selectedServo = 3

    
    if keyInput[pygame.K_4]:
        print("Servo Four Accessed")
        selectedServo = 4    

        # Move a selected servo up and down

    if keyInput[pygame.K_d]:

        if selectedServo==1:
            servoAngle1 = moveServo1(servoAngle1, upOffset)
            time.sleep(0.2)
        elif selectedServo==2:
            servoAngle2 = moveServo2(servoAngle2, upOffset)
            time.sleep(0.2)
        elif selectedServo==3:
            servoAngle3 = moveServo3(servoAngle3, upOffset)
            time.sleep(0.2)
        elif selectedServo==4:
            servoAngle4 = moveServo4(servoAngle4, upOffset)
            time.sleep(0.2)

    elif keyInput[pygame.K_a]:

        if selectedServo==1:
            servoAngle1 = moveServo1(servoAngle1, downOffset)
            time.sleep(0.2)
        elif selectedServo==2:
            servoAngle2 = moveServo2(servoAngle2, downOffset)
            time.sleep(0.2)
        elif selectedServo==3:
            servoAngle3 = moveServo3(servoAngle3, downOffset)
            time.sleep(0.2)
        elif selectedServo==4:
            servoAngle4 = moveServo4(servoAngle4, downOffset)
            time.sleep(0.2)
    




    # Stop robot anc exit instance
    if keyInput[pygame.K_ESCAPE]:
        print("Exit")
        Stop()
        Servo.XiaoGREEK_ReSetServo()
        pygame.quit()
        sys.exit()