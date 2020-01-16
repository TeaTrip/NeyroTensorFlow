import numpy as np
import parsData
import pandas as pd
from tensorflow.keras.models import Sequential #модуль для представления нейронной сети в которой слои идут последовательно
from tensorflow.keras.layers import Dense#т.к. у нас полносвязная нейронная сеть нам нужно подключить модуль Dense (так в keros называютчя такие сети)
import tensorflow as tf

model=tf.keras.models.load_model('NNetwork.h5')


def create_csv(seson,id):
    df = pd.read_csv("C:\Program Files\propusk.csv", delimiter=',',names=['id','reason','mounth','day_of_week','time_year','transport','lenght','year','disciplin','last_degree','count_children','alco','smoke','animal','weight','height','index_mass','miss_hour'])
    df[df.time_year == str(seson)][df.id == str(id)].to_csv('new_f.csv')



