#传入函数  把函数作为参数传入，这样的函数称为高阶函数

def add(a,b,f):
    return f(a)+f(b)

print(add(-4,3,abs))

#map()接受两个参数 一个是函数  一个是Iterable
#map将传入的函数依次作用到序列的每一个元素，并把结果作为新的Iterable返回
def f(x):
    return x*x
r=map(f,list(range(1,5)))
print(list(r))
print(list(map(str,list(range(1,5)))))


#filter()函数用于过滤序列
#和map类似，filter也接收一个函数和一个序列
#注意：与map不同的是filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False来保留还是丢弃该元素
def odd(n):
    if n%2==1:
        return n

print(list(filter(odd,list(range(0,10)))))


#用filter求素数   埃氏筛法

#注意，这是一个生成器，并且是一个无限序列
def _odd_iter():
    n=1
    while True:
        n=n+2
        yield n

#定义一个筛选函数
def _not_divisible(n):
    return lambda x:x % n>0


#定义一个生成器，不断返回下一个素数
def primes():
    yield 2
    it=_odd_iter()    #初始序列
    while True:
        n=next(it)    #返回序列的第一个数
        yield n
        it=filter(_not_divisible(n),it)

for n in primes():
    if n<100:
        print(n)
    else:
        break


#排序sorted()
L=[36,5,-12,9,-21]
print(sorted(L))
print(L)
#接收一个key实现自定义排序
print(sorted(L,key=abs))

L=['bob', 'about', 'Zoo', 'Credit']

#默认情况下，对字符串排序，按照ASCII码来实现
print(sorted(L))
#忽略大小写
print(sorted(L,key=str.lower))
#反向排序
print(sorted(L,key=str.lower,reverse=True))

#练习
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(L[0])
def by_name(t):
    return t[0]
def by_score(t):
    return t[1]
print(sorted(L,key=by_name))
print(sorted(L,key=by_score))
