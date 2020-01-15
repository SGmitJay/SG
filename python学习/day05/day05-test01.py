#正则表达式 -----匹配字符串
#正则表达式，如果直接给出字符就是精确匹配
#用\d可以匹配一个数字，\w可以匹配字母或数字，.可以匹配任意字符
#要匹配变长的字符，在正则表达式中，*表示任意个字符，+表示至少一个字符，用？表示0个或一个字符。
#用{n}表示n个字符，用{n,m}表示n,m个字符
#例子\d{3}\s+\d{3,8}
#\d{3}表示匹配三个数字
#\s可以匹配一个空格（也包括Tab等空白符），所以\s+表示至少有有一个空格。
#\d{3,8}表示3——8个数字

#进阶---更精确匹配，用[]表示范围
#[0-9a-zA-Z\_]可以匹配一个数字，字母或者下划线
#[0-9a-zA-Z\_]+可以匹配至少由一个下划线组成的字符串
#[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字，字母或者下划线组成的字符串，就是python合法变量
#[a-zA-Z\_][0-9a-zA-Z\_]{0，19} 精确限制了变量的长度是1-20个字符
#^表示行的开头，^\d表示必须以数字开头。
#$表示行的结束，\d$表示必须以数字结束。

#re模块
import re
#match()判断是否匹配，如果匹配成功，返回一个match,否则返回None
t1=re.match(r'^\d{3}\-\d{3,8}$','010-12345')
print(t1)
t2=re.match(r'^\d{3}\-\d{3,8}$','010 12345')
print(t2)


# def match(test):
#     if re.match(r'^\d{3}\-\d{3,8}$',test):
#         print('ok')
#     else:
#         print('failed')
#
# test=input()
# match(test)

#切分字符串
print('a b   c'.split(' '))      #正常的切分代码
print(re.split(r'\s+','a b   c'))      #可以识别连续的空格
print(re.split(r'[\s\,]+', 'a,b,, c  d'))    #可以识别连续的空格和,
print(re.split(r'[\s\,\;]+','a,b;; c  d'))     #可以识别连续的空格和,和；


#分组---提取字串
#用（）表示的就是要提取的分组（group）
m=re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print(m.group(0))   #010-12345
print(m.group(1))     #010
print(m.group(2))   #12345


#贪婪匹配
#正则匹配默认就是贪婪匹配，也就是匹配尽可能多的字符
m=re.match(r'^(\d+)(0*)$','1023000')
print(m.groups())
#由于\d+采用了贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串


#在\d+后面加？就可以让\d+采用非贪婪匹配
x=re.match(r'^(\d+?)(0*)$','1023000')
print(x.groups())


#写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
#someone@gmail.com
#bill.gates@microsoft.com
#bob#example.com
#mr-bob@example.com

def is_valid_email(addr):
    if re.match(r'^[0-9a-zA-Z.]+@(\w+).com$',addr):
        return True
    else:
        return False

print(is_valid_email('someone@gmail.com'))
print(is_valid_email('bill.gates@microsoft.com'))
print(is_valid_email('bob#example.com'))
print(is_valid_email('mr-bob@example.com'))


#提取出带名字的邮箱
