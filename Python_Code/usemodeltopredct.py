
import cv2
import tensorflow as tf

CATEGORIES = ["90anti", "90clo","up"]  # will use this to convert prediction num to string value
filepath = 'C:/Users/leeon/Desktop/PetImages'
file='IMG_20180524_144247'
path = filepath+'/'+file+'.jpg'
print(path)
img_array2 = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
# print('img_array2',img_array2)
#se è 1 allora è cat
def prepare(filepath1):
    IMG_SIZE = 200  # 50 in txt-based
    print('filepath1',filepath1)
    img_array = cv2.imread(filepath1, cv2.IMREAD_GRAYSCALE)  # read in the image, convert to grayscale
    # print('img_array1', img_array)

    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize image to match model's expected sizing

    # new dded by me sotto
    # print('new_array1', new_array)
    cv2.imshow('leeon', new_array)
    cv2.waitKey(500)

    # closing all open windows
    cv2.destroyAllWindows()
    # cui ho finito di aggiungere


    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)
    # return the im
# print('tf:',filepath+'/cat6.jpg')
model = tf.keras.models.load_model("64x3-CNN3.model")
prediction = model.predict([prepare(path)])
# REMEMBER YOU'R
print('prediction1 importante, 0 è dog e 1 è cat :',prediction)
print('predictcat:',prediction[0])
#
# prediction = model.predict([prepare('cat.jpg')])
print('prediction:',CATEGORIES[int(prediction[0][0])])
# # will be
# # a list in a list.
# print(CATEGORIES[int(prediction[0][0])])