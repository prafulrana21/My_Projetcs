import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #acces the xml file

img=cv2.imread("news.jpg") #read the image

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.5,minNeighbors=5) #this will search the human front face in the image

for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) #create a green color rectangle on the face


resized=cv2.resize(img,(img.shape[1]//3,img.shape[0]//3)) #this will resize the image
cv2.imshow("Gray",resized) #show the image with highlighted human face
cv2.waitKey(0)
cv2.destroyAllWindows() #destroy all the windows
