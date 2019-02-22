#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 03:32:22 2019

@author: meenal
"""

"""Data Generator"""

import cv2
import os

name = os.makedirs('Data')

'''Loading Harcascade File'''
face_detect = cv2.CascadeClassifier("face.xml")

vc = cv2.VideoCapture(0)
i=0 

while True:
    ret,frame = vc.read(0)
    if ret:
        '''Converting frame from BGR to gray'''
        grayscale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        '''Detecting face from the grayscale image'''
        f = face_detect.detectMultiScale(grayscale,1.1,5)
        
        '''Putting rectangle and saving in the data folder'''
        for (x,y,w,h) in f:
             i+=1
             cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 2)
             cv2.imwrite('Data/'+str(i)+'.jpg', frame[y:y+h,x:x+w])
             cv2.waitKey(100)
             
    cv2.imshow('Frame',frame)        
    if cv2.waitKey(1) & 0xff == ord('q') or i>49:
        break
vc.release()
cv2.destroyAllWindows()