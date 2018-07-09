import cv2
import numpy as np

my_img = cv2.imread('C:\\Users\\kshitij.saxena\\Desktop\\stars.png',cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('My image', cv2.WINDOW_NORMAL)
cv2.imshow('My image', my_img)

key = cv2.waitKey(0)
if key == 27: #checking if the esc key is pressed
	cv2.destroyAllWindows()
elif key == ord('s'): #wait for 's' key to be pressed to save and exit
	cv2.imwrite('C:\\Users\\kshitij.saxena\\Desktop\\my_image.png',my_img)
	cv2.destroyAllWindows()