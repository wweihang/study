# -*- coding: utf-8 -*-
import threading
"""
获取已激活的线程数         threading.active_count()   
查看所有线程信息            threading.enumerate()
查看现在正在运行的线程      threading.current_thread()
添加线程，threading.Thread()接收参数target代表这个线程要完成的任务，需自行定义
"""

def thread_job():
    print('This is a thread of %s' % threading.current_thread())

def main():
    thread = threading.Thread(target=thread_job,)   # 定义线程 
    thread.start()  # 让线程开始工作
    
if __name__ == '__main__':
    main() 
