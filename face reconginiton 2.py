import cv2
import os
import numpy
data=r"opencv project\data sets"
har=r"opencv project\haarcascade_frontalface_default.xml"
images=[]
lalbes=[]
id=0
names={}
face_cascade=cv2.CascadeClassifier(har)
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
webcam=cv2.VideoCapture(0)
while True:
    (_,img)=webcam.read()
    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grey,1.2,3)
    for (x,y,w,h) in faces :
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),5)
        face=grey[y:y+h,x:x+w]
        face_resize=cv2.resize(face,(130,100))
        prediction=modle.predict(face_resize)
        if prediction[1]<500:
            cv2.putText(img,names[prediction[0]],(20,20),cv2.FONT_HERSHEY_PLAIN,1,(255,255,255))
    cv2.imshow("face recogniton",img)
    key=cv2.waitKey(10)
    if key== 27:
        break