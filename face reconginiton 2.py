import cv2
import os
import numpy
data=r"opencv project\data sets"
har=r"opencv project\haarcascade_frontalface_default.xml"
images=[]
lalbes=[]
id=0
names={}
for subdirectrys,directry,files in os.walk(data):
    for subdirectry in directry :
        names[id]=subdirectry
        path=os.path.join(data,subdirectry)
        for file in os.listdir(path):
            imgpath=os.path.join(path,file)
            img=cv2.imread(imgpath,0)
            images.append(img)
            lalbes.append(id)
        id=id+1
(images,lalbes)=[numpy.array(lis) for lis in [images,lalbes]]
print("img captured")
#training the machine model
modle=cv2.face.LBPHFaceRecognizer_create()
modle.train(images,lalbes)
print("train")