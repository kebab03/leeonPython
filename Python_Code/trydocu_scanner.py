import cv2
import numpy as np
pathImage = "1.jpg"





def empty(a):
    pass


cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold1", "Parameters", 200, 255, empty)
cv2.createTrackbar("Threshold2", "Parameters", 200, 255, empty)



def stackImages( scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len (imgArray[x][y].shape)==2:imgArray[x][y]=cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank] * rows
        hor_con = [imageBlank] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if  imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                 imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len (imgArray[x].shape)==2:imgArray[x]=cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver


while True:
    img = cv2.imread(pathImage)
    #imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)  # ADD GAUSSIAN BLUR
    imgBlur = cv2.GaussianBlur(img, (7, 7), 1)  # ADD GAUSSIAN BLUR Trackbars
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY) # CONVERT IMAGE TO GRAY SCALE

    Threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    Threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    #thres=utlis.valTrackbars() # GET TRACK BAR VALUES FOR THRESHOLDS
    imgCanny = cv2.Canny(imgGray,Threshold1,Threshold2) # APPLY CANNY BLUR
    #imgThreshold = cv2.Canny(imgBlur,thres[0],thres[1]) # APPLY CANNY BLUR
    #imgCanny
    imgStack = stackImages(0.8,([img,imgGray,imgCanny]))
    cv2.imshow("Result",imgStack)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break