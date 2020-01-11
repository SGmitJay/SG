#定义函数
import  math
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TimeoutError('bad operand type')
    if x>0:
        return x
    else:
        return -x

print(my_abs(-3))
print(max(1,2,4,5,6,7))

#python函数返回其实是一个tuple

#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0的两个解
def quadratic(a,b,c):
    x1=((-1)*b+math.sqrt(b*b-4*a*c))/2*a
    x2=((-1)*b-math.sqrt(b*b-4*a*c))/2*a
    return x1,x2

x1,x2=quadratic(1,-3,2)
print(x1)
print(x2)

#power(x,n)
def power(x,n):
    s=1
    for i in range(n):
        s=s*x
    return s

print(power(2,4))