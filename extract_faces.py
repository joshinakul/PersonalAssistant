import cv2
cascade = cv2.CascadeClassifier('Haarcascade/myfacehaarcascade.xml')

vc = cv2.VideoCapture(0)
i = 0
while True:
    ret,frame = vc.read(0)
    faces = cascade.detectMultiScale(frame,1.5,4)
    
    for (x,y,w,h) in faces:
        i+=1
        cv2.imwrite('Extracted_faces/'+str(i)+'.jpg',frame[y:y+h,x:x+w])
        
        cv2.waitKey(100)
        
    cv2.imshow('frame',frame)
    cv2.waitKey(30)
    if i>49:
        break
vc.release()
cv2.destroyAllWindows()
