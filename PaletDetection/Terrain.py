#distance unit is milimeter
import numpy as np

import spacial_objects as obj
import SpaceGeometry as SG

chaosCircle_radius = 300
cylinder_Height= 25

leftChaosCircle_UpPosition = np.array([1000,950,25])
rightChaosCircle_UpPosition = np.array([2000,950,25])

leftChaosCircle  = obj.Circle(leftChaosCircle_UpPosition, chaosCircle_radius, 100)
rightChaosCircle = obj.Circle(rightChaosCircle_UpPosition, chaosCircle_radius, 100)
