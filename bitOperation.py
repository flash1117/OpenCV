# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 03:21:33 2018

@author: 김기태
"""

import numpy as np
import cv2

def bitOperation(hpos, vpos):
    img1 = cv2.imread("sample02.jpg")
    img2 = cv2.imread("mollang.jpg")
    
    rows, cols, channels = img2.shape
    roi = img1[vpos:rows+vpos, hpos:cols+hpos]
    
    #로고를 위해 마스크, 역마스크 생성
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)
    
    #ROI 로고부분만 검정색
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    
    img2_fg = cv2.bitwise_and(img2,img2,mask=mask)
    
    dst = cv2.add(img1_bg, img2_fg)
    img1[vpos:rows+vpos, hpos:cols+hpos] = dst
    
    cv2.imshow("result", img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
bitOperation(10,10)