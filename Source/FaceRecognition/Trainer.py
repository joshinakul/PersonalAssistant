#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 09:47:24 2019
@author: jk

"""
import os
from EmbeddingGenerator import embedding 
import numpy as np
import cv2
from ModelArchitecture import Model
from keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical

def no_of_classes():
    k = os.listdir("Data")
    return len(k)

def train(model,classes,learning_rate,epochs,batch_size):
    x=[]
    y=[]
    e=embedding()
    data_classes = os.listdir("Data")
    
    for p in data_classes:
        for i in os.listdir("Data/"+p):
            img = cv2.imread("Data/"+p+"/"+i,1)
            img = cv2.resize(img,(160,160))
            img = img.astype("float")/255.0
            img = np.expand_dims(img,axis=0)
            emb = e.embeddings(img)
            x.append(emb)
            y.append(str(p.split("_")[0]))
            
    x=np.array(x,dtype='float')
    y=np.array(y)
    y=np.resize(len(y),1)
    print(x.shape,y.shape)
    
    
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.1,random_state=77)
    y_train=to_categorical(y_train,num_classes=classes)
    y_test=to_categorical(y_test,num_classes=classes)
    
    optimizer=Adam(lr=learning_rate,decay=learning_rate/epochs)
    model.compile(optimizer=optimizer,loss="categorical_crossentropy")
    model.fit(x_train,y_train,epochs-epochs,batch_size=batch_size,shuffle='true',validation_data=(x_test,y_test))
    return model


if __name__=="__main__":
    learning_rate=0.1
    epochs=30
    batch_size=32
    classes=no_of_classes()
    m=Model(classes)
    model=m.models()
    face_model=train(model,classes,learning_rate,epochs,batch_size)
    
    if not os.path.exist("Models"):
        os.mkdir("Models")
    no_of_Models=len(os.listdir("Models"))
        
    face_model.save("Models/Face_reco_{}.MODEL".format(no_of_Models+1))
    
    
    
            
            
            
            
    
    
    
    
    
    
