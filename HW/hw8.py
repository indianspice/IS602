#Using Python's built-in functionality, scipy, or any other module, perform the following tasks:
#Thresholding: First convert the image to a binary image.  This is done with a technique called thresholding, which is
# covered in the reading.  There are functions for it in scipy, although it is very easy to do manually.  Essentially
# read each pixel and if it above a specified gray level make it white, otherwise make it black.
#Count objects:  Count the number of objects in the image.  If you are interested in how this is done, refer to the
# additional readings.  An object will be a group of white pixels surrounded by black pixels.  Doing this by hand is
# also fairly easy, but try to use functions found in the modules available.
#Find center points: For each object, find the center point in terms of x,y coordinates.  As with part 3, you can do
# this directly, but it's better to use something from a module.

import numpy as np
import scipy.ndimage as ndimage
import scipy.misc as misc
import scipy as mdimage
import matplotlib.pylab as pyl
import mahotas as mh


# Circles
# Read and show image
circles = misc.imread('circles.png')
pyl.imshow(circles)
pyl.show()

#Threshold
T = mh.otsu(circles)
circlesTh = (circles > T)
circlesF = mh.gaussian_filter(circles, 33)
circlesRegmax = mh.regmax(circlesF)
labels, near = mh.label(circlesRegmax)
pyl.imshow(mh.overlay(circles, circlesRegmax))
pyl.show()

#Count circles
km,circlesCnt = mh.label(circlesRegmax)
print circlesCnt

#Find center points
centerMass = mh.center_of_mass(circles, labels)[1:]
print centerMass

#Objects
objects = mh.imread('objects.png')
pyl.imshow(objects)
pyl.show()

#Threshold Objects
objectsTh = (objects > objects.mean())
objectsF = mh.gaussian_filter(objects, 10)
objectsRegmax = mh.regmax(objectsF)
labelsObjts, near = mh.label(objectsRegmax)
pyl.imshow(objectsRegmax)
pyl.show()      #This image did not show I toubleshoot but could not fix it. The code executes without error

#Count Objects
km, objectsCnt = mh.label(objectsRegmax)
print objectsCnt

#Find center points
centers = mh.center_of_mass(objects, labelsObjts)[1:]
print centers


#Peppers
peppers = mh.imread('peppers.png')
pyl.imshow(peppers)
pyl.show()

#Threshold Peppers
peppersTh = mh.otsu(peppers)
peppersF = (peppers > peppersTh)
peppersSm = mh.gaussian_filter(peppersF, 28)
peppersRegmax = mh.regmax(peppersSm)
labelsPeppers, near = mh.label(peppersRegmax)
pyl.imshow(peppersSm)
pyl.show()

#Count Peppers
km, peppersCnt = mh.label(peppersRegmax)
print peppersCnt

#Find Center Points
peppers = mh.center_of_mass(peppers, labelsPeppers)[1:]
print centers


#Reference
#http://docs.opencv.org/trunk/d7/d4d/tutorial_py_thresholding.html
#http://pythonvision.org/basic-tutorial/
#http://bio.academany.org/labs/fablabkamakura/students/yumi/weeks/w10_image_processing.html
