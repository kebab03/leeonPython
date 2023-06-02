globals().clear()
import numpy as np
import cv2

#events = [i for i in dir(cv2) if 'EVENT' in  i]
#print(events)
# https://www.youtube.com/watch?v=wSjB_iaQ1wE&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=12
path ='C:/Users/leeon/PycharmProjects/upl/1.jpg'



def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ' ,y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', '+ str(y)
        cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)
        cv2.imshow('image', img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        strBGR = str(blue) + ', '+ str(green)+ ', '+ str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 2)
        cv2.imshow('image', img)

#img = np.zeros((512, 512, 3), np.uint8)
# pathImage = "1.jpg"
pathImage = "C:/Users/leeon/PycharmProjects/upl/1.jpg"
img = cv2.imread(pathImage)
img_Re=cv2.resize(img,(800,880))

print(img.shape)
cv2.imshow('image_Resize', img_Re)
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()