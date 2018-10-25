# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 15:27:15 2018

@author: USER
"""

import cv2

def showimage():
    image = cv2.imread("rabbit.jpg",1)
    cv2.imshow('rabbit', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

showimage()