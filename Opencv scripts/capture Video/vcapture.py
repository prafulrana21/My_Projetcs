import cv2, time

video=cv2.VideoCapture(0) # thsi will turn on the camera
a=1

while(True):
    a=a+1
    check, frame=video.read() #this will read the image (frame)
    cv2.imshow("capturing",frame) #this will show the image on screen-
    cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    key=cv2.waitKey(1)
    if key==ord("q"):
        break   #terminate loop when user press q

video.release() #this will stop accessing the camera

#time.sleep(3)
#cv2.imshow("capturing",frame)
#cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#cv2.waitKey(0)
#video.release()

cv2.destroyAllWindows() #destroy all the windows
