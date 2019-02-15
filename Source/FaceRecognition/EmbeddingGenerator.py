#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 09:47:26 2019

@author: jk
"""
from keras.models import load_model

class embedding():
    
    def __init__(self):
        # load model 
        self.model=load_model('facenet_keras.h5')
    
    def embeddings(self,img):
        # return prediction vector of 128 values
        return self.model.predict(img)[0]
    
        
