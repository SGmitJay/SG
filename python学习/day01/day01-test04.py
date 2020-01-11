#循环
#遍历list
classmates=['A','B','C']
for classmate in classmates:
    print('Hi',classmate)
#range(n)  从0开始小于n的数
#计算0~100的整数之和  for循环实现
sum01=0
for n in range(101):
    sum01+=n
print(sum01)
#计算0~100的整数之和 while 循环实现
n=100
sum02=0
while n>0:
    sum02+=n
    n=n-1
print(sum02)