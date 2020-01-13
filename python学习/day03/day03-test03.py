#错误处理

#当我们认为某些代码可能会出错，就可以用try来运行这段代码
#如果执行出错，则后续代码不会继续执行，而是直接跳转错误处理代码,即except语句块
#执行完except语句块，如果有finally语句块，则执行finally语句块

try:
    print('try...')
    r=10/0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END')