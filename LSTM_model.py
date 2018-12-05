#!/usr/bin/python3.5

import pandas as pd
df = pd.read_pickle('processed_small.pickle')
df = df.dropna()

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
X = df['review']
y = df['star']
onehot = OneHotEncoder()
y = onehot.fit_transform(y.values.reshape(-1,1))
y = y.toarray()
print(y.shape)
X_train, X_test,y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Dense , LSTM , Embedding, Dropout , Activation, Flatten
from tensorflow.keras.layers import Bidirectional, GlobalMaxPool1D
from tensorflow.keras.models import Model, Sequential

max_features = 6000
tokenizer = Tokenizer(num_words=max_features)
tokenizer.fit_on_texts(X_train)
list_tokenized_train = tokenizer.texts_to_sequences(X_train)
maxlen = 500
X_t = pad_sequences(list_tokenized_train, maxlen=maxlen)

embed_size = 128
model = Sequential()
model.add(Embedding(max_features, embed_size))
model.add(Bidirectional(LSTM(32, return_sequences = True)))
model.add(GlobalMaxPool1D())
model.add(Dense(20, activation="relu"))
model.add(Dropout(0.05))
model.add(Dense(5, activation="softmax"))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['categorical_accuracy'])

log_name = 'lstm'

from tensorflow.keras.callbacks import TensorBoard
import time
tb = TensorBoard(log_dir="logs/" + log_name +" "+ time.ctime())
batch_size = 1000
epochs = 20
history = model.fit(X_t,y_train, batch_size=batch_size, epochs=epochs,validation_split=0.1,callbacks=[tb])
model.save("LSTM_model.h5")



import numpy as np
import time
def plot(history, log_name, num_epoch):
    import matplotlib.pyplot as plt
    plt.plot(np.linspace(1, num_epoch, num_epoch),
             np.array(history.history["categorical_accuracy"]), label='Accuracy', color='b')
    plt.plot(np.linspace(1, num_epoch, num_epoch),
             np.array(history.history["val_categorical_accuracy"]), label='Validation Accuracy', color='r')
    plt.legend()
    plt.title("Accuracy" + log_name + time.ctime())
    plt.savefig("./image/Accuracy " + log_name + " " + time.ctime())
    # plt.show()
    plt.close()
    plt.plot(np.linspace(1, num_epoch, num_epoch), np.array(history.history["loss"]), label='Loss', color='b')
    plt.plot(np.linspace(1, num_epoch, num_epoch),
             np.array(history.history["val_loss"]), label='Validation Loss', color='r')
    plt.legend()
    plt.title("Loss" + log_name + time.ctime())
    plt.savefig("./image/Loss " + log_name + " " + time.ctime())
    # plt.show()
    plt.close()

plot(history,log_name,epochs)
