# https: // stackoverflow.com / questions / 50951955 / pytesseract - tesseractnotfound - error - tesseract - is -
# not -installed - or -its -
# not -i
globals().clear()
import cv2
import numpy as np
import pytesseract
from PIL import Image
from pytesseract import image_to_string

# Path of working folder on Disk Replace with your working folder
#src_path = "C:\\Users\\<user>\\PycharmProjects\\ImageToText\\input\\"
src_path = 'C:/Users/leeon/Pictures/Atest-tesseract/image.jpg'
# If you don't have tesseract executable in your PATH, include thefollowing:
#pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR / tesseract'
#TESSDATA_PREFIX = 'C:/Program Files (x86)/Tesseract-OCR'


def get_string(img_path):
    # Read image with opencv
    img = cv2.imread(img_path)

    # Convert to gray
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    # Write image after removed noise
    cv2.imwrite(src_path + "removed_noise.png", img)

    #  Apply threshold to get image with only black and white
    # img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # Write the image after apply opencv to do some ...
    cv2.imwrite(src_path + "thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))

    # Remove template file
    # os.remove(temp)

    return result


print('--- Start recognize text from image ---')
#print(get_string(src_path + "image.png"))
print(get_string(src_path ))

print("------ Done -------")