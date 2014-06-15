

from PIL import Image
from pylab import *
from numpy import *
from lib import imtools

image = Image.open('../images/lena.jpg').convert('1')
print image.mode
imshow(image)


im = array(Image.open('../images/lena.jpg'))
im2, cdf = imtools.histeq(im) 


figure()
imshow(im)

figure()
imshow(im2)

show()
