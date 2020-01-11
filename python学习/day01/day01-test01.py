# a=10
# if a>0:
#     print(-a)
# else:
#     print(a)


#这种变量本身类型不固定的语言称之为动态语言。与之对应是静态语言。
# a=123
# print(a)
# a='ABC'
# print(a)
# b=a
# a='BCD'
# print(b)
# print(a)

#python 的除法
#结果是浮点数
print(10/3)
print(9/3)
#结果是整数
print(10//3)

#ASCII  大小写英文字母，数字和一些符号  一个字节
#GB2312  编入中文
#Unicode 把所有语言都统一到一套编码
#UTF-8 为了节约空间
#UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节


#格式化字符串
print('Hi,%s have $%d.'%('SG',10000000))
