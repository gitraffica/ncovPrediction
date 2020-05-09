import time
import keras
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense, Activation, Dropout

class NN:

    def __init__(self, data, LSTMCount = 2, Units = 128):
        data = np.array(data)
        self.Xtrain = data[:, :-1]
        tmp = np.array([data[:, -1]])
        self.Ytrain = []
        for i in tmp[0]:
            self.Ytrain.append([i])
        self.Xtrain = np.reshape(self.Xtrain, (self.Xtrain.shape[0], 1, self.Xtrain.shape[1]))
        
        self.Xtrain = np.array(self.Xtrain)
        self.Ytrain = np.array(self.Ytrain)
        self.model = Sequential()
        print((1, len(data[0]) - 1))
        for i in range(LSTMCount - 1):
            self.model.add(LSTM(input_shape = (1, len(data[0]) - 1), units = Units, return_sequences = True))
            self.model.add(Dropout(0.2))

        self.model.add(LSTM(input_shape = (len(data), len(data[0]) - 1), units = Units, return_sequences = False))
        self.model.add(Dropout(0.2))

        self.model.add(Dense(units = Units, activation = 'relu'))
        self.model.compile(loss = 'sparse_categorical_crossentropy', optimizer = 'adam')
        self.model.summary()
    
    def train(self):
        my_callbacks = [
            tf.keras.callbacks.ModelCheckpoint(filepath='model.{epoch:02d}-{val_loss:.2f}.h5'),
        ]
        self.model.fit(self.Xtrain, self.Ytrain, batch_size = 1, epochs = 100, validation_split = 0.2, callbacks = my_callbacks)
    
    def predict(self, data):
        return self.model.predict(data)
