
import cv2 as cv 
import numpy as np
algorithm=cv.bgsegm.createBackgroundSubtractorMOG()
def find_cars(prev_frame,frame) :
	prev_frame_gray=cv.cvtColor(prev_frame,cv.COLOR_BGR2GRAY);
	frame_gray=cv.GaussianBlur(cv.cvtColor(frame,cv.COLOR_BGR2GRAY),(3,3),5);
	img_sub=algorithm.apply(frame_gray)
	dialated=cv.dilate(img_sub,np.ones((5,5)))
	kernel=cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
	dialated=cv.morphologyEx(dialated,cv.MORPH_CLOSE,kernel)
	dialated=cv.morphologyEx(dialated,cv.MORPH_CLOSE,kernel)
	valid=[]
	contours,hierarchy=cv.findContours(dialated.copy(),cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
	for i,cntr in enumerate(contours) :
		x,y,w,h=cv.boundingRect(cntr)
		if  y>=310 and w>60 and h>60:
			valid.append(cntr)
			# cv.rectangle(prev_frame,(x,y),(x+w,y+h),(0,255,0),thickness=1)
	cv.line(prev_frame,(0,254),(638,254),(0,255,0))
	# cv.imshow('Dailated',dialated)
	return valid