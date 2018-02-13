import cv2
import urllib.request
import numpy as np
import os

def detectFace(url,name,photoId):
    imgResp=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(imgResp.read()))
    im = cv2.imdecode(imgnp,-1)
    detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    i=0
    offset=50
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(50, 50), flags=cv2.CASCADE_SCALE_IMAGE)
    directory = "dataSet/face/"+name
    for(x,y,w,h) in faces:
        i=i+1
        if not os.path.exists(directory):
            os.makedirs(directory)
        cv2.imwrite(directory +'/'+ photoId + ".jpg", gray[y-offset:y+h+offset,x-offset:x+w+offset])
        cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)
        cv2.imshow('im',im[y-offset:y+h+offset,x-offset:x+w+offset])
        cv2.waitKey(100)
    cv2.destroyAllWindows()
    