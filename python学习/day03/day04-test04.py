#IO编程

#读写文件
# f=open('test.txt','r')
# print(f.read())
# f.close()   #关闭文件，文件使用完毕后必须关闭。

#为了保证无论正确还是错误都能正确关闭文件
# try:
#     f=open('test.txt','r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

#with语句自动帮我们调用close()方法
# with open('test.txt','r')as  f:
#     print(f.read())

#readline()可以每次读取一行内容
#readlines()一次读取所有所有内容并按行返回list
#如果文件很小，read()一次性读取，如果不能确定文件大小，反复调用read(size)；如果是配置文件，调用readlines()
with open('test.txt','r') as f:
   # for line in f.readlines():
        #print(line.strip())
    print(f.readline().strip())   #读取一行
    print(f.readline())

with open('test.txt','w') as f:   #以'w'模式写入文件时，如果文件已经存在，会直接覆盖内容
    f.write('hello world 888\n')
#如果我们想在后面追加到文件末尾 'a' append
with open('test.txt','a') as f:
    f.write('hello world 999')
