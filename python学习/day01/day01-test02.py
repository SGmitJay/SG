#list
#python内置的数据类型
#list是一种有序的集合，可以随时添加和删除其中的元素
classmates=['A','B','C']
print(classmates)
print(classmates[0])
print(classmates[1])
print(classmates[2])
#-1表示倒数第一个
print(classmates[-1])
print(classmates[-2])
#list 是一个可变的有序表，可以往list中追加元素到末尾
classmates.append('D')
print(classmates[3])
#把元素插入到指定的位置
classmates.insert(4,'E')
print(classmates)
#删除末尾元素  pop()
classmates.pop()
print(classmates)
#删除指定位置的元素 pop(i)
classmates.pop(3)
print(classmates)

#有序列表tuple  tuple和listz相似，但是tuple一旦初始化就不能修改
t=(1,2)


