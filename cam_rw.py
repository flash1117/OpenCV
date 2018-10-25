# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 15:01:26 2018

@author: Kim Ki Tae
"""
import cv2

def showVideo():
    try:
        print("open cam")
        cap = cv2.VideoCapture(0)
    except:
        print("open cam error")
        return;
        
    cap.set(3, 480) ## 폭
    cap.set(4, 320) ## 높이
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Video read error")
            break
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("video", gray)
        
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            cap.release()
            cv2.destroyAllWindows()
            break
        
showVideo()

