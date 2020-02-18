# coding:UTF-8
import math
import tensorflow as tf
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt
def softmax(x):
    print(x.shape[1])
    for num in range(x.shape[1]):
        e = np.exp(x[:,num,:])
        print(e.shape)
        #对列求和
        x_sum = np.sum(e,axis=1)[:,np.newaxis]
        b = np.tile(x_sum,(1,np.shape(x[:,num,:])[1]))
        x[:,num,:] = e/b
        print("num:",num,e/b)
    return x



#x1 = np.random.rand(2,4,2)
#print(x1)
#y1 = softmax(x1)
#print(y1)


def draw_plt(predit,label):
    names = range(len(predit))
    names = [str(x) for x in list(names)]
    x = range(len(names))
    plt.plot(x, predit, marker='o', mec='r', mfc='w',label='uniprot90_train')
    plt.plot(x, label, marker='*', ms=5,label='uniprot90_test')
    plt.legend()
    plt.xticks(x, names, rotation=1)
    plt.margins(0)
    plt.subplots_adjust(bottom=0.10)
    plt.xlabel('time') 
    plt.ylabel("value") 
    pyplot.yticks([0.750,0.800,0.850])
    plt.show()
    plt.title("A simple plot") 
    #plt.savefig('D:\\f1.jpg',dpi = 900)


y_train = [0.840,0.839,0.834,0.832,0.824,0.831,0.823,0.817,0.814,0.812,0.812,0.807,0.805]
y_test  = [0.838,0.840,0.840,0.834,0.828,0.814,0.812,0.822,0.818,0.815,0.807,0.801,0.796]
draw_plt(y_train,y_test)
draw_plt(y_train,y_test)

