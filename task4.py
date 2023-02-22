# Task 4. To load an image with cv2 and display its grayscale, resized and rotated image.

import cv2
  
# Load the image

img = cv2.imread("Test_image.jpg")
img_gray = cv2.imread("Test_image.jpg", cv2.IMREAD_GRAYSCALE)

# Display the image
cv2.imshow('image', img)

# Display grayscale image
img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow('Gray image', img_gray)

# Display resized image
print("Original dimensions: ", img.shape)
scale_percent = 60
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# Resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

print("Resized dimensions: ", resized.shape)

cv2.imshow('resized-image', resized)

# Display rotated image
img_cw_180 = cv2.rotate(img, cv2.ROTATE_180)
cv2.imshow("Image rotated by 180 degree", img_cw_180)

# Check keyboard input
input_key = cv2.waitKey(0)&0xFF
# Wait for 'esc' to exit
if input_key == 27:
    cv2.destroyAllWindows()

# Wait for 's' to save the image before exit
elif input_key == ord('s'):
    cv2.imwrite("Duplicate_image.jpg", img)
    cv2.destroyAllWindows()
                        
