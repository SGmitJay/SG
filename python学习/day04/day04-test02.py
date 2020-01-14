#多线程
#Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。
# 绝大多数情况下，我们只需要使用threading这个高级模块。
#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行

import  time,threading

#新线程执行代码
def loop():
    print('thread %s is running...' %threading.current_thread().name)    #当前线程的名字
    n=0
    while n<5:
        n=n+1
        print('thread %s >>>%s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended.' %(threading.current_thread().name))

print('thread %s is running ...' %(threading.current_thread().name))
t=threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()   #等线程结束后在继续往下进行
print('thread %s ended..' %(threading.current_thread().name))


#多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
# 而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
# 因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
#多线程编程，模型复杂，容易发生冲突，必须用锁加以隔离，同时，又要小心死锁的发生。
#Python解释器由于设计时有GIL全局锁，导致了多线程无法利用多核。多线程的并发在Python中就是一个美丽的梦。