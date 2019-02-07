#Shi-Tomasi Algorithm
import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('D:/computer vision/d.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
des=cv2.goodFeaturesToTrack(gray,100,0.01,10)
#converting the float point array to integers

des=np.int0(des)

for i in des:
    x,y=i.ravel() 
    cv2.circle(img,(x,y),3,(255,0,0),-1)
    
plt.imshow(img)
