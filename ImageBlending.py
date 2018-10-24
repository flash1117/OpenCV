# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 03:03:04 2018

@author: 김기태
"""

import numpy as np
import cv2

def onMouse(x):
    pass

def imgBlending(img1, img2):

    cv2.namedWindow("ImageAdd")
    cv2.createTrackbar("Add", "ImageAdd", 0, 100, onMouse)
    mix = cv2.getTrackbarPos("Add", "ImageAdd")
    
    while True:
        img = cv2.addWeighted(img1, float(100 - mix)/100, # 가중치를 두어서 mix
                              img2 ,float(mix)/100, 0)
        cv2.imshow("MixedImage", img)
        
        key = cv2.waitKey(0) & 0xFF
        if key == 27: # ESC
            break
        
        mix = cv2.getTrackbarPos("Add", "ImageAdd")
        
    cv2.destroyAllWindows()
    
img1 = cv2.imread("sample01.jpg")
img2 = cv2.imread("sample02.jpg")
imgBlending(img1, img2)
        
        
    