import cv2,os
import numpy as np
from PIL import Image 
import pickle

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'dataSet'

imgResp=urllib.request.urlopen(url)
imgnp=np.array(bytearray(imgResp.read()))
im = cv2.imdecode(imgnp,-1)
font = (cv2.FONT_HERSHEY_SIMPLEX) #Creates a font
gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
faces=faceCascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(50, 50), flags=cv2.CASCADE_SCALE_IMAGE)
for(x,y,w,h) in faces:
    nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
    cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
    if(nbr_predicted==1):
        nbr_predicted='Maxim'
    elif(nbr_predicted==4):
        nbr_predicted='Kar'
    cv2.putText(im,str(nbr_predicted), (x,y+h),font, 2, (0,0,255), 3) #Draw the text
		#   cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)
    cv2.imshow('im',im)
if cv2.waitKey(100) & 0xFF == ord('q'):  
