# Task 3. To use keyboard input to control the angle of the servos, find the limiting angle of each servo
# and grab a small item by the robot hand (after grabbing, move the robot tank to another position to put
# the item down). You may take a video via the camera in the front to show the grabbing, moving, and
# releasing of a small item (e.g. an empty plastic water bottle). (20/100)

from _XiaoRGEEK_SERVO_ import XR_Servo
Servo = XR_Servo()
import time

angle = input("Enter Servo Angle: ")

LIMITING_ANGLE = 180

# Restore all servo angles to their saved default values
Servo.XiaoRGEEK_ReSetServo()
#Access one of 4 servos [1,2,3,4] then use [w,s] to increase/decrease angle 

while angle<LIMITING_ANGLE:

        # Set Servo1 angle as 135 degrees
        Servo.XiaoRGEEK_SetServoAngle(1, 135)
        Servo.XiaoRGEEK_SetServoAngle(1, 135)
        Servo.XiaoRGEEK_SetServoAngle(1, 135)
        time.sleep(1)

        # Save all servo angles at this point
        Servo.XiaoRGEEK_SaveServo()
        time.sleep(1)

        # Set Servo1 angle as 150 degrees
        Servo.XiaoRGEEK_SetServoAngle(1, 150)
        time.sleep(1)

        Servo.XiaoRGEEK_SaveServo()
        time.sleep(1)

