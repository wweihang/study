# -*- coding: utf-8 -*-
import threading
import time

def thread_job():
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1) # 任务间隔0.1s
    print("T1 finish\n")

added_thread = threading.Thread(target=thread_job, name='T1')
added_thread.start()
added_thread.join()
print("all done\n")
print("----------------------\n")


"""
使用join对控制多个线程的执行顺序非常关键。举个例子，假设我们现在再加一个线程T2，T2的任务量较小，会比T1更快完成
join后的程序需要等待该线程结束后才进行

"""

def T1_job():
    print("T1 start\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 finish\n")

def T2_job():
    print("T2 start\n")
    print("T2 finish\n")

thread_1 = threading.Thread(target=T1_job, name='T1')
thread_2 = threading.Thread(target=T2_job, name='T2')
thread_1.start() # 开启T1
thread_2.start() # 开启T2
thread_2.join() # join for T2
thread_1.join() # join for T1
print("all done\n")
print("----------------------\n")
