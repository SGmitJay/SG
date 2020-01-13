#对于操作系统来说，一个任务就是一个进程
#有时进程有多个子任务称为线程
from multiprocessing import Process
from multiprocessing import Pool
import  os,time,random

#子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' %(name,os.getpid()))
# if __name__=='__main__':
#     print('Parent process %s .' %os.getpid())
#     p=Process(target=run_proc,args=('test',))   #创建子进程时，只需要传入一个执行函数和函数的参数，创建一个process实例，用start()方法启动
#     print('child process will start.')
#     p.start()
#     p.join()    #join()可以等待子进程结束后再继续往下进行 ，通常用于进程间的同步
#     print('child process end')

# def long_time_task(name):
#     print('Run task %s (%s)...' %(name,os.getpid()))
#     start=time.time()
#     time.sleep(random.random()*3)
#     end=time.time()
#     print('Task %s runs %0.2f seconds.' %(name ,(end-start)))
#
# if __name__=='__main__':
#     print('Parent process %s .' %os.getpid())
#     p=Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task,args=(i,))
#     print('waiting for all subprocess done...')
#     p.close()
#     p.join()
#     print('All subprocessse done.')

#对pool对象join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close(),调用close()之后

#子进程
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)


#进程间通信
#在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
from multiprocessing import  Process,Queue
import os,time,random

#写数据进程执行的代码
def write(q):
    print()