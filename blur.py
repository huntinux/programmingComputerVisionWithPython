
from PIL import Image
from numpy import *
from scipy.ndimage import filters
im = array(Image.open('empire.jpg').convert('L'))
im2 = filters.gaussian_filter(im,5)

imshow(im)

figure()
imshow(im2)

show()
