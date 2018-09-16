import cv2

img=cv2.imread("galaxy.jpg",1) #this will read the image in rgb(colored) form

print(type(img))
print(img) #print the matrix of the image
print(img.shape) #gives the no. columns and rows of rows
print(img.ndim)

resized_image=cv2.resize(img,(img.shape[1]//2,img.shape[0]//2)) #this will resize the original image

cv2.imshow('Galaxy',resized_image) #show the resized image
cv2.imwrite("Galaxy_resized.jpg",resized_image) #this will save the new resized image
cv2.waitKey(0) #this allows user to close the window by pressing any key
cv2.destroyAllWindows() #this will destroy all the windows
