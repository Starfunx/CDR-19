import numpy as np
import cv2

import ColorFilter

def findCenters(threshold, minArea):
    """Finds center of external shapes

    Parameters
    ----------
    threshold : grayscale image, or mask.
        grayscale image where to search centers of shapes
    minArea : integer
        minimal pixel number that the blob needs to have to have its center returned

    Returns
    -------
    array of 2d vectors
        Centers of shapes found

    """

    Centers = np.array([[0],[0]])
    # find contours in the binary image
    im2, contours, hierarchy = cv2.findContours(threshold,cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    # loop over the contours
    for c in contours:
        area = cv2.contourArea(c)
        if area >= minArea:
           # calculate moments for each contour
            M = cv2.moments(c)
           # calculate moments for each contour
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
            else:
                 cX, cY = 0, 0
            Centers = np.append(Centers, [[cX],[cY]], axis = 1)
    return Centers[:,1:].transpose()

def findAtoms(photo, colorRanges):

    lower_RED = colorRanges[0]
    upper_RED = colorRanges[1]
    lower_GREEN = colorRanges[2]
    upper_GREEN = colorRanges[3]
    lower_BLUE = colorRanges[4]
    upper_BLUE = colorRanges[5]

    #convert rgb image to hsv
    hsv = cv2.cvtColor(photo, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to separate the colors
    redMask = ColorFilter.hsvMask(hsv, lower_RED, upper_RED)
    greenMask = ColorFilter.hsvMask(hsv, lower_GREEN, upper_GREEN)
    blueMask = ColorFilter.hsvMask(hsv, lower_BLUE, upper_BLUE)

    minArea = 5
    RCenters = findCenters(redMask,     minArea)
    GCenters = findCenters(greenMask,   minArea)
    BCenters = findCenters(blueMask,    minArea)

    return RCenters, GCenters, BCenters
