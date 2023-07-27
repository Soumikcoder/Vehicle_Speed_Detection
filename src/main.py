# importing librarys
import cv2 as cv 
import numpy as np


# loading video
capture=cv.VideoCapture("example_video/test1.mp4")
if not capture.isOpened() :
	print("file path of Video is wrong.......")
while True:
	ret,frame=capture.read()
	if frame is None:
		break;
	# displaying each frame
	cv.imshow('Sample',frame)
	if cv.waitKey(40) & 0xff ==ord('d'):
		break

capture.release()
cv.waitKey(0)