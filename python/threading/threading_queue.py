# -*- coding: utf-8 -*-

# 代码实现功能，将数据列表中的数据传入，使用四个线程处理，将结果保存在Queue中，线程执行完后，从Queue中获取存储的结果
import threading
import time
from queue import Queue


# 函数的参数是一个列表l和一个队列q，函数的功能是，对列表的每个元素进行平方计算，将结果保存在队列中
def job(l,q):
    for i in range (len(l)):
        l[i] = l[i]**2
    q.put(l)   #多线程调用的函数不能用return返回值


# 在多线程函数中定义一个Queue，用来保存返回值，代替return，定义一个多线程列表，初始化一个多维数据列表，用来处理：
def multithreading():
    q =Queue()
    threads = []
    data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
    #在多线程函数中定义四个线程，启动线程，将每个线程添加到多线程的列表中
    for i in range(4):   #定义四个线程
        t = threading.Thread(target=job,args=(data[i],q)) #Thread首字母要大写，被调用的job函数没有括号，只是一个索引，参数在后面
        t.start()#开始线程
        threads.append(t) #把每个线程append到线程列表中
    #分别join四个线程到主线程
    for thread in threads:
        thread.join()
    #定义一个空的列表results，将四个线运行后保存在队列中的结果返回给空列表results
    results = []
    for _ in range(4):
        results.append(q.get())
    print(results)

if __name__=='__main__':
    multithreading()
