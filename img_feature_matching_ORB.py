# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 14:30:21 2018

@author: USER
"""

import numpy as np
import cv2

def featureMatching():
    img1 = cv2.imread("test1.jpg", cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread("test2.jpg", cv2.IMREAD_GRAYSCALE)
    res = None
    
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)
    
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
    matches = bf.match(des1, des2)
    
    matches = sorted(matches, key=lambda x:x.distance)
    res = cv2.drawMatches(img1, kp1, img2, kp2, matches[:30], res, flags=0)
    
    cv2.imshow("feature matching", res)
    cv2.waiyKey(0)
    cv2.destroyAllWindows()
    
featureMatching()