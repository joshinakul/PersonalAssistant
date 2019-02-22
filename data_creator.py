import cv2

vc = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_default.xml')
number_of_images = 0

while True:
    ret,frame = cv2.read(0)
    if ret:
        faces = cascade.detectMultiScale(frame)
    

