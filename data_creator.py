import cv2

vc = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarcascade/haarcascade_frontalface_alt2.xml')
number_of_images = 0

while True:
    ret,frame = vc.read(0)
    if ret:
        faces = cascade.detectMultiScale(frame)
        for (x,y,w,h) in faces:
            number_of_images+=1
            cv2.imwrite('ExtractedFaces/'+str(number_of_images)+'.jpg',frame[y:y+h,x:x+h])
            cv2.waitKey(20)
        print('Image number '+str(number_of_images)+' fetched!')
        if number_of_images>50 or cv2.waitKey(3)==ord('q'):
            break
vc.release()
cv2.destroyAllWindows()


