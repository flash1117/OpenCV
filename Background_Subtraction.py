# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 15:37:33 2018

@author: USER
"""

import numpy as np
import cv2

def backSubtraction():
    cap = cv2.VideoCapture(0)
    cap.set(3,640)
    cap.set(4,480)
    #mog = cv2.bgsegm.createBackgroundSubtractorMOG()
    mog = cv2.createBackgroundSubtractorMOG2()
    
    while True:
        ret, frame = cap.read()
        fgmask = mog.apply(frame)
        
        cv2.imshow("mask", fgmask)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        
    cap.release()
    cv2.destroyAllWindows()
    
    
    
def backSubtractionGMG(): # opening 기법으로 noise 제거 하는 것이 좋음
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
    
    while True:
        ret, frame = cap.read()
        fgmask = fgbg.apply(frame)
        fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
        
        cv2.imshow("mask", fgmask)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        
    cap.release()
    cv2.destroyAllWindows()
        
backSubtractionGMG()
#backSubtraction()