#进程间通信
#在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
from multiprocessing import  Process,Queue
import os,time,random

#写数据进程执行的代码
def write(q):
    print('Process to write :%s' % os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...' %value)
        q.put(value)
        time.sleep(random.random())

#读数据进程执行的代码
def read(q):
    print('Process to read :%s' %os.getpid())
    while True:
        value=q.get(True)
        print('Get %s from queue...' %value)

if __name__=='__main__':
    q=Queue()                                    #父进程创建queue，并传给各个子进程
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    #启动子进程pw,写入
    pw.start()
    #启动子进程pr，读取
    pr.start()
    #等待pw结束
    pw.join()
    #进程pr是死循环，无法等待其结果，只能强行终止
    pr.terminate()

