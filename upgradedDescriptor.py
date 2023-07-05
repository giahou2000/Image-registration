import math
import numpy as np

def myLocalDescriptorUpgrade(I, p, rhom, rhoM, rhostep, N):
    height, width = I.shape[:2]
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
    else:
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

            temp.append(pixel_values)
        
    d = np.mean(temp, axis=0)

    return d