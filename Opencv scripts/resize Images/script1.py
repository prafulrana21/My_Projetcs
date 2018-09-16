import cv2
import glob

images=glob.glob("*.jpg") #create the list of all the images with jpg extension

for image in images:
    img=cv2.imread(image,0) #read the image
    re=cv2.resize(img,(100,100)) #resize the original image
    cv2.imshow('Hey',re)#open the image on a window
    cv2.waitKey(500) #close the image after 500 milliseconds
    cv2.destroyAllWindows()
    cv2.imwrite("resized"+image,re) #save the new resized image
