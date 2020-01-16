import numpy as np
import parsData
import pandas as pd
from tensorflow.keras.datasets import boston_housing
from tensorflow.keras.models import Sequential #модуль для представления нейронной сети в которой слои идут последовательно
from tensorflow.keras.layers import Dense#т.к. у нас полносвязная нейронная сеть нам нужно подключить модуль Dense (так в keros называютчя такие сети)
import tensorflow as tf

def predict():
    model=tf.keras.models.load_model('NNetwork.h5')
    np.random.seed(42)



    # (x_train, y_train), (x_test, y_test) = boston_housing.load_data()

    numbers = parsData.get_data_wanted()

    x_train, y_train, x_test, y_test =parsData.getData()

    mean = x_train.mean(axis=0)
    std = x_train.std(axis=0)
    x_train-=mean
    x_train/=std
    x_test-=mean
    x_test/=std

    pred=model.predict(x_test)
    sum = 0
    for number in numbers:
        print('iteration - ',number," Предсказанные пропуски:", pred[number][0], ", правильные пропуски:", y_test[number])
        sum += abs(pred[number][0])
    return(round(sum))
