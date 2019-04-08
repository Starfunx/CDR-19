import numpy as np
################################################################################
## parameters
################################################################################
#General static parameters
Hcyl  = 25
cahosCircleRadius = 300

CameraPosition = np.array(
    [0,80,325])
alphaCam =  np.pi* 1/8

#robot position and orientation (Relative to terrain)
thetaZrob = -np.pi/2
robotPosition = np.array(
    [100,950,0]   ,float)

# Camera absolute position
CamAbsPos = robotPosition + np.array(
[ CameraPosition[0]*np.cos(thetaZrob) - CameraPosition[1]*np.sin(thetaZrob),
  CameraPosition[1]*np.cos(thetaZrob) + CameraPosition[0]*np.sin(thetaZrob),
  robotPosition[2] + CameraPosition[2]])
