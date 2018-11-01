# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 15:24:01 2018

@author: USER
"""

import numpy as np
import cv2

def FLANN(factor):
    img1 = cv2.imread("test1.jpg", cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread("test2.jpg", cv2.IMREAD_GRAYSCALE)
    res = None
    
    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)
    
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)
    
    good = []
    for m,n in matches:
        if m.distance < factor*n.distance:
            good.append(m)
            
    res = cv2.drawMatches(img1, kp1, img2, kp2, good, res, flags=2)
    
    cv2.imshow("feature matching", res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
FLANN(0.7)