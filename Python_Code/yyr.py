print(6+9)
import tensorflow.keras as keras
import tensorflow as tf
print('__version__',tf.__version__)
mnist = tf.keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()
#print(x_train[0])
import matplotlib.pyplot as plt
mynum=5
#plt.imshow(x_train[4],cmap=plt.cm.binary)
plt.imshow(x_train[mynum])
plt.show()

#print(y_train[0])
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)
#print('x_train[2]',x_train[2])

#plt.imshow(x_train[0],cmap=plt.cm.binary)
#plt.show()
model = tf.keras.models.Sequential()
#Sequential è feed forwar model come in fig di spegazione di
#https://www.youtube.com/watch?v=wQ8BIBpya2k&list=PLQVvvaa0QuDfhTox0AjmQ6tvTgMBZBEXN&index=1
model.add(tf.keras.layers.Flatten())
#flatten è una fun di keras  che trasforma  il 28x28 di foto in un vettore di colonna di input ome in foto
#di speigazione
#si puo fare ank con reshape questo

#ora aggiungo hidden layer
#128 sono numeri di neuroni
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
#number of classification è output layer k cui vale 10 , xk i numeri sono da 0 a 9
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))
#ora inizia il traning di model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#adam è il piu gradientdiscent   puo essere un ottimizzaretore , adam è piu semplice
model.fit(x_train, y_train, epochs=3)
#fit ha il compito di insegnare al model di riconoscere
val_loss, val_acc = model.evaluate(x_test, y_test)
print('val_loss',val_loss)
print('val_acc',val_acc)
model.save('epic_num_reader.model')
new_model = tf.keras.models.load_model('epic_num_reader.model')
predictions = new_model.predict(x_test)

print('the  firnt prediction is', predictions)

import numpy as np

print('the number predict is ',np.argmax(predictions[7]))
#nota bene cui ho scelto di fare il riconoscimento perr cui che
#ho dato cosa confrontare
plt.imshow(x_test[5],cmap=plt.cm.binary)
plt.show()
print(2+7)