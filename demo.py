from mySimpleDescriptor import myLocalDescriptor
from upgradedDescriptor import myLocalDescriptorUpgrade
import cv2
from HarrisCornerDetector import myDetectHarrisFeatures
import numpy as np

filename = "im1.png"
image = cv2.imread(filename, 0)

rhom = 5
rhoM = 20
rhostep = 1
N = 8

# Descriptors for the (100, 100) point
p = [100, 100]

print("")
print("______(100, 100)______")
print("")
print("myLocalDescriptor:")
d = myLocalDescriptor(image, p, rhom, rhoM, rhostep, N)
print(d)
print("")
print("myLocalDescriptorUpgrade:")
d = myLocalDescriptorUpgrade(image, p, rhom, rhoM, rhostep, N)
print(d)


# Descriptors for the (200, 200) point
p = [200, 200]

print("")
print("______(200, 200)______")
print("")
print("myLocalDescriptor:")
d = myLocalDescriptor(image, p, rhom, rhoM, rhostep, N)
print(d)
print("")
print("myLocalDescriptorUpgrade:")
d = myLocalDescriptorUpgrade(image, p, rhom, rhoM, rhostep, N)
print(d)


# Descriptors for the (202, 202) point
p = [202, 202]

print("")
print("______(202, 202)______")
print("")
print("myLocalDescriptor:")
d = myLocalDescriptor(image, p, rhom, rhoM, rhostep, N)
print(d)
print("")
print("myLocalDescriptorUpgrade:")
d = myLocalDescriptorUpgrade(image, p, rhom, rhoM, rhostep, N)
print(d)


# Corners detection
corners = myDetectHarrisFeatures(image)