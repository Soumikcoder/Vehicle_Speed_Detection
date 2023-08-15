# importing librarys
import cv2 as cv 
import numpy as np
from model1 import * 

# loading video
capture=cv.VideoCapture("example_video/test3.mp4")
if not capture.isOpened() :
	print("file path of Video is wrong.......")
ret,frame=capture.read()
frame=cv.resize(frame,(640,480))
cars_count=0
while True:
	if frame is None:
		break;
	# displaying each frame
	if cv.waitKey(40) & 0xff ==ord('d'):
		break
	prev_frame=frame
	# cv.imshow('Sample',frame)
	ret,frame=capture.read()
	frame=cv.resize(frame,(640,480))
	valid=find_cars(prev_frame,frame)
	cv.putText(prev_frame,f"Vehicle Detected:{len(valid)}",(55,15),cv.FONT_HERSHEY_COMPLEX,0.6,(0,180,0),2)
	cv.imshow('Sample2',prev_frame)

capture.release()
cv.waitKey(0)