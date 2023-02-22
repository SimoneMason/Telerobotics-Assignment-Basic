# Task 3. To use keyboard input to control the angle of the servos, find the limiting angle of each servo
# and grab a small item by the robot hand (after grabbing, move the robot tank to another position to put
# the item down). You may take a video via the camera in the front to show the grabbing, moving, and
# releasing of a small item (e.g. an empty plastic water bottle). (20/100)

from _XiaoRGEEK_SERVO_ import XR_Servo
Servo = XR_Servo()

import time
import pygame
import sys

LIMITING_ANGLE_1 = 300
LIMITING_ANGLE_2 = 300
LIMITING_ANGLE_3 = 300
LIMITING_ANGLE_4 = 3000

servoAngle1 = 0
servoAngle2 = 0
servoAngle3 = 0
servoAngle4 = 0
selectedServo = 1

upOffset = 10
downOffset = -10


# Restore all servo angles to their saved default values
Servo.XiaoRGEEK_ReSetServo()


def moveServo1(angle, offset):

    angle = angle + offset
    if (angle <= LIMITING_ANGLE_1):
        Servo.XiaoRGEEK_SetServoAngle(1, angle)
        Servo.XiaoRGEEK_SaveServo()
    else: angle = angle - offset
    
    return angle
    
    


def moveServo2(angle, offset):

    angle = angle + offset
    if (angle < LIMITING_ANGLE_2):
          Servo.XiaoRGEEK_SetServoAngle(2, angle)
          Servo.XiaoRGEEK_SaveServo()
          return angle

def moveServo3(angle, offset):

    angle += offset
    if (angle < LIMITING_ANGLE_3):
         Servo.XiaoRGEEK_SetServoAngle(3, angle)
         Servo.XiaoRGEEK_SaveServo()
         return angle

def moveServo4(angle, offset):

    angle += offset
    if (angle < LIMITING_ANGLE_4):
         Servo.XiaoRGEEK_SetServoAngle(4, angle)
         Servo.XiaoRGEEK_SaveServo()
         return angle


pygame.init()
pygame.display.set_mode((80,80))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Servo.XiaoGREEK_ReSetServo()
            pygame.quit()
            sys.exit()
            
    keyInput= pygame.key.get_pressed()

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

    if keyInput[pygame.K_w]:

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

    elif keyInput[pygame.K_s]:

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
        Servo.XiaoGREEK_ReSetServo()

        pygame.quit()
        sys.exit()
    
  