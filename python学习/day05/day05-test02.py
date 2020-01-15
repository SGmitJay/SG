#datetime是python处理日期和时间的标准库
from datetime import datetime     #从datetime模块中导入datetime类

now=datetime.now()    #返回当前时间日期
print(now)
print(type(now))
dt=datetime(2020,1,19,23,35)
print(dt)

#把一个datetime类型转换为timestamp只需要简单调用timestamp()方法
print(dt.timestamp())
#把timestamp转换为datetime
t= 1429417200.0
print(datetime.fromtimestamp(t))     #本地时间
print(datetime.utcfromtimestamp(t))     #utc时间

#str转换为datetime
#字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式。
m=datetime.strptime('2020-1-15 13:25:45','%Y-%m-%d %H:%M:%S')
print(m)

now=datetime.now()
print(now.strftime('%Y %m %d %H:%M:%S'))