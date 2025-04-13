import cv2 #opencv itself
import numpy as np # matrix manipulations

from matplotlib import pyplot as plt 
# import pylab 
# pylab.rcParams['figure.figsize'] = (10.0, 8.0) 

input_image = cv2.imread('/run/media/ilya/2EA61BC4A61B8C09/Python/lab8-theory/Lab-8/variant10.jpg')
ret, new_image = cv2.threshold(input_image, 150, 255, cv2.THRESH_BINARY_INV)

plt.imshow(new_image)
plt.show()