# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 21:00:52 2018

@author: 김기태
"""

import cv2

def thresholding():
    img = cv2.imread("sample01.jpg", cv2.IMREAD_GRAYSCALE)
    
    thr1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C
                                      ,cv2.THRESH_BINARY, 11, 2)
    thr2 =  cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY, 11, 2)
    
    titles = ["original", "adaptive mean", "adaptive gaussian"]
    images = [img, thr1, thr2]
    
    for i in range(3):
        cv2.imshow(titles[i], images[i])
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
thresholding()