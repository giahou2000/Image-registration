import math
import numpy as np

def myLocalDescriptor(I, p, rhom, rhoM, rhostep, N):
    """
    I: the image
    p: the point that we will describe
    rhom: the radius of the small circle
    rhoM: the radius of the big circle
    rhostep: the radius step for all the circles
    N: the number of points we will scan on each circle
    """

    # access some useful image data
    height, width = I.shape[:2]

    # initialize lists
    temp = []
    d = []

    # watch out for points p near the vertices of the image
    if p[0] < rhoM:
        d = []
    elif p[0] > (width - rhoM):
        d = []
    elif p[1] < rhoM:
        d = []
    elif p[1] > height - rhoM:
        d = []
    # create the descriptor
    else:
        # for each circle
        for r in range(rhom, rhoM + 1, rhostep):
            # Calculate the angle step between pixels
            angle_step = (2 * math.pi) / N
            # Initialize an array to store the pixel values
            pixel_values = []

            # Iterate over the angle range
            for theta in np.arange(0, 2 * math.pi, angle_step):
                # Calculate the coordinates of the pixel on the circle
                x = int(p[0] + r * math.cos(theta))
                y = int(p[1] + r * math.sin(theta))
                # Get the pixel value and store it
                pixel_values.append(I[y, x])

            # store the scanned points of the circle
            temp.append(pixel_values)
        
        # the descriptor is the mean values at axis 0 (row-wise)
        d = np.mean(temp, axis=0)

    return d