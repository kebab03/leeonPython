# Python program to explain cv2.rotate() method

# importing cv2
globals().clear()
import cv2
import numpy as np
# from PIL import Image
import pytesseract
# end = False
end = True
if end:
    # path
    path = r'C:/Users/leeon/Pictures/Atest-tesseract/image.jpg'

    # Reading an image in default mode
    img = cv2.imread(path)
    img_w=cv2.resize(img, (900, 880))
    # Window name in which image is displayed
    window_name = 'Image'

    # Using cv2.rotate() method
    # Using cv2.ROTATE_90_CLOCKWISE rotate
    # by 90 degrees clockwise

    # Displaying the image
    cv2.imshow(window_name, img_w)




    def ocr_core(img):
        text = pytesseract.image_to_string(img)
        return text


    # img = cv2.imread('C:/Users/leeon/Pictures/Atest-tesseract/image.jpg')


    # img = cv2.imread('D:\contro\surf.jpeg')
    def get_grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    def remove_noise(image):
        return cv2.medianBlur(image, 5)


    def thresholding(image):
        return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


    img = get_grayscale(img)
    img = thresholding(img)
    img = remove_noise(img)

    test = ocr_core(img)

    if 'p.' in test:
        end =False
        print(ocr_core(img))
        cv2.waitKey(0)
    else:
        # image = cv2.rotate(image, cv2.cv2.ROTATE_90_CLOCKWISE)
        image = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
        filename = 'image.jpg'

        # Using cv2.imwrite() method
        # Saving the image
        cv2.imwrite(filename, image)
        cv2.waitKey(0)
