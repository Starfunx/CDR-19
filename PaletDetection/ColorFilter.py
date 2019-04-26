#libs
import cv2
import numpy as np

def hsvMask(hsv, lower, upper):
    if lower[0] <= upper[0] :
        mask = cv2.inRange(hsv, lower, upper)
    else: # lower[0] > upper [0]
        mask1 = cv2.inRange(hsv, np.concatenate((lower[:1],lower[1:])) ,
                                 np.concatenate(([255],upper[1:])))
        mask2 = cv2.inRange(hsv, np.concatenate(([0],lower[1:])) ,
                                 np.concatenate((upper[:1],upper[1:])))
        mask= cv2.bitwise_or(mask1, mask2)
    return mask
