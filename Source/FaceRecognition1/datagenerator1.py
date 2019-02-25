#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 19:25:29 2019

@author: sejal
"""


""" Import Libraries """

import cv2
import os

"""The method makedirs() is recursive directory creation function."""

name = os.makedirs('Images')


""" To load the harcascade file"""

cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


"""To capture a video cap object created"""
cap = cv2.VideoCapture(0)
i=0

while True:
    ret,frame = cap.read(0)
    
    if ret :
            
        ''' Detecting face'''
        faces = cascade.detectMultiScale(frame, 1.5,4)
        
        
        for (x,y,w,h) in faces :
            i=i+1
            cv2.imwrite('Images/'+str(i)+'.jpg',frame[y:y+h,x:x+w])
            cv2.waitkey(100)
            
   
    cv2.imshow('frame',frame)
    cv2.waitkey(30)
    if i>49 :
      break

cap.release()
cv2.destroyAllWindows()

     