from mySimpleDescriptor import myLocalDescriptor
from PIL import Image

filename = "im1.png"
img = Image.open('im1.png').convert('L')
pix = img.load()
width, height = img.size

rhom = 5
rhoM = 20
rhostep = 1
N = 8

d = myLocalDescriptor(pix, pix[-100, -100], rhom, rhoM, rhostep, N)