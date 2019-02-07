#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 19:19:28 2019

@author: jk
"""
import cv2
Class DetectFace():
    def __init__(self,img):
        self.detect_face(img)
        
        
    def detect_face(img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);
        
    return faces
    pass