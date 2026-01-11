import cv2
import numpy as np
import os
harfile=r"opencv project\haarcascade_frontalface_default.xml"
datasets=r"opencv project\data sets"
sub_data="krish"
path=os.path.join(datasets,sub_data)
if not os.path.isdir(path):
    os.mkdir(path)
face_cascade=cv2.CascadeClassifier(harfile)
webcam=cv2.VideoCapture(0)
count=1
while count<30:
    value,image=webcam.read()
    grey=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grey,1.2,3)
    for (x,y,w,h) in faces :
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,0),5)
        face=grey[y:y+h,x:x+w]
        face_resize=cv2.resize(face,(130,100))
        cv2.imwrite(f"{path}/{count}.png", face_resize)
        count=count+1
        print("imiage capture")
    cv2.imshow("image",image)
    a=cv2.waitKey(10)
    if a == 27:
        break
