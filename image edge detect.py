#Canny Edge Detection

import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('D:/computer vision/d.jpg')
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur=cv2.blur(img,ksize=(5,5))

median=np.median(img)
low=int(max(0,0.7*median))
upper=int(min(160,1.3*median))

edges=cv2.Canny(blur,low,upper)

plt.imshow(edges)
