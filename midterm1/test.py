import numpy as np
import pandas as pd

data = pd.read_csv('~/Dev/engr-492/midterm1/train.csv')

data = np.array(data) # convert to numpy array
m, n = data.shape     # m: rows, n: columns
np.random.shuffle(data)

data_train = data[1000:m].T
Y_train = data_train[0]

print("Shape of Y_train: ", Y_train.shape)
print("Size of Y_train: ", Y_train.size)
print("Y: ", Y_train)

one_hot = np.zeros((20, 10))
print("Initial one_hot: ")
print(one_hot)

Z = np.random.randint(0, 9, 20)
print("Z: ", Z)
one_hot[np.arange(20), Z] = 1
print("Updated one_hot: ")
print(one_hot)
