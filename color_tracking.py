# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 18:22:24 2018

@author: KKT
"""

import numpy as np
import cv2

def tracking():
        try:
            print("start camera")
            cap = cv2.VideoCapture(0)
        except:
            print("open cam error")
            return
            
        while True:
            ret, frame = cap.read()
            
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            #HSV에서 BGR 로 가정할 범위를 정의함
            lower_blue = np.array([100,100,100])
            upper_blue = np.array([160,255,255])
            
            lower_green = np.array([40,100,100])
            upper_green = np.array([100,255,255])
            
            lower_red = np.array([-40, 100, 100])
            upper_red = np.array([40,255,255])
            
            mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
            mask_green = cv2.inRange(hsv, lower_green, upper_green)
            mask_red = cv2.inRange(hsv, lower_red, upper_red)
            
            # mask && origin image
            res1 = cv2.bitwise_and(frame, frame, mask=mask_blue)
            res2 = cv2.bitwise_and(frame, frame, mask=mask_green)
            res3 = cv2.bitwise_and(frame, frame, mask=mask_red)
            
            cv2.imshow("origin", frame)
            cv2.imshow("blue", res1)
            cv2.imshow("green", res2)
            cv2.imshow("red", res3)
            
            key = cv2.waitKey(1) & 0xFF
            if key == 27:
                break
            
        cv2.destroyAllWindows()
        
tracking()

            
            

