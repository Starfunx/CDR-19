'''
camera parameters
'''
import numpy as np

class camera:
    def __init__(self):
        self.npx = None
        self.npy = None
        self.cz = None
        self.cx = None
        self.cy = None
        self.kx = None
        self.ky = None
        self.binningRatio = None

    def setCameraProfile(self, cameraMode):
        #focal length (mm)
        self.cz = np.float32(3.04)

        #number of pixels per milimeter
        self.kx = 1/1.12e-3
        self.ky = 1/1.12e-3

        camera_modes = {
        1 : (1920, 1080, 1), #1920x1080 resolution, no binning.
        2 : (3280, 2464, 1), #3280x2464 resolution, no binning.
        3 : (3280, 2464, 1), #3280x2464 resolution, no binning.
        4 : (1640, 1232, 2), #1640x1232 resolution, 2x2 binning.
        5 : (1640,  922, 2), #1640x922  resolution, 2x2 binning.
        6 : (1280,  720, 2), #1280x720 resolution, 2x2 binning.
        7 : ( 640,  480, 2),  #640x480 resolution, 2x2 binning.
        }

        self.npx = camera_modes[cameraMode][0]
        self.npy = camera_modes[cameraMode][1]
        self.binningRatio = camera_modes[cameraMode][2]
        #camera center (pixels)
        self.cx = self.npx/2
        self.cy = self.npy/2

    def ProjectionMatrix(self):
        P = np.array(
            [[1,      0,         0,      0],
             [0,      1,         0,      0],
             [0,      0, 1/self.cz,      0]])
        A = np.array(
            [[self.kx/self.binningRatio,                         0, self.cx],
             [                        0, self.ky/self.binningRatio, self.cy],
             [                        0,                         0,       1]])
        return np.dot(A,P)
