# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 16:11:15 2018

@author: KKT
"""

import numpy as np
import cv2
from random import shuffle
import math


mode, drawing = True, False
ix, iy = -1,-1
b = [i for i in range(256)]
g = [i for i in range(256)]
r = [i for i in range(256)]
     
def onMouse(event, x, y, flags, param):
    global ix,iy, drawing, mode, b,g,r
    
    if event == cv2.EVENT_LBUTTONDOWN: # 마우스 눌렀을때
        drawing = True
        ix, iy = x,y
        shuffle(b), shuffle(g), shuffle(r)
    
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(param, (ix,iy), (x,y), (b[0],g[0],r[0]), -1)
            else:
                R = (ix-x)**2 + (iy-y)**2
                R = int(math.sqrt(R))
                cv2.circle(param, (ix,iy), R, (b[0], g[0], r[0]), -1)
                
    elif event == cv2.EVENT_LBUTTONUP:
        drawing=False
        if mode:
            cv2.rectangle(param, (ix,iy), (x,y), (b[0], g[0], r[0]), -1)
        else:
            R = (ix-x)**2 + (iy-y)**2
            R = int(math.sqrt(R))
            cv2.circle(param, (ix,iy), R, (b[0], g[0], r[0]), -1)
        
def mouseBrush():
    global mode
    
    img = np.zeros((512,512,3), np.uint8)
    cv2.namedWindow("paint")
    cv2.setMouseCallback("paint", onMouse, param=img)
    
    while True:
        cv2.imshow("paint", img)
        key = cv2.waitKey(1) & 0xFF
        
        if key == 27:
            break
        elif key == ord('m'):
            mode = not mode
        
    cv2.destroyAllWindows()
    
mouseBrush()