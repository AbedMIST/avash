import pathlib

import cv2
import sys
import numpy as np
from pathlib import Path

camera = cv2.VideoCapture(0)
cnt = 0
while True:
    return_value, image = camera.read()
    cv2.imshow('frame', image)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        name = 'captureImg'+'.png'
        cv2.imwrite(name, image)
        immmg = cv2.imread('captureImg.png')
        # cv2.imshow('name', immmg)

        # input image -> all faces

        #imagePath = sys.argv[1]

        # Load the cascade

        # Load some pre-trained data on face frontal from opencv (haar cascade algorithm)
        trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

        # Choose an image to detect faces in

        # Must convert to greyscale
        grayscaled_img = cv2.cvtColor(immmg, cv2.COLOR_BGR2GRAY)

        # Detect Faces
        face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

        img_crop = []

        # Draw rectangles around the faces
        facenum = 0
        for (x, y, w, h) in face_coordinates:
            cv2.rectangle(immmg, (x, y), (x + w, y + h), (0, 255, 0), 2)
            img_crop.append(immmg[y:y + h, x:x + w])
            facenum = facenum+1
        print(facenum)
        for counter, cropped in enumerate(img_crop):
            cv2.imshow('Cropped', cropped)
            cv2.imwrite("pose_result_{}.png".format(counter), cropped)
            rgb_img = cv2.cvtColor(cropped, cv2.COLOR_BGR2RGB)
            img_encoding = face_recognition.face_encodings(rgb_img)[0]
            cv2.waitKey(0)


        #
        cnt = cnt+1
    if cnt == 4:
        break
del(camera)


#https://docs.google.com/document/d/1VRbTdGiFAJraoXKogXxTESRDqVsM2stHeezqQQWIoTs/edit?usp=sharing
