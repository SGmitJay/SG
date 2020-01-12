#面向对象编程
class Student(object):    # object这个参数是指从哪个类继承下来的
    #__init__方法的第一个参数永远是self，表示创建的实例本身，
    # 因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身
    #但是self不需要传
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def print_score(self):
        print('%s:%s'%(self.name,self.score))

bart=Student('Bart Simpson',59)
lisa=Student('Lisa Simpson',87)
bart.print_score()
lisa.print_score()


#一个类要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__,在python中，实例的变量名如果以__开头，就成了一个私有变量
#私有变量只有内部能访问，外部不能访问

class Student01(object):
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    def print_score(self):
        print('%s:%s'%(self.__name,self.__score))
#get 和set
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_name(self,name):
        self.__name=name
    def set_score(self,score):
        self.__score=score

bart=Student01('Bart Simpson',59)
print(bart.get_name())
print(bart.get_score())


#练习
#为了统计学生人数，可以给Student类增加一个类属性，每创建一个实例，该属性自动增加：
class Student02(object):
    count=0
    def __init__(self,name):
        self.name=name
        Student02.count+=1
a=Student02('A')
b=Student02('B')
c=Student02('C')
#以上创建了三个实例
print(Student02.count)
