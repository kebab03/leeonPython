import cv2
import os

DATADIR = r"C:\Users\leeon\Desktop\progettazione libro\progettazione di macchineelettriche\up"

for img in os.listdir(DATADIR):  # iterate over each image per dogs and cats
    try:
        #print(DATADIR+'/'+img)
        img_array = cv2.imread(DATADIR+'/'+img)  # convert to array  COUNTERCLOCKWISE
        image = cv2.rotate(img_array,cv2.ROTATE_90_CLOCKWISE)
        #image = cv2.rotate(img_array, cv2.ROTATE_90_COUNTERCLOCKWISE)

        cv2.imwrite(DATADIR+'/'+img, image)
        # print('Successfully saved')
    except Exception as e:  # in the interest in keeping the output clean...
        pass










