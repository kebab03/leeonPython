import cv2
import numpy as np
from matplotlib import pyplot as plt
direc ='C:/Users/leeon/Pictures/Atest-tesseract/'
name='image'
name_templet=name+'_templet'
path_src= direc+name+'.jpg'
path_templet=direc+name_templet+'.jpg'


print(path_templet)

template_Old = cv2.imread(path_templet, 0)
# template=cv2.resize(template_Old,(100,50))
# template=cv2.resize(template_Old,(320,80))
template=cv2.resize(template_Old,(100,60))
def nothing (x):
    print(x)
# grayImage = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
cv2.namedWindow("In_Trackbars_Window")
cv2.resizeWindow("In_Trackbars_Window", 360, 240)
cv2.createTrackbar("Threshold1", "In_Trackbars_Window",0,255, nothing)
cv2.createTrackbar("Threshold2", "In_Trackbars_Window",0,255, nothing)


so=0

while   True:
    # Threshold1 = cv2.getTrackbarPos("Threshold1", "In_Trackbars_Window")
    Threshold2 = cv2.getTrackbarPos("Threshold2", "In_Trackbars_Window")
    Threshold1=120
    # Threshold2=245
    print('Threshold1:', Threshold1)
    print('Threshold2:', Threshold2)
    (thresh, blackAndWhiteImage) = cv2.threshold(template_Old, Threshold1, Threshold2, cv2.THRESH_BINARY)
    cv2.imshow('Black white image', blackAndWhiteImage)

    print('so:',str(so))
    so=so+1
    cv2.waitKey(0)

cv2.destroyAllWindows()
#     key=cv2.waitKey(1)
#     if key==27:
#         break
# cv2.destroyAllWindows()