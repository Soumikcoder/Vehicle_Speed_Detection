# importing librarys
import cv2 as cv 
import model1  

# loading video
capture=cv.VideoCapture("example_video/test1.mp4")
if not capture.isOpened() :
	print("file path of Video is wrong.......")
ret,frame=capture.read()

# loading first frame
frame=cv.resize(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)))
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
		# cv.imshow('Sample',frame)
		ret,frame=capture.read()
		if ret:
			frame=cv.resize(frame,(int(frame.shape[1]/2),int(frame.shape[0]/2)))

			# returns no of vehicles
			valid=model1.find_cars(prev_frame,frame)
			cv.putText(prev_frame,f"Vehicle Detected:{len(valid)}",(55,15),cv.FONT_HERSHEY_COMPLEX,0.6,(0,180,0),2)

			cv.imshow('Sample2',prev_frame)
		else :
			playing=False

capture.release()

