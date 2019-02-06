# Face Recognition
A facial recognition system is a technology capable of identifying or verifying a person from a digital image or a video frame from a video source. There are multiple methods in which facial recognition systems work, but in general, they work by comparing selected facial features from given image with faces within a database. It is also described as a Biometric Artificial Intelligence based application that can uniquely identify a person by analysing patterns based on the person's facial textures and shape.

# What the project does?
Project contain 2 python files, one with name- "saving_face-encoding_intofile.py" that saves the face encodings of the person who's image it is reading and another named-"face_recogition(reading encodings and interpreting in livestreaming).py" that reads the face_encoding file and compare that face encoding with live faces(live streaming), if the face encoding in the file matches with the person in front it returns the name of the person given in the code.


# Requirements:-
Install face_recognition (library)

Install numpy (if you don't have)

Install cv2    (openCV library)

# How users can get started with the project?
1) Download the repository

2) Open file ""saving_face-encoding_intofile.py" , in this file give the path to image of who's face is to recognise           like("/home/pi/Desktop/") in my case:-

aditya_image = face_recognition.load_image_file("/home/pi/Desktop/adi1.jpg")

You can use yourname_image instead of aditya_image and yourname_face_encoding instead of aditya_face_encoding but remember should also change below[.face_encodings(yourname_image)]:-

aditya_face_encoding= face_recognition.face_encodings(aditya_image)[0]

you can give whatever name you want to give to face encoding file it will be saved in .dat format:-

with open('yourname_faces.dat', 'wb') as f:
 
   pickle.dump(yourname_face_encoding, f)
   
 You can save as many file as you want for different images.
      
3) Open file "face_recogition(reading encodings and interpreting in livestreaming).py" from pickle.load() load the file by giving the name of face encoding file. You can open as many face encoding files as you want.

known_face_encodings = [ yourname_face_encoding ] Here in known_face_encodings[] list you can write the variable you created for encodings.

known_face_names = [ "yourname" ]

Here in known_face_name[] list you can add your name you want to see while camera is recognising you.

# Created and managed by ADITYA SURANA.
