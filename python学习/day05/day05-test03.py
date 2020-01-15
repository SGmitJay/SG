#collections是Python内建的一个集合模块，提供了许多有用的集合类。
from collections import namedtuple
#namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素
#nametuple('名称'，'属性list')
Point=namedtuple('Point',['x','y'])
p=Point(1,2)
print(p.x)
print(p.y)
print(isinstance(p,tuple))
print(isinstance(p,Point))


#deque是高效实现插入和删除操作的双向列表，适用于队列和栈
#deque除了实现list的append()和pop(),还支持appendleft()和popleft(),往头部添加或删除元素
from collections import  deque
m=deque(['A','B','C'])
m.append('X')
m.appendleft('Y')
print(m)

#defaultdict
from collections import defaultdict
dd=defaultdict(lambda :'N/A')
dd['key1']='abc'
print(dd['key1'])
print(dd['key2'])


#OrderedDict保持dict中key的顺序
from collections import  OrderedDict
d=dict([('a',1),('b',2),('c',3)])
print(d)
#注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
od=OrderedDict([('a',1),('c',3),('b',2)])
print(od)
