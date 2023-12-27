# importing librarys
import cv2 as cv 
import model1  

# loading video

capture=cv.VideoCapture("example_video/test1.mp4")
	
ret,frame=capture.read()

# loading first frame
try:
	frame=cv.resize(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)))
except Exception as e:
	print("file path of Video is wrong......." )
	exit()
cars_count=0
playing=True

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
		valid=model1.find_cars(prev_frame,frame)
		cv.putText(prev_frame,f"Vehicle Detected:{len(valid)}",(55,15),cv.FONT_HERSHEY_COMPLEX,0.6,(0,180,0),2)
		cv.imshow('Sample2',prev_frame)
		# else :
		# 	playing=False


capture.release()

