import cv2,os
import numpy as np
from PIL import Image 
recognizer = cv2.face.LBPHFaceRecognizer_create()
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'dataSet/face'

def get_images_and_labels(path):
     folder_paths =[os.path.join(path, f) for f in os.listdir(path)]
     for folder_path in folder_paths:
        image_paths = [os.path.join(folder_paths, f) for f in os.listdir(folder_paths)]
        # images will contains face images
        images = []
        # labels will contains the label that is assigned to the image
        labels = []
        for image_path in image_paths:
            # Read the image and convert to grayscale
            image_pil = Image.open(image_path).convert('L')
            # Convert the image format into numpy array
            image = np.array(image_pil, 'uint8')
            # Get the label of the image
            #nbr = int(os.path.split(image_path)[-1].split(".")[0].replace("face-", ""))
            nbr = folder_path
            #nbr=int(''.join(str(ord(c)) for c in nbr))
            print(nbr)
            # Detect the face in the image
            faces = faceCascade.detectMultiScale(image)
            # If face is detected, append the face to images and the label to labels
            for (x, y, w, h) in faces:
                images.append(image[y: y + h, x: x + w])
                labels.append(nbr)
                cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
                cv2.waitKey(10)
        # return the images list and labels list
     return images, labels


images, labels = get_images_and_labels(path)
cv2.imshow('test',images[0])
cv2.waitKey(1)

recognizer.train(images, np.array(labels))
recognizer.write('trainer/trainer.yml')
cv2.destroyAllWindows()