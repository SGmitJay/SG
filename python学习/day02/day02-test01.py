#可变参数
#方法一  把参数作为一个list或tuple传进来
def calc01(numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
#调用的时候，需要先组装一个list或tuple
print(calc01([1,2,3]))

#方法二 定义可变参数
def calc02(*numbers):
    sum=0
    for n in numbers:
        sum=sum+n*n

    return sum
print(calc02(1,2,3,4,5))

#*numbers表示把这个list的所有元素作为可变参数传进去


#关键字参数
def person(name, age ,**kw):
    print('name:',name,'age:',age,'other:',kw)

person('SG',21)
person('SG',21,city='wuhan')
person('SG',21,city='wuhan',school='hust')
#也可以事先组装一个dict
d={'city':'wuhan','school':'hust'}
person('SG',21,**d)

#参数组合
#在python中定义函数，可以用必选参数，默认参数，可变参数，关键字参数，命名关键字参数
#注意参数使用顺序必须是必选参数，默认参数，可变参数，命名关键字参数，关键字参数