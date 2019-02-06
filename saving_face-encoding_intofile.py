import face_recognition
import numpy as np
import os
import pickle

all_face_encodings = {}

aditya_image = face_recognition.load_image_file("/home/pi/Desktop/adi1.jpg")
aditya_face_encoding= face_recognition.face_encodings(aditya_image)[0]


with open('aditya_faces.dat', 'wb') as f:
    pickle.dump(aditya_face_encoding, f)