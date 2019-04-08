#distance unit is milimeter
#angles are in radian
import numpy as np

import Simulation_Parameters as params
#import Camera_Parameters as camera

def rotationMatrix(Matrix4):
    RotationMatrix = Matrix4
    RotationMatrix[0][3] = 0
    RotationMatrix[1][3] = 0
    RotationMatrix[2][3] = 0
    return RotationMatrix

def terrain2RobotMatrix(params):
    TraTerrain2Robot = np.array(
            [[1, 0, 0, -params.robotPosition[0]],
             [0, 1, 0, -params.robotPosition[1]],
             [0, 0, 1, -params.robotPosition[2]],
             [0, 0, 0, 1]], float)

    thetaZrobTer = -params.thetaZrob
    RotZTerrain2Robot = np.array(
        [[np.cos(thetaZrobTer), -np.sin(thetaZrobTer), 0, 0],
         [np.sin(thetaZrobTer),  np.cos(thetaZrobTer), 0, 0],
         [                   0,                     0, 1, 0],
         [                   0,                     0, 0, 1]], float)

    return  np.dot(RotZTerrain2Robot,TraTerrain2Robot)

def robot2CameraMatrix(params):
    TraRobot2Camera = np.array(
        [[1, 0,  0, -params.CameraPosition[0]],
         [0, 1,  0, -params.CameraPosition[1]],
         [0, 0, -1, params.CameraPosition[2]],
         [0, 0,  0, 1]], float)

    thetaCam = np.pi/2 - params.alphaCam
    RotXRobot2Camera = np.array(
        [[1, 0, 0, 0],
         [0, np.cos(thetaCam), -np.sin(thetaCam), 0],
         [0, np.sin(thetaCam), np.cos(thetaCam), 0],
         [0, 0, 0, 1]], float)
    return np.dot(RotXRobot2Camera,TraRobot2Camera)

def world2CameraMatrix(params):
    HTerrain2Robot = terrain2RobotMatrix(params)
    HRobot2Camera = robot2CameraMatrix(params)
    H = np.dot(HRobot2Camera ,HTerrain2Robot)
    return H

def world2Camera(params, A):
    ones = np.array([np.ones_like(A[0])])
    A = np.concatenate((A, ones), axis=0)
    H = world2CameraMatrix(params)
    R =  np.dot(H,A)
    return np.stack((R[0]/R[3], R[1]/R[3], R[2]/R[3]))

def LinePlaneIntersection(plane, line):
    PlanePoint = plane[0]
    PlaneOrthVect = plane[1]
    LinePoint = line[0]
    LineVect = line[1]

    #linear equation to solve to find the parameter
    a = np.sum(PlaneOrthVect * LineVect, axis = 0)
    b = np.sum(PlaneOrthVect * (PlanePoint - LinePoint), axis = 0)
    t = np.linalg.solve(np.array([[a]]), np.array([b]))

    print("a : " + str(a))
    print("b : " + str(b))
    print("t : " + str(t))

    intersectionPoint = np.transpose(np.array([
         LinePoint[0] + t*LineVect[0],
         LinePoint[1] + t*LineVect[1],
         LinePoint[2] + t*LineVect[2]]))

    return intersectionPoint

def CameraProject(camera, D):
    cameraMatrix = camera.ProjectionMatrix()
    ones = np.array([np.ones_like(D[0])])
    D = np.concatenate((D, ones), axis=0)
    B = np.dot(cameraMatrix, D)
    return np.stack((B[0]/B[2], B[1]/B[2]))

def CameraInverseProject(camera, B):
    A = np.array(
        [[camera.kx,         0, camera.cx],
         [        0, camera.ky, camera.cy],
         [        0,         0,         1]])
    Ap = np.linalg.inv(A)

    #Pixel to milimeter coordinate conversion
    Bp = np.dot(Ap, np.append(B,[1]))

    #paramètre du plan dans R0
    PointPlan = np.transpose(np.array([0,0,25]))
    VectNormalPlan = np.transpose(np.array([0,0,1,1]))

    World2CameraRotationMatrix = rotationMatrix(world2CameraMatrix(params))


    #paramètres du plan dans Rcam = projection world2camera
    PointPlanRcam = world2Camera(params, PointPlan)[:3]
    VectNormalPlanRcam = np.dot(World2CameraRotationMatrix, VectNormalPlan)[:3]

    Plan = np.stack((PointPlanRcam, VectNormalPlanRcam))
    #paramètres de la droite dans le repère de la caméra
    PointDroiteRcam = np.transpose(np.array([0, 0, 0]))
    VectDroiteRcam = np.transpose(np.array([Bp[0], Bp[1], camera.cz]))
    Droite = np.stack((PointDroiteRcam, VectDroiteRcam))

    intersection = np.append(LinePlaneIntersection(Plan, Droite), np.array([1]))

    #projection of the point in the main repere
    Camera2worldMatrix = np.linalg.inv(world2CameraMatrix(params))
    pointRterrain = np.dot(Camera2worldMatrix, intersection)

    return np.stack((pointRterrain[0]/pointRterrain[3],
                     pointRterrain[1]/pointRterrain[3],
                     pointRterrain[2]/pointRterrain[3]))

def getMask(object, cameraProile, CameraMode):
    pass



# to add:
#Documentation for all functions
#
# -- mask get the mask of the usefull zone (big red circle)
