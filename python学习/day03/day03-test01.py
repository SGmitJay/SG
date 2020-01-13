#在python中,定义了一个类，创建了实例后，我们可以给该实例绑定任何属性和方法，这是动态语言的灵活性
#我们不仅可以给实例绑定属性和方法，还可以对已经创建的类绑定属性和方法，所有的实例可调用
#如果我们要限制实例的属性，只允许对类的实例动态添加我们限制的属性
#使用__slots__变量来限制类实例能添加的属性



#使用@property  装饰器
class Student(object):
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer')
        if value < 0 or value >100:
            raise ValueError('score must between 0~100')
        self.__score=value

s=Student()
s.score=60
print(s.score)
#s.score=999


#利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self,width):
        self.__width=width
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self,height):
        self.__height=height
    @property     #只读属性，因为可以通过width和height计算出来
    def resolution(self):
        return self.__height*self.__width


screen=Screen()
screen.width=1024
print(screen.width)
screen.height=768
print(screen.height)
print(screen.resolution)

#python支持多重继承  而java只支持单一继承

#定制类
class Fib(object):
    def __init__(self):
        self.a,self.b=0,1    #初始化
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b    #计算下一个值
        if self.a>100:
            raise StopIteration()
        return self.a
    def __getitem__(self, n):
        a,b=1,1
        for x in range(n):
            a,b=b,a+b
        return a
for n in Fib():    #打印0~100之间的斐波拉契数
    print(n)
f=Fib()
print(f[5])