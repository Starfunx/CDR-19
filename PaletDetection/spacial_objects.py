# permet d'obtenir des points dans l'espace pour des figures géométriques donnés

import numpy as np


#renvoie nbpoints points d'un cercle de diametre CircleDiameter dans le plan
# x,y 
def Circle(circleCenter, CircleDiameter, nbpoints):
    theta = np.linspace(0,2*np.pi,nbpoints)
    X = np.cos(theta) * CircleDiameter / 2 + circleCenter[0]
    Y = np.sin(theta) * CircleDiameter / 2 + circleCenter[1]
    Z = np.ones_like(X) * circleCenter[2]

    C = np.stack((X,Y,Z))
    return C

def Line(A, B, nbpoints):
    T = np.linspace(0, 1, nbpoints)
    V =np.array(
        [[B[0]-A[0]],
         [B[1]-A[1]],
         [B[2]-A[2]]])

    X = V[0]*T + np.ones_like(T) * A[0]
    Y = V[1]*T + np.ones_like(T) * A[1]
    Z = V[2]*T + np.ones_like(T) * A[2]

    L = np.stack((X,Y,Z))
    return L
