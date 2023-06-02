import cv2
import numpy as np
from matplotlib import pyplot as plt
direc ='C:/Users/leeon/Pictures/Atest-tesseract/'
name='image'
name_templet=name+'_templet'
path_src= direc+name+'.jpg'
path_templet=direc+name_templet+'.jpg'

# print(path_src)
# print(path_templet)

img_rgb = cv2.imread(path_src)
print('img_rgb',img_rgb.shape)
img_Re=cv2.resize(img_rgb,(800,880))

# img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

img_gray = cv2.cvtColor(img_Re, cv2.COLOR_BGR2GRAY)
template_Old = cv2.imread(path_templet,0)
# template=cv2.resize(template_Old,(100,50))
# template=cv2.resize(template_Old,(320,80))


(thresh, blackAndWhiteImage) = cv2.threshold(template_Old, 120, 255, cv2.THRESH_BINARY)
# cv2.imshow('Black white image', blackAndWhiteImage)

template=blackAndWhiteImage
# template=cv2.resize(template,(200,60))
cv2.imshow('Black white image_templet', template)

print('template_shape:::',template.shape)
print('img_Re_shape::',img_Re.shape)
print('img_Re_shape[::]::',img_Re.shape[::])
cv2.imshow('template',template)
cv2.imshow('img_Re',img_Re)

cv2.imshow('img_gray',img_gray)
def nothing (x):
    print(x)
# grayImage = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("In_Trackbars_Window")
cv2.resizeWindow("In_Trackbars_Window", 360, 240)
cv2.createTrackbar("Name_of_Threshold1", "In_Trackbars_Window",0,255, nothing)
cv2.createTrackbar("Threshold2", "In_Trackbars_Window", 0, 255, nothing)



# (thresh, blackAndWhiteImage) = cv2.threshold(template_Old, Threshold1, Threshold2, cv2.THRESH_BINARY)
# while   True:
#     (thresh, blackAndWhiteImage) = cv2.threshold(template_Old, 127, 255, cv2.THRESH_BINARY)
#     cv2.imshow('Black white image', blackAndWhiteImage)
# cv2.imshow('Original image', originalImage)

# cv2.waitKey(0)
# cv2.destroyAllWindows()







h, w = template.shape[::]
print('h::',h)
print('w:::',w)
# h=h_s/2
# w=w_s/2

#methods available: ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

res = cv2.matchTemplate(img_gray, template, cv2.TM_SQDIFF)
# For TM_SQDIFF, Good match yields minimum value; bad match yields large values
# For all others it is exactly opposite, max value = good fit.
# plt.imshow(res, cmap='gray')
#print('res:',res)
#print('res_shape:',res.shape)
#print('res_dtype:',res.dtype)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print('min_loc:',min_loc)
top_left = min_loc  #Change to max_loc for all except for TM_SQDIFF
bottom_right = (top_left[0] + w, top_left[1] + h)
cv2.rectangle(img_gray, top_left, bottom_right, 255, 1)  #White rectangle with thickness 2.

cv2.imshow("Matched image", img_gray)
# so=0
# while   True:
#     Threshold1 = cv2.getTrackbarPos("Name_of_Threshold1", "In_Trackbars_Window")
#     Threshold2 = cv2.getTrackbarPos("Threshold2", "In_Trackbars_Window")
#     print('Threshold1:', Threshold1)
#     print('Threshold2:', Threshold2)
#     (thresh, blackAndWhiteImage) = cv2.threshold(template_Old, 120, 255, cv2.THRESH_BINARY)
#     cv2.imshow('Black white image', blackAndWhiteImage)
#
#     print(so)
#     so=so+1
cv2.waitKey(0)

cv2.destroyAllWindows()
#     key=cv2.waitKey(1)
#     if key==27:
#         break
# cv2.destroyAllWindows()