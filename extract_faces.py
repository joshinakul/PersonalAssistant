import cv2
img = cv2.imread('Data/nj.jpg')
cascade = cv2.CascadeClassifier('Haarcascade/myfacehaarcascade.xml')
faces = cascade.detectMultiScale(img,1.5,4)
for (x,y,w,h) in faces:
    cv2.imwrite('Extracted_faces/nj.jpg',img[y:y+h,x:x+w])
