#在函数内部可以调用其他函数，如果一个函数可以在内部调用本身，这个函数就是递归函数。
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(3))

#解决递归调用栈溢出的方法是通过尾递归优化
#尾递归是指在函数返回时，调用自身本身，并且return 语句不能包含表达式。
def function(n):
    return fact_iter(n,1)
def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num*product)

#练习 汉诺塔问题
#实现这个算法简单分为三个步骤
#1）把n-1个盘子从a移到b
#2)把第n个盘子从a移到c
#3)把n-1个盘子从b借助a移到c
def move(n,a,b,c):
    if n==1:
        print(a,'-->',c)
        return    #python函数要么返回预期的值，要么返回None
    move(n-1,a,c,b)
    move(1,a,b,c)
    move(n-1,b,a,c)

move(3,'A','B','C')