#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 17:33:05 2019

@author: jk
"""

import cv2
import os
import csv
from FaceDetector import DetectFace
import time



class CreateData():
    
    id=0
    Users={}
    
    
    def __init__(self):
        self.generate_images()
        
        
   
    def detect_face(self,img):
        return DetectFace.detect_face(img)
    """
    function: Create_dir
         create the directory if not already present
         parameter:
             name:String of the name of directory
         return :
             None
    """
    def create_dir(self,name:str):
        if not os.path.exists(name):
            os.mkdir(name)
        else :
            print("Directory already present")
    
    
    """
    function :create_data
    parameter:
            self
    return:
            self.user=user name
            self.id=present id value
        
    """
    def create_data(self):
        user=str(input("Enter user name:"))
        self.id+=1
        self.Users[user]=self.id #writing to users dictionary
        self.create_dir("Data/"+user+"_"+str(self.id))# create dir for cuurent user
        return user,self.id
    
    
    """
    function :write to csv
                write user data to csv file    
    parameter:
              self
    return:
              None
    """
    def write_to_csv(self):
        with open("Faces_list.csv","w") as face_list:
            writer=csv.writer(face_list)
            for keys, values in self.users.items():
                writer.writerow([keys,values])
    
    
    """
    function :generate_images
        Click images if face is detected .
    parameter:
        self
    return:
        None
        
    """
    def generate_images(self):
        self.count=0
        cap=cv2.VideoCapture(0)# start vidocapture
        sample_num=0
        # ggenerate user name and id
        user,Id=self.create_data()
        while True:
            ret ,frame=cap.read()
            frame = cv2.resize(frame,(600,400))  
            if ret:
                k=cv2.waitKey(100)
                faces=self.detect_face(frame) # Detectface
                
                # check if faces are found
                if len(faces)==0:
                    print("no faces detected")
                    continue;
                else:
                    
                    for _ in faces:
                        # set image name
                        img_name="Data/"+user+"_"+str(Id)+"/{}.png".format(sample_num)
                        # Save image
                        cv2.imwrite(img_name,frame)
                        sample_num+=1 # increment sample num variable
                        print("{}-Data Created for {}".format(sample_num,user))
                        
                
                cv2.imshow('frame',frame)
                cv2.namedWindow("frame",cv2.WINDOW_NORMAL)
                
                if sample_num>50:
                    break
                # close frame
                if k%256==27:
                    print("Escape Hit")
                    break
        cap.release()
        cv2.destroyAllWindows()
    
CreateData()

     
        
        
        
        
        
        
    
    
    
    


 
        
    
    
    