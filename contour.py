from PIL import Image
from pylab import *

# open image
im_original = Image.open('../images/build.jpg')
imshow(im_original)

# create new figure 
figure()
im = Image.open('../images/build.jpg').convert('L')
imshow(im)

# read image to array
im_array = array(im)

# create a new figure
figure()
gray() # don't use colors

# show contours with origin upper left corner
contour(im_array, origin='image')
axis('equal')
axis('off')

# draw histogram

figure()
hist(im_array.flatten(), 128)


show()
