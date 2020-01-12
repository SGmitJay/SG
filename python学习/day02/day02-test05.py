#匿名函数
#关键字lambda表示匿名函数，前面的x表示函数参数
#匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
print(list(map(lambda x:x*x,list(range(1,5)))))