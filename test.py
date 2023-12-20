"""import cv2
import numpy as np
import glob
original = cv2.imread("D:/OneDrive_2023-12-09/Hub Designs/TransferNow-Sample data to be tested/test 9.JPG")
# Sift and Flann
sift = cv2.xfeatures2d.SIFT_create()
kp_1, desc_1 = sift.detectAndCompute(original, None)
index_params = dict(algorithm=0, trees=5)
search_params = dict()
flann = cv2.FlannBasedMatcher(index_params, search_params)

# Load all the images
all_images_to_compare = []
titles = []
for f in glob.iglob("D:\OneDrive_2023-12-09\Hub Designs\TransferNow-original images\*"):
    image = cv2.imread(f)
    titles.append(f)
    all_images_to_compare.append(image)

for image_to_compare, title in zip(all_images_to_compare, titles):
    # 1) Check if 2 images are equals
    if original.shape == image_to_compare.shape:
        print("The images have same size and channels")
        difference = cv2.subtract(original, image_to_compare)
        b, g, r = cv2.split(difference)
        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("Similarity: 100% (equal size and channels)")
            break
    # 2) Check for similarities between the 2 images
    kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)
    matches = flann.knnMatch(desc_1, desc_2, k=2)
    good_points = []
    for m, n in matches:
        if m.distance > 0.6*n.distance:
            good_points.append(m)
    number_keypoints = 0
    if len(kp_1) >= len(kp_2):
        number_keypoints = len(kp_1)
    else:
        number_keypoints = len(kp_2)
    print("Title: " + title)
    percentage_similarity = len(good_points) / number_keypoints * 100
    print("Similarity: " + str(int(percentage_similarity)) + "\n")"""


"""import cv2


def is_template_in_image(img, templ):

    # Template matching using TM_SQDIFF: Perfect match => minimum value around 0.0
    result = cv2.matchTemplate(img, templ, cv2.TM_SQDIFF)

    # Get value of best match, i.e. the minimum value
    min_val = cv2.minMaxLoc(result)[0]

    # Set up threshold for a "sufficient" match
    thr = 10e-6

    return min_val <= thr


# Read template
template = cv2.imread('D:/OneDrive_2023-12-09/Hub Designs/TransferNow-Sample data to be tested/test 9.JPG')

# Collect image file names
images = ["D:/OneDrive_2023-12-09/Hub Designs/TransferNow-original images/4004.jpg", "D:/OneDrive_2023-12-09/Hub Designs/TransferNow-original images/4013.jpg"]

for image in images:
    if is_template_in_image(cv2.imread(image), template):
        print('{}: {}'.format(image, 'Pokemon has ran away.'))
    else:
        print('{}: {}'.format(image, 'Nothing to see here.'))"""

"""import cv2
import numpy as np

image= cv2.imread('D:/OneDrive_2023-12-09/Hub Designs/TransferNow-original images/4013.jpg')
cv2.imshow('Rainforest', image)
cv2.waitKey(0)
gray= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

template= cv2.imread('D:/OneDrive_2023-12-09/Hub Designs/TransferNow-Sample data to be tested/test 9.JPG',0)


result= cv2.matchTemplate(gray, template, cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc= cv2.minMaxLoc(result)

height, width= template.shape[:2]

top_left= max_loc
bottom_right= (top_left[0] + width, top_left[1] + height)
cv2.rectangle(image, top_left, bottom_right, (0,0,255),5)

cv2.imshow('Rainforest', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""


#!/usr/bin/python
# vim: set ts=2 expandtab:
"""
Module: test01.py
Desc: Test to draw info out of poker image.
Author: John O'Neil
Email: oneil.john@gmail.com
DATE: Saturday, Sept 21st 2014

  Simple test to draw info from poker image.
  Image and required info is in /test subfolder.

"""

"""import cv2
import numpy as np

img_rgb = cv2.imread('D:/OneDrive_2023-12-09/Hub Designs/TransferNow-original images/4013.jpg')
template = cv2.imread('D:/OneDrive_2023-12-09/Hub Designs/TransferNow-Sample data to be tested/test 9.JPG')
w, h = template.shape[:-1]

res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
threshold = .8
loc = np.where(res >= threshold)
for pt in zip(*loc[::-1]):  # Switch columns and rows
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imwrite('result.png', img_rgb)

import cv2

method = cv2.TM_SQDIFF_NORMED

