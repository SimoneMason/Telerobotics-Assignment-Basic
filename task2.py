# Task 2. To use keyboard input to control the robot tank's movement and travel speed. Note: The travel
# speed can be varied by changing the duty cycle of the PWM (the frequency of the PWM signal should
# be set at 1000 Hz). Keyboard input can be captured using a library called pygame, or you can use any
# other library you find useful. (20/100)

import pygame
import RPi.GPIO as GPIO
import time
import sys


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

## Define port and default duty cycle of PWM

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
                                     
Frequency=1000
Speed=50


# Specify the PWM control port and the frequency of the PWM signal
PWMA=GPIO.PWM(ENA,Frequency)
PWMB=GPIO.PWM(ENB,Frequency)

PWMA.start(0)
PWMB.start(0)


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
    
    PWMA.ChangeDutyCycle(90)
    PWMB.ChangeDutyCycle(90)
    GPIO.output(ENA,True)
    GPIO.output(ENB,True)
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)
    
def Turn_Right():

    PWMA.ChangeDutyCycle(90)
    PWMB.ChangeDutyCycle(90)
    GPIO.output(ENA,True)
    GPIO.output(ENB,True)
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)  

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

pygame.init()
pygame.display.set_mode((80,80))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Stop()
            pygame.quit()
            sys.exit()
            
    keyInput= pygame.key.get_pressed()
    
    if keyInput[pygame.K_UP]:
          Move_Forward()
          print("Forward")
          time.sleep(1)
          

    if keyInput[pygame.K_DOWN]:
        print("Reverse")
        Move_Backward()
        time.sleep(1)
        
    if keyInput[pygame.K_LEFT]:
        print("Left pressed")
        Turn_Left()
        time.sleep(1)
    
    if keyInput[pygame.K_RIGHT]:
        print("Right pressed")
        Turn_Right()
        time.sleep(1)

    if keyInput[pygame.K_d]:
        print("Increase speed")    
        Speed = Increase_Speed(Speed)
        time.sleep(1)


    if keyInput[pygame.K_a]:
        print("Decrease speed")
        Speed = Decrease_Speed(Speed)
        time.sleep(1)
       
    if keyInput[pygame.K_q]:
        print("Stop")
        Stop()

    # Stop robot anc exit instance
    if keyInput[pygame.K_ESCAPE]:
        print("Exit")
        Stop()
        pygame.quit()
        sys.exit()
    
  
