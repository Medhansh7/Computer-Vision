#Corner Harris Algorithm

import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('D:/computer vision/d.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)
dst=cv2.cornerHarris(gray,2,3,0.04)

dst=cv2.dilate(dst,None)
img[dst>0.01*dst.max()]=[255,0,0]

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xff == ord('q'):
    cv2.destroyAllWindows()
