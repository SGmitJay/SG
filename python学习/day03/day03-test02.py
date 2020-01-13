#枚举类
from enum import Enum,unique
#Month类型的枚举类
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name,member in Month.__members__.items():
    print(name,'=>',member,',',member.value)   #value属性是自动赋给成员的int常量

 #unique装饰器可以帮助我们检查没有重复值
@unique
class Weekday(Enum):
    sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6