# Read the images from the file
small_image = cv2.imread('D:/OneDrive_2023-12-09/Hub Designs/TransferNow-Sample data to be tested/test 9.JPG')
large_image = cv2.imread('D:/OneDrive_2023-12-09/Hub Designs/TransferNow-original images/4013.jpg')

result = cv2.matchTemplate(small_image, large_image, method)

# We want the minimum squared difference
mn,_,mnLoc,_ = cv2.minMaxLoc(result)

# Draw the rectangle:
# Extract the coordinates of our best match
MPx,MPy = mnLoc

# Step 2: Get the size of the template. This is the same size as the match.
trows,tcols = small_image.shape[:2]

# Step 3: Draw the rectangle on large_image
cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

# Display the original image with the rectangle around the match.
cv2.imwrite('result.png', large_image)

# The image is only displayed if we call this
cv2.waitKey(0)"""


"""import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img = cv.imread('test/test2.jpg', cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
img2 = img.copy()
template = cv.imread('test/4002.jpg', cv.IMREAD_GRAYSCALE)
assert template is not None, "file could not be read, check with os.path.exists()"
w, h = template.shape[::-1]
# All the 6 methods for comparison in a list
methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
            'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
for meth in methods:
    img = img2.copy()
    method = eval(meth)
    # Apply template Matching
    res = cv.matchTemplate(img,template,method)
    print(res)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    
    cv.rectangle(img,top_left, bottom_right, (0, 255, 0),10)
    plt.subplot(121),plt.imshow(res,cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap = 'gray') 
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)
    plt.show()"""


"""import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img_rgb = cv.imread('test/4012.jpg')
assert img_rgb is not None, "file could not be read, check with os.path.exists()"
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('test/test8.jpg', cv.IMREAD_GRAYSCALE)
assert template is not None, "file could not be read, check with os.path.exists()"
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
if len((loc[0])) > 0:
    print("Oggetti trovati")
else:
    print("No oggetti")
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255,255,255), 2)
cv.imwrite('res.png',img_rgb)"""

"""import os
file = "C:/Users/Orion/Documents/PythonProjects/image_finder/"
a = [x[0] for x in os.walk(f"{file.replace('/', os.sep)}")]
print(a)
all_files = []
for i in a:
    files = os.listdir(i)

datoMinimo = 0
datoMassimo = 87
valoreNormalizzato = 0
for i in range(datoMassimo):
    valoreDato = i  # Cambia questo valore con i tuoi dati effettivi

    valoreNormalizzato = ((valoreDato - datoMinimo) / (datoMassimo - datoMinimo)) * 100
    
    print(valoreNormalizzato)

if valoreNormalizzato < 100 and valoreNormalizzato >98:
    valoreNormalizzato +=2"""
"""import random
from threading import Thread
import time
def test(c):
    print(c)
    for i in c:
        time.sleep(1)
        print(i, "Ciao")


test1 = [1,2,3,4,5,6,7,8,9,10,11]
def split(a, n):
    k, m = divmod(len(a), n)
    return (a[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))
 
print(list(split(test1, 3)))
t = list(split(test1, 3))
for x in t:
    t1 = Thread(target=test, args=(x,))
    t1.start()"""

import numpy as np
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import os
import sys

def compare_image():
        image = "test/4012.jpg"
        main_image = "test/test2.jpg"
        try:
            main_response = False
            img_rgb = cv.imread(image)
            assert img_rgb is not None, "file could not be read, check with os.path.exists()"
            img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
            template = cv.imread(main_image, cv.IMREAD_GRAYSCALE)
            assert template is not None, "file could not be read, check with os.path.exists()"
            w, h = template.shape[::-1]
            res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
            threshold = 0.5
            loc = np.where( res >= threshold)
            #print(loc)
            with open('test.npy', 'rb') as f:
                if res in f:
                    pass
                else:
                    with open('test.npy', 'wb') as f:
                        np.save(f, res)
            
            if len((loc[0])) > 0:
                main_response = True
                print("Imgae Found!")
            else:
                main_response = False
                print("Imgae Not Found!")
            """for pt in zip(*loc[::-1]):
                cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (255,255,255), 2)"""
            #cv.imwrite('res.png',img_rgb)
        except Exception as e:
            print(e)
            main_response = False
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)

        return main_response

compare_image()

with open('test.npy', 'rb') as f:
    a = np.load(f)
print(a)