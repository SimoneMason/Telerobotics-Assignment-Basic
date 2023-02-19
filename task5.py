# Task 5. To call the camera via cv2 and implement the function of taking and storing pictures.
# (10/100)

import cv2

def callCamera():

    # Capture the default camera
    cap = cv2.VideoCapture(0)
    img_counter = 0 

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('frame', frame)


        # Wait for 'w' to save capture
        if cv2.waitKey(1) & 0xFF == ord('w'):
            img_name = "cv2_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cap.release()
    cv2.destroyAllWindows()

callCamera()

