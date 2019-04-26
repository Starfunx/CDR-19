import matplotlib.pyplot as plt
import numpy as np
import SpaceGeometry as SG
import spacial_objects as obj

import Camera_Parameters as Camera
import Simulation_Parameters as params
import Terrain as T

camera = Camera.camera()
camera.setCameraProfile(6)


#Objetcts
#circle
Circle0 = obj.Circle(np.array([1000,950,0], float), params.cahosCircleRadius, 90)
greenCyl = obj.Circle(np.array([921,946,params.Hcyl], float), 76, 20)
blueCyl = obj.Circle(np.array([996,1049,params.Hcyl], float), 76, 20)

Circle0Center = Circle0Center = np.transpose([1000,950,25])

L = obj.Line([0, 950-200, 0], [3000,950-200,0], 200)
L2 = obj.Line([0, 950+200, 0], [3000,950+200,0], 200)

#projection in the camera coordinate system
D1 = SG.world2Camera(params, T.leftChaosCircle)
#image projection
Y1 = SG.CameraProject(camera, D1)

D8 = SG.world2Camera(params, T.rightChaosCircle)
Y8 = SG.CameraProject(camera, D8)

D2 = SG.world2Camera(params, greenCyl)
Y2 = SG.CameraProject(camera, D2)

D3 = SG.world2Camera(params, blueCyl)
Y3 = SG.CameraProject(camera, D3)

D4 = SG.world2Camera(params, Circle0)
Y4 = SG.CameraProject(camera, D4)

D5 = SG.world2Camera(params, L)
Y5 = SG.CameraProject(camera, D5)

D6 = SG.world2Camera(params, L2)
Y6 = SG.CameraProject(camera, D6)

D7 = SG.world2Camera(params, Circle0Center)
Y7 = SG.CameraProject(camera, D7)



# projection on the plane Z=25
pointRTerrain = SG.CameraInverseProject(camera, Y7)
print("pointRTerrain: " + str(pointRTerrain))

# print(np.linalg.inv(world2CameraMatrix(params)))

################################################################################
## plot
# #graph
plot = plt.figure(figsize=(10,6), num='simulation de camera')

# Terrain
plot = plt.subplot(221)
terrainImg = plt.imread("terrain2000x3000.png")
implot = plot.imshow(terrainImg, origin='upper',extent = (0, 3000, 0, 2000))

plot.plot(T.leftChaosCircle[0], T.leftChaosCircle[1], 'r.')
plot.plot(T.rightChaosCircle[0], T.rightChaosCircle[1], 'r.')

plot.plot(params.robotPosition[0], params.robotPosition[1], 'wo')
plot.plot(params.CamAbsPos[0], params.CamAbsPos[1], 'w+')

plot.plot(greenCyl[0], greenCyl[1], 'g.')
plot.plot(blueCyl[0], blueCyl[1], 'b.')
plot.plot(L[0], L[1], 'k.')
plot.plot(L2[0], L2[1], 'k.')
plot.plot(Circle0Center[0], Circle0Center[1], 'yo')

plot = plt.subplot(222)
plt.axis('equal')
plot.axis([0, camera.npx, 0, camera.npy], ' on equal scaled square')

plot.plot(Y4[0], Y4[1], 'k.')
plot.plot(Y1[0], Y1[1], 'r.')
plot.plot(Y2[0], Y2[1], 'g.')
plot.plot(Y3[0], Y3[1], 'b.')
plot.plot(Y5[0], Y5[1], 'k.')
plot.plot(Y6[0], Y6[1], 'k.')
plot.plot(Y7[0], Y7[1], 'yo')
plot.plot(Y8[0], Y8[1], 'r.')

# Terrain
plot = plt.subplot(223)
terrainImg = plt.imread("terrain2000x3000.png")
implot = plot.imshow(terrainImg, origin='upper',extent = (0, 3000, 0, 2000))

plot.plot(pointRTerrain[0], pointRTerrain[1], 'yo')



plt.show()
