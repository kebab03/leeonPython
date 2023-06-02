import numpy as np
import matplotlib.pyplot as plt
import pickle
import os
import random
import cv2
from tqdm import tqdm

DATADIR = "C:/Users/leeon/Desktop/PetImages"

CATEGORIES = ["Dog", "Cat"]

for category in CATEGORIES:  # do dogs and cats
    path = os.path.join(DATADIR,category)  # create path to dogs and cats
    for img in os.listdir(path):  # iterate over each image per dogs and cats
        img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
       # img_array = cv2.imread(os.path.join(path, img))#cosi ho i colori
        plt.imshow(img_array, cmap='gray')  # graph it
        plt.show()  # display!

        break  # we just want one for now so break
    break  #...and one more!
print('arra',img_array)
print('arry shp',img_array.shape)
IMG_SIZE = 200

new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
print('arry vero shp:',new_array.shape)
plt.imshow(new_array, cmap='gray')
plt.show()

training_data = []

def create_training_data():
    for category in CATEGORIES:  # do dogs and cats

        path = os.path.join(DATADIR,category)  # create path to dogs and cats
        class_num = CATEGORIES.index(category)  # get the classification  (0 or a 1). 0=dog 1=cat
        print('lista :',tqdm(os.listdir(path)))
        for img in tqdm(os.listdir(path)):  # iterate over each image per dogs and cats
            try:
                img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize to normalize data size
                training_data.append([new_array, class_num])  # add this to our training_data
            except Exception as e:  # in the interest in keeping the output clean...
                pass
            #except OSError as e:
            #    print("OSErrroBad img most likely", e, os.path.join(path,img))
            #except Exception as e:
            #    print("general exception", e, os.path.join(path,img))

create_training_data()

print('len',len(training_data))

print('tran data:', training_data)


random.shuffle(training_data)
#for sample in training_data[:10]:
    # print(sample[1])
X = []
y2 = []

for features,label in training_data:
    X.append(features)
    y2.append(label)
print('y:',y2)
print('typey:',type(y2))
y=np.array(y2)
print('typeynew',type(y))
print('first',X[0].reshape(-1, IMG_SIZE, IMG_SIZE, 1))

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)


pickle_out = open("X1.pickle","wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y1.pickle","wb")
pickle.dump(y, pickle_out)
pickle_out.close()

#We can always load it in to our current script, or a totally new one by doing:

# pickle_in = open("X.pickle","rb")
# X = pickle.load(pickle_in)
#
# pickle_in = open("y.pickle","rb")
# y = pickle.load(pickle_in)

# fine file 2

# # inizio file 3
# import tensorflow as tf
# from tensorflow.keras.datasets import cifar10
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
# from tensorflow.keras.layers import Conv2D, MaxPooling2D
#
# import pickle
#
# pickle_in = open("X.pickle","rb")
# X = pickle.load(pickle_in)
#
# pickle_in = open("y.pickle","rb")
# y = pickle.load(pickle_in)
#
# X = X/255.0
# print('type',type(X))
# model = Sequential()
# units=64
# model.add(Conv2D(units, (3, 3), input_shape=X.shape[1:]))
# model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
#
# model.add(Conv2D(units, (3, 3)))
# model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
#
# model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
#
# model.add(Dense(64))
# #è output la seguente
# model.add(Dense(1))
# model.add(Activation('sigmoid'))
#
# model.compile(loss='binary_crossentropy',
#               optimizer='adam',
#               metrics=['accuracy'])
#
# model.fit(X, y, batch_size=32, epochs=5, validation_split=0.1)
#cui che 32
# dice quanti ne passano nel
# algoritmo  ora posso fare il train



# fine file 3

# inizio file 4


#
# from tensorflow.keras.callbacks import TensorBoard
# NAME = "Cats-vs-dogs-CNN"
#
# tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))
#
# model.fit(X, y,
#           batch_size=32,
#           epochs=3,
#           validation_split=0.3,
#           callbacks=[tensorboard])
# import tensorflow as tf
# from tensorflow.keras.datasets import cifar10
# from tensorflow.keras.preprocessing.image import ImageDataGenerator
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
# from tensorflow.keras.layers import Conv2D, MaxPooling2D
# # more info on callbakcs: https://keras.io/callbacks/ model saver is cool too.
# from tensorflow.keras.callbacks import TensorBoard
# import pickle
# import time
#
# NAME = "Cats-vs-dogs-CNN"
#
# pickle_in = open("X.pickle","rb")
# X = pickle.load(pickle_in)
#
# pickle_in = open("y.pickle","rb")
# y = pickle.load(pickle_in)
#
# X = X/255.0
#
# model = Sequential()
#
# model.add(Conv2D(256, (3, 3), input_shape=X.shape[1:]))
# model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
#
# model.add(Conv2D(256, (3, 3)))
# model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
#
# model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
# model.add(Dense(64))
#
# model.add(Dense(1))
# model.add(Activation('sigmoid'))
#
# tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))
#
# model.compile(loss='binary_crossentropy',
#               optimizer='adam',
#               metrics=['accuracy'],
#               )
#
# model.fit(X, y,
#           batch_size=32,
#           epochs=3,
#           validation_split=0.3,
#           callbacks=[tensorboard])
#
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
# from tensorflow.keras.layers import Conv2D, MaxPooling2D
# # more info on callbakcs: https://keras.io/callbacks/ model saver is cool too.
# from tensorflow.keras.callbacks import TensorBoard
# import pickle
# import time
#
# NAME = "Cats-vs-dogs-64x2-CNN"
#
# pickle_in = open("X.pickle","rb")
# X = pickle.load(pickle_in)
#
# pickle_in = open("y.pickle","rb")
# y = pickle.load(pickle_in)
#
# X = X/255.0
#
# model = Sequential()
#
# model.add(Conv2D(64, (3, 3), input_shape=X.shape[1:]))
# model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
#
# model.add(Conv2D(64, (3, 3)))
# model.add(Activation('relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
#
# model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
# model.add(Dense(64))
# model.add(Activation('relu'))
#
# model.add(Dense(1))
# model.add(Activation('sigmoid'))
#
# tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))
#
# model.compile(loss='binary_crossentropy',
#               optimizer='adam',
#               metrics=['accuracy'],
#               )
#
# model.fit(X, y,
#           batch_size=32,
#           epochs=10,
#           validation_split=0.3,
#           callbacks=[tensorboard])