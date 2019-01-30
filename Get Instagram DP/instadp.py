from tkinter import *
from getdp.img import getimg
import cv2
from skimage import io
from io import BytesIO
from PIL import ImageTk,Image 
import requests 
import urllib.parse
import os
def getinstadp():
	x=''
	x=getimg.calling(username.get())
	response = requests.get(x)
	img      = Image.open(BytesIO(response.content))
	img.show()
	#image = io.imread(x)
	#cv2.imshow("Correct", cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
	#cv2.imwrite("username.jpg",cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
	#root = Tk()
	#os.rename("username.jpg","username.gif")
	#can1=Canvas(root,bg="green",height=300,width=400)
	#img = PhotoImage(file="username.gif")
	#image=can1.create_image(200,100,anchor=CENTER,image=img)
	#can1.pack()
	#panel = Label(root, image = img)
	#panel.pack(side = "bottom", fill = "both", expand = "yes")
	#root.mainloop()
window=Tk() #create the window(outer structure of the app
window.wm_title("Instagram DP") #give the title to the app

window.resizable(0,0)
#Label(text="Insta DP Viewer",pady=5,bg="green",font=("",30)).pack()
l1=Label(window, text="Username") #create the title label
l1.grid(row=0,column=0) #position the title label

username=StringVar() #create an object that contain the Title of Book
t1=Entry(window,textvariable=username) #create the entry box for title label
t1.grid(row=0,column=1,columnspan=2) #position the Entry Box


b1=Button(window,text="Submit", width=12,command=getinstadp) #create the View All Button
b1.grid(row=1,column=0) #position the button

b6=Button(window,text="close", width=12,command=window.destroy)#create the Close Button 
b6.grid(row=1,column=3) #position the button

window.mainloop()