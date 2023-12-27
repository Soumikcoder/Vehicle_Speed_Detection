# importing librarys
import cv2 as cv 
from model1 import model1 

# loading video
video_id=2
capture=cv.VideoCapture(f"example_video/test{video_id}.mp4")
ret,frame=capture.read()

# loading first frame
try:
	frame=cv.resize(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)))
except Exception as e:
	print("file path of Video is wrong......." )
	exit()
cars_count=0
playing=True

#choosing parameter
if video_id==1:
	y_up=180
	y_down=310
	car_size=25
elif video_id==2 :
	y_up=100
	y_down=310
	car_size=80
model= model1(y_up,y_down,car_size)
#Press D to Quit the video

#video loop
while playing:
		# displaying each frame
		if cv.waitKey(40) & 0xff ==ord('d'):
			playing=False
			break
		prev_frame=frame
		ret,frame=capture.read()
		frame=cv.resize(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)))

			# returns no of vehicles
		valid=model.find_cars(prev_frame,frame)
		cv.putText(prev_frame,f"Vehicle Detected:{len(valid)}",(55,15),cv.FONT_HERSHEY_COMPLEX,0.6,(0,180,0),2)
		cv.imshow('Sample2',prev_frame)

capture.release()

