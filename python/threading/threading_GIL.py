# -*- coding: utf-8 -*-
"""
 python 的多线程 threading 有时候并不是特别理想. 最主要的原因是就是, Python 的设计上, 有一个必要的环节, 
就是 Global Interpreter Lock (GIL). 这个东西让 Python 还是一次性只能处理一个东西. 
所以程序 threading 和 Normal 运行了一样多次的运算. 但是我们发现 threading 却没有快多少, 
按理来说, 我们预期会要快3-4倍, 因为有建立4个线程, 但是并没有. 这就是其中的 GIL 在作怪.
有一点要强调的是GIL只会影响到那些严重依赖CPU的程序（比如计算型的）。 如果你的程序大部分只会涉及到I/O，
比如网络交互，那么使用多线程就很合适， 因为它们大部分时间都在等待。

"""

import threading
from queue import Queue
import copy
import time

def job(l, q):
    res = sum(l)
    q.put(res)

def multithreading(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)

def normal(l):
    total = sum(l)
    print(total)

if __name__ == '__main__':
    l = list(range(1000000))
    s_t = time.time()
    normal(l*4)
    print('normal: ',time.time()-s_t)
    s_t = time.time()
    multithreading(l)
    print('multithreading: ', time.time()-s_t)
