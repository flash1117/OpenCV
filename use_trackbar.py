# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:59:16 2018

@author: KKT
"""

import numpy as np
import cv2

def onChange(x):
    pass

def trackbar():
    img = np.zeros((200, 512, 3), np.uint8)
    cv2.namedWindow("color palette")
    
    cv2.createTrackbar('B', "color palette", 0, 255, onChange)
    cv2.createTrackbar('G', "color palette", 0, 255, onChange)
    cv2.createTrackbar('R', "color palette", 0, 255, onChange)

    switch = '0: OFF\n1: ON'
    cv2.createTrackbar(switch, "color palette", 0, 1, onChange)
    
    while True:
        cv2.imshow("color palette", img)
        key = cv2.waitKey(1) & 0xFF

        if key == 27:
            break
        
        b = cv2.getTrackbarPos('B', "color palette")
        g = cv2.getTrackbarPos('G', "color palette")
        r = cv2.getTrackbarPos('R', "color palette")
        s = cv2.getTrackbarPos(switch, "color palette")
        
        if s==0:
            img[:] = 0
        else:
            img[:] = [b,g,r]

    cv2.destroyAllWindows()
    
trackbar()
