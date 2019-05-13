import numpy as np
import blobDetector
import cv2

#vizualisation (debug)
import matplotlib.pyplot as plt
import time

start = time.time()

lower_RED = np.array([160,120,120])
upper_RED = np.array([10,255,255])

lower_GREEN = np.array([10,120,120])
upper_GREEN = np.array([40,170,255])

lower_BLUE = np.array([90,80,120])
upper_BLUE = np.array([140,255,255])

colorRanges = np.array([
    lower_RED, upper_RED,
    lower_GREEN, upper_GREEN,
    lower_BLUE, upper_BLUE
    ])

# Load picture, convert to grayscale and detect edges
filename = "Assets/image6.png"
img = cv2.imread(filename)
output_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

Time = time.time() - start


RCenters, GCenters, BCenters = blobDetector.findAtoms(img, colorRanges)


#plots
print("Red :\n"   + str(RCenters))
print("Green :\n" + str(GCenters))
print("Blue :\n"  + str(BCenters))
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
plt.title("img")
implot = plot.imshow(output_img, origin='upper')

plot = plt.subplot(224)
plt.title(str(Time) + 's')
implot = plot.imshow(img, origin='upper')
plot.plot(RCenters[0], RCenters[1], 'yo')
plot.plot(GCenters[0], GCenters[1], 'yo')
plot.plot(BCenters[0], BCenters[1], 'yo')


plt.show()
