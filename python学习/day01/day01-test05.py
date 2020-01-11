#字典dict
dict={'A':1,'B':2,'C':3}
print(dict['A'])
print('C' in dict)    #判断C是否在dict的key
print('D' in dict)

#删除字典中的key   pop(key)
dict.pop('C')
print(dict)
#dict是用空间换时间的方法
#和list比较，dict有以下几个特点：
#查找和插入的速度极快，不会随着key的增加而变慢；
#需要占用大量的内存，内存浪费多。
#通过key计算位置的算法称为哈希算法
#key是不可变的


#set  不能重复的key的集合  ，不储存value
s=set([1,2,1,2,3,3])
print(s)
#add(key) 方法添加元素到set中
s.add(4)
print(s)
#remove(key)删除set中的元素
s.remove(4)
print(s)
#set可以看成是数学意义上无序和无重复元素的集合