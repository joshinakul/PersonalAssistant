#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 17:33:05 2019

@author: jk
"""

import cv2
import os

"""
function: Create_dir
     create the directory if not already present
parameter:
    name:String of the name of directory
return :
        None
"""
def create_dir(name:str):
    if not os.path.exists(name):
        os.mkdir(name)
    else :
        print("Directory already present")


create_dir("Data")
    


 
        
    
    
    