import numpy as np
import math
from scipy import ndimage

def isCorner(I, p, k, Rthres):
    """
    I: the grayscale image
    p: the point of interest
    k: a parameter defined by us, in order to calibrate the detection process
    Rthres: threshold for detecting corners
    """

    # Initialize export variable
    c = False

    # Calculate R

    # Derivative I1
    Kx = -1*np.array([[-1,0,1]]) # the mask
    I1 = ndimage.convolve(I, Kx)

    # Derivative I2
    Ky = -1*np.array([[-1],[0],[1]]) # the mask
    I2 = ndimage.convolve(I, Ky)

    # Initialize parameters
    u1 = 2
    u2 = 2
    sigma = 1

    M = Mfunc(u1, u2, p[0], p[1], I1, I2, sigma)

    R = np.linalg.det(M) - k * ((np.trace(M))**2)

    # If R > threshold
    if R > Rthres:
        # we detected a corner
        c = True
    # If R < threshold
    elif R < Rthres:
        # no corner detected
        c = False
    
    return c

# Function that has non zero values near to (0,0)
def w(x1, x2, sigma):
    return math.exp(-(x1**2 + x2**2)/(2*(sigma**2)))

# Function the exports the A matrix for Harris Corner Detection algorithm
def alpha(p1, p2, u1, u2, I1, I2):
    return [[(I1[p1+u1][p2+u2])**2, I1[p1+u1][p2+u2] * I2[p1+u1][p2+u2]], [I1[p1+u1][p2+u2] * I2[p1+u1][p2+u2], (I2[p1+u1][p2+u2])**2]]

# Function the exports the M matrix for Harris Corner Detection algorithm
def Mfunc(u1, u2, p1, p2, I1, I2, sigma):
    M = 0
    for i in range(u1):
        for j in range(u2):
            M = M + np. multiply(int(w(i, j, sigma)), alpha(p1, p2, i, j, I1, I2))
    return M

def myDetectHarrisFeatures(I):
    """
    I: the grayscale image
    """

    # Initialize parameters
    height, width = I.shape[:2]
    k = 1
    Rthres = 5

    # Detect the corners
    corners = []
    for i in range(height):
        for j in range(width):
            if isCorner(I, [i, j], k, Rthres) == True:
                corners.append([i, j])

    return corners