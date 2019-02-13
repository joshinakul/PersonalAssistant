#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 09:47:25 2019

@author: jk
"""

from keras.layers import Dense,Activation
from keras.layers import LeakyReLU
from keras.models import Sequential

class Model():
    
    def __init__(self,classes):
        
        self.model=Sequential()
        self.classes=classes
        
    
    def model(self):
        
        self.model.add(Dense(64,input_dim=128))
        self.model.add(LeakyReLU(alpha=0.1))
        self.model.add(Dense(32))
        self.model.add(LeakyReLU(alpha=0.1))
        self.model.add(Dense(16))
        self.model.add(LeakyReLU(alpha=0.1))
        self.model.add(Dense(self.classes))
        self.model.add(Activation('softmax'))
        
        return self.model
        