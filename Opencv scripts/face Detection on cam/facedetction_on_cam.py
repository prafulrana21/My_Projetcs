import cv2, time

video=cv2.VideoCapture(0) #this will acccess the web cam

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #read the xml file
#check, frame=video.read()
while(True):
    check, img=video.read() #read the images from the camera
    #cv2.imshow("capturing",img)
    gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #change the color of image to gray
    faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.5,minNeighbors=5) #find the human face from the image
    for x,y,w,h in faces:
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) #create a rectangle around the humna face
    resized=cv2.resize(img,(img.shape[1]-100,img.shape[0]-100)) #resize the new image with highligted human face
    cv2.imshow("Gray",resized) #show the new image
    key=cv2.waitKey(1) #close the image after 1 millisecond
    if key==ord("q"):
        break #terminate the loop when user press the 'q' key

video.release() #stop accessing the camera

#time.sleep(3)
#cv2.imshow("capturing",frame)
#cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#cv2.waitKey(0)
#video.release()

cv2.destroyAllWindows() #destroy all windows
