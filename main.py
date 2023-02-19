import pygame
import sys

pygame.init()
pygame.display.set_mode((80,80))


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            break
            
    keyInput= pygame.key.get_pressed()
    
    if keyInput[pygame.K_UP]:
          print("up pressed - moving forward")

    if keyInput[pygame.K_DOWN]:
        print("down pressed - moving backwards")
        
    if keyInput[pygame.K_LEFT]:
        print("left presssed - rotating left")

    
    if keyInput[pygame.K_RIGHT]:
        print("right presssed - rotating right")


    if keyInput[pygame.K_d]:
        print("d presssed - decrease speed")    



    if keyInput[pygame.K_a]:
        print("a pressed - incease speed")

       
    if keyInput[pygame.K_q]:
        print("q pressed - stop program")


    # Stop robot anc exit instance
    if keyInput[pygame.K_ESCAPE]:
        print("Exit")
        Stop()
        pygame.quit()
        sys.exit()