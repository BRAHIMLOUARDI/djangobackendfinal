import numpy as np
from tensorflow import keras

from tensorflow.keras import optimizers
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import load_model

(X_train_data,Y_train_data),(X_test_data,Y_test_data) = mnist.load_data()
N = X_train_data.shape[0] 

X_train = np.reshape(X_train_data,(N,784)) 
X_train = X_train/255 

Y_train = to_categorical(Y_train_data, num_classes=10)

X_test = np.reshape(X_test_data,(X_test_data.shape[0],784))
X_test = X_test/255
Y_test = to_categorical(Y_test_data, num_classes=10)

p = 8
modele = Sequential()

modele.add(Dense(p, input_dim=784, activation='sigmoid'))

modele.add(Dense(p, activation='sigmoid'))

modele.add(Dense(10, activation='softmax'))

modele.compile(loss='categorical_crossentropy',
optimizer='sgd',
metrics=['accuracy'])
print(modele.summary())


modele.fit(X_train, Y_train, batch_size=32, epochs=1)

resultat = modele.evaluate(X_test, Y_test, verbose=0)
print('Valeur de l''erreur sur les données de test (loss):', resultat[0])
print('Précision sur les données de test (accuracy):', resultat[1])


for x in range(25):
    modele.save(f"media/my_model_exp{x}.h5")
    modele.fit(X_train, Y_train, batch_size=32, epochs=1)
    resultat = modele.evaluate(X_test, Y_test, verbose=0)
    print('Valeur de l''erreur sur les données de test (loss):', resultat[0])
    print('Précision sur les données de test (accuracy):', resultat[1])
    modele=load_model(f"media/my_model_exp{x}.h5")
   