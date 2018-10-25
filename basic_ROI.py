# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 17:57:03 2018

@author: USER
"""

import numpy as np
import cv2

img = cv2.imread("rabbit.jpg")
cv2.imshow("origin", img)

subimg = img[300:400, 350:750]
cv2.imshow("cutting", subimg)

img[300:400, 0:400] = subimg # (0,300) ~ (400, 400)

print(img.shape)
print(subimg.shape)

cv2.imshow("modified", img)

cv2.waitKey(0)
cv2.destroyAllWindows()