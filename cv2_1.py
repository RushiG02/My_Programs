# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:57:46 2020

@author: Rushi
"""

import numpy as np
import cv2

def ntg(x):
    print(x)
    
img=np.zeros([300,512,3],np.uint8)
'''
img=cv2.imread('20190307_153251.jpg',1)
img=cv2.resize(img,(480,480),interpolation=cv2.INTER_AREA)

b=img[:,0]
g=img[:,1]
r=img[:,2]
print(b,g,r)
'''
cv2.namedWindow('image')
cv2.createTrackbar('B','image',0,255,ntg)
cv2.createTrackbar('G','image',0,255,ntg)
cv2.createTrackbar('R','image',0,255,ntg)

while(1):
    cv2.imshow('image',img)

    k=cv2.waitKey(1)&0xFF
    if k==27:
        break
    b=cv2.getTrackbarPos('B','image')
    g=cv2.getTrackbarPos('G','image')
    r=cv2.getTrackbarPos('R','image')
    
    img[:]=[b,g,r]
cv2.destroyAllWindows()