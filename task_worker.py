import time,sys,queue,random
from multiprocessing.managers import BaseManager

BaseManager.register('get_task')
BaseManager.register('get_result')

m = BaseManager(address = ('127.0.0.1',9000),authkey=b'abc')

try:
    m.connect()
except:
    print('connect failed')
    sys.exit()

task = m.get_task()
result = m.get_result()

while not task.empty():
    n = task.get(timeout = 1)
    print('run task %d' % n)
    sleeptime = random.randint(0,3)
    time.sleep(sleeptime)
    rt = (n, sleeptime)
    result.put(rt)

if __name__=='__main__':
    pass