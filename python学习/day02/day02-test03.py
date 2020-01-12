def f1(n):
    L=[]
    while n>=0:
        L.append(n)
        n=n-2
    return L
print(f1(10))

#切片
L=['a','b','c','d']
print(L[1:3])
L=list(range(100))
print(L[0:10])
print((L[:10]))
print(L[-10:])
print(L[-10:0])
print(L[-10:-1])

#前十个数，每两个取一个
print(L[:10:2])
#L中所有数，间隔10取一个
print(L[::10])

L=[1,2,3]
print(L[1:len(L)])
print(L[-1:])
print(L[:-1])
#字符串也能看作是一种list
#python 没有针对字符串的截取函数，只需要一个切片就能完成。

#练习  利用切片操作，实现一个trim()函数，去除字符串首尾的空格
def trim(s):
    if s[0:1]==' ':
        s=s[1:]
        return trim(s)

    elif s[-1:]==' ':
        s=s[:-1]
        return trim(s)
    else:
        return s



L1='    hello '
L2='   hello    world'
print(trim(L1))
print(trim(L2))

#迭代
#python的for 循环不仅可以可以用在list或者tuple,还可以作用在其他可迭代对象
d={'a':1,'b':2,'c':3}
#在默认情况下，dict迭代是key
for n in d:
    print(n)
#如果要迭代value
for value in d.values():
    print(value)
#如果key ,value一起迭代
for key ,value in d.items():
    print(key,value)

#判断一个对象是否可迭代
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance([1,2,3],Iterable))
print(isinstance(123,Iterable))

#Python内置的enumerate函数可以把一个list变成索引-元素对
for key,value in enumerate(['A','B','C']):
    print(key,value)
#迭代--元素本身

#-----
for x,y in [(1,1),(2,4),(3,3)]:
    print(x,y)

#迭代法寻找list中的最大最小值
def findMinAndMax(L):
    max=L[0]
    min=L[0]
    for i in L:
        if i>max:
            max=i
        if i<min:
            min=i
    return (max,min)
L=[1,2,3,4,5]
print(findMinAndMax(L))


#列表生成器
print([x*x for x in range(1,11)])
print([x*x for x in range(1,11) if x%2==0])

#两层循环 全排列
print([m+n for m in 'ABC'for n in 'XYZ'])

#练习
