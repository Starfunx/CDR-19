#
#   librairies
#
import time
import numpy as np
import cv2
# PiCam sudo apt-get install python3-picamera
import picamera

import blobDetector
import Camera_Parameters
import Robot_Parameters

#
#   initialisation
#
camera = picamera.PiCamera()
camera.resolution = (3280, 2464)
camera.framerate = 24
time.sleep(2)

image = np.empty((240, 320, 3), dtype=np.uint8)

cameraModel = Camera_Parameters.camera()
cameraModel.setCameraProfile(2)


#color ranges
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

## get the robot command to find the cilynders
## get the robot position (obtain with the robot command)
robotXpos, robotYpos = [ , ]

## take a photo with the PicamV2
camera.capture(image, 'bgr')

## find center of the cilinders
RCenters, GCenters, BCenters = blobDetector.findAtoms(img, colorRanges)

## inverse project the position of the elipses on the z=25 plane on the terrain
## (gives us the positions of the found center of the "atom" cylinders)


# send result to the robot.
