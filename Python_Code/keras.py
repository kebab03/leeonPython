import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation , Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from random import randint
from sklearn.utils import  shuffle
from sklearn.preprocessing import MinMaxScaler


train_labels = []#categoria  cioè  identifica che cosa è
train_samples = []


for i in range(50):
    # 5 % di giovani ha avuto effetti collaterali
    random_younger = randint(13,64)
    train_samples.append(random_younger)
    train_labels.append(1)#cui ho taggato id di questi giovani

    #5 % di vecchi  che non hanno avuto ettetti colalterali
    random_older = randint(65, 100)
    train_samples.append(random_older)
    train_labels.append(0)
    # cui ho taggato id di
    # questi giovani

for i in range(1000):
    # 95 % di giovani non hanno avuto effetti collaterali
    random_younger = randint(13,64)
    train_samples.append(random_younger)
    train_labels.append(0)#cui ho taggato id di questi giovani

    #95 % di vecchi  che  hanno avuto ettetti colalterali
    random_older = randint(65, 100)
    train_samples.append(random_older)
    train_labels.append(1)


train_labels = np.array(train_labels)
train_samples = np.array(train_samples)
train_labels , train_samples = shuffle(train_labels,train_samples)


scaler = MinMaxScaler(feature_range=(0,1))
scaled_train_samples = scaler.fit_transform(train_samples.reshape(-1,1))
for i in scaled_train_samples:
    print(i)
# physical_devices = tf.config.experimental.list_physical_devices('GPU')
# print("num gpus aviale:",len(physical_devices))
# tf.config.experimental.set_memory_growth(physical_devices[0],True)


model = Sequential([
    Dense(units=16, input_shape=(1,), activation='relu'),

    Dense(units=32,activation='relu'),
    Dense(units=2,activation='softmax')
])#16 è arbitrario
#softmax a la probabilita x ogni classe di giovani  o vecchi
model.summary()
model.compile(optimizer=Adam(learning_rate=0.0001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#ho appena copilato il modello che deve essere trained
#y è target data, batch è il numero di pixel che vengono passati alla volta  al filtro layer
# epochs è il numero di volte che viene trained
model.fit(x=scaled_train_samples,y=train_labels, validation_split=0.1 ,batch_size=10 ,epochs=30,shuffle=True,verbose=2)
#verbose di k posso vedere loputput
# validatio split   toglie una parte di trainning set  x validare il modello cui ho scelto 10%
# viene fatto prima di fare shuffel di train data  ultimi 10%
# 37min

# 43 min  ora inizio a verificare il mio
# codice mettendo dentro i dati veri se riesce a dire il fututo

test_labels = []#categoria  cioè  identifica che cosa è
test_samples = []


for i in range(50):
    # 5 % di giovani ha avuto effetti collaterali
    random_younger = randint(13,64)
    test_samples.append(random_younger)
    test_labels.append(1)#cui ho taggato id di questi giovani

    #5 % di vecchi  che non hanno avuto ettetti colalterali
    random_older = randint(65, 100)
    test_samples.append(random_older)
    test_labels.append(0)
    # cui ho taggato id di
    # questi giovani

for i in range(1000):
    # 95 % di giovani non hanno avuto effetti collaterali
    random_younger = randint(13,64)
    test_samples.append(random_younger)
    test_labels.append(0)#cui ho taggato id di questi giovani

    #95 % di vecchi  che  hanno avuto ettetti colalterali
    random_older = randint(65, 100)
    test_samples.append(random_older)
    test_labels.append(1)


test_labels = np.array(test_labels)
test_samples = np.array(test_samples)
test_labels , test_samples = shuffle(test_labels,test_samples)


scaler = MinMaxScaler(feature_range=(0,1))
scaled_test_samples = scaler.fit_transform(test_samples.reshape(-1,1))#cui ho normalizzato i dati tra -1e 1
for i in scaled_test_samples:
    print(i)






predictions = model.predict(x=scaled_test_samples, batch_size=10, verbose=0)
for i in predictions:
    print(i)

rounded_predictions = np.argmax(predictions,axis=1)
import os.path
if os.path.isfile('nomedimodel.h5') is False:
    model.save('nomedimodel.h5')


from  tensorflow.keras.models import load_model

new_model = load_model('nomedimodel.h5')
new_model.summary()
new_model.get_weights()
new_model.optimizer

from  tensorflow.keras.models import model_from_json
model 2 jason  salva solo la architettur senza weight
json_string = model.to_json()
json_string
model_architecture = model_from_json(json_string)
model_architecture.summary()# ora per devo retrain mentre con .h5 non devo farlo
