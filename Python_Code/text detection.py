import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img_a = cv2.imread("C:/Users/leeon/Desktop/PetImages/IMG_20180524_144247.jpg")
IMG_SIZE = 1000
IMG_SIZEh = 600
img = cv2.resize(img_a, (IMG_SIZEh, IMG_SIZE))

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# gray = cv2.cvtColor(img_a, cv2.COLOR_BGR2GRAY)
# adaptive_thershold = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY, 85,11)
# text = pytesseract.image_to_string(img_a)
# text1 = pytesseract.image_to_string(adaptive_thershold)
# result = text1.find('43')

# print('text:', text)
# print('text1:', text1)
# print('text1 typ:', type(text1))
# print(img_a.shape)
# print ("Substring 'p.43' found at index:", result )
#############################################
#### Detecting Characters  ######
#############################################
# IMG_SIZE = 1000
# IMG_SIZEh = 900
# img = cv2.resize(img_a, (IMG_SIZEh, IMG_SIZE))
# print('dopo',img.shape)
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    #     print(b)
    b = b.split(' ')
    #     print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 2)
    cv2.putText(img, b[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 255), 2)

cv2.imshow('img_a', img)
# cv2.imshow('img_gra', gray)
cv2.waitKey(0)