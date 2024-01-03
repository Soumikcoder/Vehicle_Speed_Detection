import cv2 as cv 
import numpy as np

class counter():
	def __init__(self):
		self.count=0
		self.prev_count=0
	def total_count(self,current_count):
		if current_count>self.prev_count:
			self.count=self.count+(current_count-self.prev_count)
		self.prev_count=current_count
		return self.count
class model1():
	"""docstring for model1"""
	algorithm=cv.bgsegm.createBackgroundSubtractorMOG()

	def __init__(self,y_level_up,y_level_down,car_size):
		self.y_level_up = y_level_up
		self.y_level_down=y_level_down
		self.car_size=car_size

	def find_cars(self,prev_frame,frame) :
		prev_frame_gray=cv.cvtColor(prev_frame,cv.COLOR_BGR2GRAY);
		frame_gray=cv.GaussianBlur(cv.cvtColor(frame,cv.COLOR_BGR2GRAY),(3,3),5);
		img_sub=self.algorithm.apply(frame_gray)
		dialated=cv.dilate(img_sub,np.ones((5,5)))
		kernel=cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
		dialated=cv.morphologyEx(dialated,cv.MORPH_CLOSE,kernel)
		dialated=cv.morphologyEx(dialated,cv.MORPH_CLOSE,kernel)
		contours,hierarchy=cv.findContours(dialated.copy(),cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

		valid=[]
		for i,cntr in enumerate(contours) :
			x,y,w,h=cv.boundingRect(cntr)
			#right lane cars
			if  y>=self.y_level_up and y<=self.y_level_down-h and x<=int(frame.shape[1])/2 and w>self.car_size and h>self.car_size:
				valid.append(cntr)
				cv.rectangle(prev_frame,(x,y),(x+w,y+h),(0,255,0),thickness=1)

			#left lane cars
			if  y>=self.y_level_up and y<=self.y_level_down-h and x>int(frame.shape[1])/2 and w>self.car_size and h>self.car_size:
				valid.append(cntr)
				cv.rectangle(prev_frame,(x,y),(x+w,y+h),(0,0,255),thickness=1)
		#upper line
		cv.line(prev_frame,(0,self.y_level_up),(int(frame.shape[1]),self.y_level_up),(0,255,0))
		#lower line
		cv.line(prev_frame,(0,self.y_level_down),(int(frame.shape[1]),self.y_level_down),(0,255,0))
		return valid
