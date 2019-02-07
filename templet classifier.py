#TEMPLET MATCHING

import cv2
import numpy as np
import matplotlib.pyplot as plt

full=cv2.imread('D:/test1.png')
#plt.imshow(full)
logo=cv2.imread('D:/test2.png')
#plt.imshow(logo)

methods=['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
for m in methods:
    plt.figure(figsize=(10,10))
    
    full_copy=full.copy()
    method=eval(m)
    
    res=cv2.matchTemplate(full_copy,logo,method)
    
    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left=max_loc
        
    height,width,channels=logo.shape
    
    bottom_right=(top_left[0]+width,top_left[1]+height)
    
    cv2.rectangle(full,top_left,bottom_right,(255,0,0),10)
    
    plt.subplot(121)
    plt.imshow(res)
    plt.title('Heatmap')
    plt.axis('off')
    plt.subplot(122)
    plt.imshow(full)
    plt.title('Detection')
    plt.axis('off')
    plt.show()
 