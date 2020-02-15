#!/usr/bin/env python3
#-*- coding:utf-8 -*-

'a new git version'

__author__ = 'molength'

from multiprocessing.managers import BaseManager
import time,random,queue
from multiprocessing import freeze_support

MAX_QUEUE_NUM = 10
IP_ADDRESS = ('127.0.0.1',9000)

task_queue = queue.Queue(MAX_QUEUE_NUM)
result_queue = queue.Queue(MAX_QUEUE_NUM)

def get_task():
    return task_queue
    
def get_result():
    return result_queue

def test():
    #把Queue注册到网络上    
    BaseManager.register('get_task',callable=get_task)
    BaseManager.register('get_result',callable=get_result)


    #绑定网络ip:端口，设置验证码
    manager = BaseManager(address=IP_ADDRESS,authkey=b'abc')
    manager.start()

    try:
        task = manager.get_task()
        result = manager.get_result()
        
        for i in range(MAX_QUEUE_NUM):
            print('Put task %d...'%i)
            task.put(i)
            
        while not result.full():
            time.sleep(1)
            
        for i in range(result.qsize()):
            ans = result.get()
            print('Task %d is finished,runtime%d s'%ans)
            
    except:
        print('Manager error')
    finally:
        manager.shutdown()
    
if __name__ == '__main__':
    freeze_support()
    test()