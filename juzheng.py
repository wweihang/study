#coding:utf-8
import librosa
import numpy as np

a = np.random.randint(0,10,(5,3))
b = a.reshape(-1).tolist()

c =  np.zeros((a.shape[0] * a.shape[1]))
for raw in range(a.shape[1]):
    for col in range(a.shape[0]):
        c[raw*a.shape[0]+col] = a[col][raw]
c = c.tolist()
print a
print b
print c
