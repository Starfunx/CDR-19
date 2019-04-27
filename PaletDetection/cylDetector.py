import numpy as np
import cv2

import ColorFilter

#vizualisation (debug)
import matplotlib.pyplot as plt
import time

def findCenters(threshold):
    Centers = np.array([[0],[0]])
    # find contours in the binary image
    im2, contours, hierarchy = cv2.findContours(threshold,cv2.RETR_EXTERNAL ,
        cv2.CHAIN_APPROX_SIMPLE)
    # loop over the contours
    for c in contours:
        area = cv2.contourArea(c)
        if area >= 10:
           # calculate moments for each contour
            M = cv2.moments(c)
           # calculate moments for each contour
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
            else:
                 cX, cY = 0, 0
            Centers = np.append(Centers, [[cX],[cY]], axis = 1)
    return Centers[:,1:]


start = time.time()

lower_RED = np.array([160,120,120])
upper_RED = np.array([10,255,255])

lower_GREEN = np.array([10,120,120])
upper_GREEN = np.array([40,170,255])

lower_BLUE = np.array([90,80,120])
upper_BLUE = np.array([140,255,255])

# Load picture, convert to grayscale and detect edges
filename = "Assets/image6.png"
img = cv2.imread(filename)
output_img = img

#convert rgb image to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Threshold the HSV image to separate the colors
redMask = ColorFilter.hsvMask(hsv, lower_RED, upper_RED)
greenMask = ColorFilter.hsvMask(hsv, lower_GREEN, upper_GREEN)
blueMask = ColorFilter.hsvMask(hsv, lower_BLUE, upper_BLUE)

RCenters = findCenters(redMask)
GCenters = findCenters(greenMask)
BCenters = findCenters(blueMask)

Time = time.time() - start

#plots
print("Red :\n"   + str(RCenters))
print("Green :\n" + str(GCenters))
print("Blue :\n"  + str(BCenters))

RCenters = RCenters.transpose()
GCenters = GCenters.transpose()
BCenters = BCenters.transpose()
# print(RCenters.shape[1])

for i in range(RCenters.shape[0]):
    cv2.putText(img, "Red", (RCenters[i][0]-15, RCenters[i][1]-15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,  (30, 30, 30), thickness = 1, lineType=cv2.LINE_AA)
for i in range(GCenters.shape[0]):
    cv2.putText(img, "Green", (GCenters[i][0]-15, GCenters[i][1]-15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,  (30, 30, 30), thickness = 1, lineType=cv2.LINE_AA)
for i in range(BCenters.shape[0]):
    cv2.putText(img, "Blue", (BCenters[i][0]-15, BCenters[i][1]-15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,  (30, 30, 30), thickness = 1, lineType=cv2.LINE_AA)


RCenters = RCenters.transpose()
GCenters = GCenters.transpose()
BCenters = BCenters.transpose()

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plot = plt.figure(figsize=(10,6), num='elipse center')


plot = plt.subplot(221)
plt.title("hsv")
implot = plot.imshow(hsv, origin='upper')

plot = plt.subplot(222)
plt.title("redMask")
implot = plot.imshow(redMask, origin='upper')

plot = plt.subplot(223)
plt.title("blueMask")
implot = plot.imshow(blueMask, origin='upper')

plot = plt.subplot(224)
plt.title(str(Time) + 's')
implot = plot.imshow(img, origin='upper')
plot.plot(RCenters[0], RCenters[1], 'yo')
plot.plot(GCenters[0], GCenters[1], 'yo')
plot.plot(BCenters[0], BCenters[1], 'yo')


plt.show()
