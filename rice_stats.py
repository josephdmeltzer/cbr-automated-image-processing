import cv2
import numpy as np
import argparse
import image_preparer
from scipy.ndimage import interpolation

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,contours,hierarchy = cv2.findContours(thresh,1,cv2.CHAIN_APPROX_SIMPLE)

# for cnt in contours:
    # rect = cv2.minAreaRect(cnt)
    # box = cv2.boxPoints(rect)
    # a, b, c, d = box
    # for p in box:
    # 	print(p)
    # box = np.int0(box)
    # cv2.drawContours(img,[cnt],0,(0,255,0),2)
    # cv2.rectangle(img, (int(x),int(y)), (int(x+w),int(y+h)), (0,255,0),3)

image_preparer.image_show("Title",img)

# h,w,_ = img.shape
# M = cv2.getRotationMatrix2D((w/2,h/2),45,1.0)
# rotated = cv2.warpAffine(img, M, (int(1.42*w),int(1.42*h)))

maxWidth = 0
finalHeight = 0

for a in range(0,20):
	rotated = interpolation.rotate(img,9*a)
	gray2 = cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY)
	_,thresh2 = cv2.threshold(gray2,127,255,cv2.THRESH_BINARY)
	contours2,contours2,hierarchy2 = cv2.findContours(thresh2,1,cv2.CHAIN_APPROX_SIMPLE)
	x,y,w,h = cv2.boundingRect(contours2[0])
	print(w)
	if w>maxWidth:
		print(w)
		maxWidth = w
		finalHeight = h
print(maxWidth)
print(finalHeight)
# cv2.rectangle(img,(),(),(0,255,0),3)


# rotated = interpolation.rotate(img,2*30)
# gray2 = cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY)
# _,thresh2 = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# contours2,contours2,hierarchy2 = cv2.findContours(thresh2,1,cv2.CHAIN_APPROX_SIMPLE)
# x,y,w,h = cv2.boundingRect(contours2[0])

# cv2.rectangle(rotated,(x,y),(x+w,y+h),(0,255,0),3)
# ------------------
# for cnt in contours:
# 	cv2.drawContours(img,[cnt],0,(0,255,0),2)


image_preparer.image_show("Title2",rotated)




