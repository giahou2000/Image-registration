from mySimpleDescriptor import myLocalDescriptor
import cv2
import numpy as np
import math

filename = "im1.png"
image = cv2.imread(filename, 0)

rhom = 5
rhoM = 20
rhostep = 1
N = 8
p = [100, 100]

d = myLocalDescriptor(image, p, rhom, rhoM, rhostep, N)
print(d)