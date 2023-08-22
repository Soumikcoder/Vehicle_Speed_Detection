import cv2 as cv 
import numpy as np

algorithm=cv.bgsegm.createBackgroundSubtractorMOG()
y_level_up=180
y_level_down=310

def find_cars(prev_frame,frame) :
	prev_frame_gray=cv.cvtColor(prev_frame,cv.COLOR_BGR2GRAY);
	frame_gray=cv.GaussianBlur(cv.cvtColor(frame,cv.COLOR_BGR2GRAY),(3,3),5);
	img_sub=algorithm.apply(frame_gray)
	dialated=cv.dilate(img_sub,np.ones((5,5)))
	kernel=cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
	dialated=cv.morphologyEx(dialated,cv.MORPH_CLOSE,kernel)
	dialated=cv.morphologyEx(dialated,cv.MORPH_CLOSE,kernel)
	contours,hierarchy=cv.findContours(dialated.copy(),cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

	valid=[]
	for i,cntr in enumerate(contours) :
		x,y,w,h=cv.boundingRect(cntr)
		#right lane cars
		if  y>=y_level_up and y<=y_level_down-h and x<=int(frame.shape[1])/2 and w>25 and h>25:
			valid.append(cntr)
			cv.rectangle(prev_frame,(x,y),(x+w,y+h),(0,255,0),thickness=1)

		#left lane cars
		if  y>=y_level_up and y<=y_level_down-h and x>int(frame.shape[1])/2 and w>25 and h>25:
			valid.append(cntr)
			cv.rectangle(prev_frame,(x,y),(x+w,y+h),(0,0,255),thickness=1)
	#upper line
	cv.line(prev_frame,(0,y_level_up),(int(frame.shape[1]),y_level_up),(0,255,0))
	#lower line
	cv.line(prev_frame,(0,y_level_down),(int(frame.shape[1]),y_level_down),(0,255,0))
	return valid