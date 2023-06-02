import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import itertools
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation , Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from random import randint
from sklearn.utils import  shuffle
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import confusion_matrix


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
#verbose è 0 xk nella predizione non voglio avere output
for i in predictions:
    print(i)
    #  se ha side effect predizione probabilita è 1 mentre 0 se non ha side effect

rounded_predictions = np.argmax(predictions,axis=1)
for i in rounded_predictions:
    print('se è 0 non ha effetti se è 1 ha side effect:',i
          )
    if i == 0 :
        print('non ha effet:',i)
    if i == 1  :
        print('ha side  effet:', i)
cm = confusion_matrix(y_true=test_labels, y_pred=rounded_predictions)
def plot_confusion_matrix( cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
this funcion prints and plot the confusion matrix
normalization can be applied by setting normalization
    """
    print('arriva')
    plt.imshow('x')

    plt.imshow(cm, interpolation='nearest',cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks,classes,rotation=45)
    plt.yticks(tick_marks,classes)
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:,np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('confusion matrix,without normalization '
              )
    print(cm)
    thresh = cm.max() /2.
    for i, j in itertools.product(range(cm.shape[0]),range(cm.shape[1])):
        plt.text(j,i , cm[i,j],
                 horizontalalignment ="center",
                 color="white" if cm[i,j] > thresh else "black")
        plt.tight_layout()
        plt.ylabel('True label')
        plt.xlabel('predict label')


cm_plot_labels = ['no side effect ','had_side_effects']
plot_confusion_matrix(cm=cm, classes=cm_plot_labels,title='conusion Matrix ')
print('try ')