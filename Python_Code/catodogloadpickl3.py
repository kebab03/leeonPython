# inizio file 3
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
import pickle
import time

NAME = "Cats-vs-dogs-CNN-64x3-{}".format(int(time.time()))
tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))
pickle_in = open("X1.pickle","rb")
X = pickle.load(pickle_in)

pickle_in = open("y1.pickle","rb")
y = pickle.load(pickle_in)

X = X/255.0
print('type',type(X), 'sha diX:', X.shape)
print('X da vede shp', X.shape)
#Conv2D è un layer k acetta  img 1.20 min di keras with
# tensorflo di frecamp gal gadot
#3, 3 è il size di kernal  relu è una funzione
model = Sequential()
units=64
model.add(Conv2D(units, (3, 3), input_shape=X.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
# 1h21min freecod  keras with tensor   è un altro layer   dimezza la dimensione di imag

#ora inizio il 2 nd layer
model.add(Conv2D(units, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
# cui trasformo in 1 d layer
model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
#
# model.add(Dense(64))
# model.add(Activation('relu'))
#  sopra act è agit dop è output
#  la seguente..nota bene il numero 1 di dense indica il numero di uscite 1h4235 min  frecam keras tensor
model.add(Dense(1))
model.add(Activation('sigmoid'))
#softmax  puo dare probabilita di output
#con compile inizio a fare il trainning
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])
#1h2431 min con bainary  cros ho 1 solo output , mentre cn
#categorical crossentropy ho piu valori in out put
# in caso di una sola uscita con bainary , l'uscita è pesato con sigmoid e non piu con softmax
model.fit(X, y, batch_size=32, epochs=10, validation_split=0.3,
          callbacks=[tensorboard] )

#cui che 32
# dice quanti ne passano nel
# algoritmo  ora posso fare il train



# fine file 3
model.save('64x3-CNN2.model')
# inizio file 4

