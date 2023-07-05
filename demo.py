from mySimpleDescriptor import myLocalDescriptor
from PIL import Image

filename = "im1.png"
img = Image.open('im1.png').convert('L')
pix = img.load()
width, height = img.size

print(width)
print(height)
print(pix[-1630, -1320])
print(type(pix))

d = myLocalDescriptor(img, p = 0, rhom = 0, rhoM = 0, rhostep = 0, N = 0)