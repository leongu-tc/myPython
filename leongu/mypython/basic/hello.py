#!/usr/bin/python
#coding=utf-8

import time
import calendar



print "Hello, 中国!"

if True:
    print "Answer"
    print "True"
else:
    print "Answer"
    # 没有严格缩进，在执行时会报错
    print "False"

# raw_input("按下 enter 键退出，其他任意键显示...\n")
print '---------'
import sys; x = 'runnnnnn'; sys.stdout.write(x + '\n')
print '---------'
x="a"
y="b"
# 换行输出
print x
print y

print '---------'
# 不换行输出
print x,
print y,

# 不换行输出
print x,y
print '---------'
counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串
print counter
print miles
print name
print '---------'
str1 = 'Hello World!'
print str1           # 输出完整字符串
print str1[0]        # 输出字符串中的第一个字符
print str1[2:5]      # 输出字符串中第三个至第六个之间的字符串
print str1[2:5:2]      # 输出字符串中第三个至第六个之间的字符串
print str1[2:]       # 输出从第三个字符开始的字符串
print str1 * 2       # 输出字符串两次
print str1 + "TEST"  # 输出连接的字符串
print '---------'

list = ['runoob', 786, 2.23, 'john', 70.2]
tinylist = [123, 'john']

print list  # 输出完整列表
print list[0]  # 输出列表的第一个元素
print list[1:3]  # 输出第二个至第三个元素
print list[2:]  # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2  # 输出列表两次
print list + tinylist  # 打印组合的列表
print '---------'
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}

print dict['one']  # 输出键为'one' 的值
print dict[2]  # 输出键为 2 的值
print tinydict  # 输出完整的字典
print str(tinydict)  # 输出完整的字典
print type(tinydict)
print tinydict.keys()  # 输出所有键
print tinydict.values()  # 输出所有值
print '---------'

a = 21
b = 10
c = 0

c = a + b
print "1 - c 的值为：", c

c = a - b
print "2 - c 的值为：", c

c = a * b
print "3 - c 的值为：", c

c = a / b
print "4 - c 的值为：", c

c = a % b
print "5 - c 的值为：", c

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print "6 - c 的值为：", c

a = 10
b = 5
c = a // b
print "7 - c 的值为：", c
print '---------'

a = 21
b = 10
c = 0

if a == b:
    print "1 - a 等于 b"
else:
    print "1 - a 不等于 b"

if a != b:
    print "2 - a 不等于 b"
else:
    print "2 - a 等于 b"

if a <> b:
    print "3 - a 不等于 b"
else:
    print "3 - a 等于 b"

if a < b:
    print "4 - a 小于 b"
else:
    print "4 - a 大于等于 b"

if a > b:
    print "5 - a 大于 b"
else:
    print "5 - a 小于等于 b"

# 修改变量 a 和 b 的值
a = 5
b = 20
if a <= b:
    print "6 - a 小于等于 b"
else:
    print "6 - a 大于  b"

if b >= a:
    print "7 - b 大于等于 a"
else:
    print "7 - b 小于 a"
print '---------'

a = 21
b = 10
c = 0

c = a + b
print "1 - c 的值为：", c

c += a
print "2 - c 的值为：", c

c *= a
print "3 - c 的值为：", c

c /= a
print "4 - c 的值为：", c

c = 2
c %= a
print "5 - c 的值为：", c

c **= a
print "6 - c 的值为：", c

c //= a
print "7 - c 的值为：", c
print '---------'

a = 60  # 60 = 0011 1100
b = 13  # 13 = 0000 1101
c = 0

c = a & b;  # 12 = 0000 1100
print "1 - c 的值为：", c

c = a | b;  # 61 = 0011 1101
print "2 - c 的值为：", c

c = a ^ b;  # 49 = 0011 0001
print "3 - c 的值为：", c

c = ~a;  # -61 = 1100 0011
print "4 - c 的值为：", c

c = a << 2;  # 240 = 1111 0000
print "5 - c 的值为：", c

c = a >> 2;  # 15 = 0000 1111
print "6 - c 的值为：", c
print '---------'

a = 10
b = 20

if a and b:
    print "1 - 变量 a 和 b 都为 true"
else:
    print "1 - 变量 a 和 b 有一个不为 true"

if a or b:
    print "2 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
    print "2 - 变量 a 和 b 都不为 true"

# 修改变量 a 的值
a = 0
if a and b:
    print "3 - 变量 a 和 b 都为 true"
else:
    print "3 - 变量 a 和 b 有一个不为 true"

if a or b:
    print "4 - 变量 a 和 b 都为 true，或其中一个变量为 true"
else:
    print "4 - 变量 a 和 b 都不为 true"

if not (a and b):
    print "5 - 变量 a 和 b 都为 false，或其中一个变量为 false"
else:
    print "5 - 变量 a 和 b 都为 true"
print '---------'

a = 10
b = 20
list = [1, 2, 3, 4, 5];

if (a in list):
    print "1 - 变量 a 在给定的列表中 list 中"
else:
    print "1 - 变量 a 不在给定的列表中 list 中"

if (b not in list):
    print "2 - 变量 b 不在给定的列表中 list 中"
else:
    print "2 - 变量 b 在给定的列表中 list 中"

# 修改变量 a 的值
a = 2
if (a in list):
    print "3 - 变量 a 在给定的列表中 list 中"
else:
    print "3 - 变量 a 不在给定的列表中 list 中"
print '---------'

a = 20
b = 20

if (a is b):
    print "1 - a 和 b 有相同的标识"
else:
    print "1 - a 和 b 没有相同的标识"

if (a is not b):
    print "2 - a 和 b 没有相同的标识"
else:
    print "2 - a 和 b 有相同的标识"

# 修改变量 b 的值
b = 30
if (a is b):
    print "3 - a 和 b 有相同的标识"
else:
    print "3 - a 和 b 没有相同的标识"

if (a is not b):
    print "4 - a 和 b 没有相同的标识"
else:
    print "4 - a 和 b 有相同的标识"
if (a == b):
    print "3 - a 和 b 有相同的标识"
else:
    print "3 - a 和 b 没有相同的标识"
print '---------'
num = 5
if num == 3:            # 判断num的值
    print 'boss'
elif num == 2:
    print 'user'
elif num == 1:
    print 'worker'
elif num < 0:           # 值小于零时输出
    print 'error'
else:
    print 'roadman'     # 条件均不成立时输出
print '---------'
count = 0
while (count < 9):
    print 'The count is:', count
    count = count + 1

print "Good bye!"
print '---------'
i = 1
while i < 10:
    i += 1
    if i % 2 > 0:  # 非双数时跳过输出
        continue
    print i  # 输出双数2、4、6、8、10

i = 1
while 1:  # 循环条件为1必定成立
    print i  # 输出1~10
    i += 1
    if i > 10:  # 当i大于10时跳出循环
        break
print '---------'
count = 0
while count < 5:
   print count, " is  less than 5"
   count = count + 1
else:
   print count, " is not less than 5"
print '---------'
for letter in 'Python':  # 第一个实例
    print '当前字母 :', letter

fruits = ['banana', 'apple', 'mango']
for fruit in fruits:  # 第二个实例
    print '当前水果 :', fruit

print "Good bye!"
print '---------'
fruits = ['banana', 'apple', 'mango']
for index in range(len(fruits)):
    print '当前水果 :', fruits[index]

print "Good bye!"
print '---------'
for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'
print '---------'
print float("1.001")
import math
print dir(math)
print '---------'
a = "Hello"
b = "Python"

print "a + b 输出结果：", a + b
print "a * 2 输出结果：", a * 2
print "a[1] 输出结果：", a[1]
print "a[1:4] 输出结果：", a[1:4]

if ("H" in a):
    print "H 在变量 a 中"
else:
    print "H 不在变量 a 中"

if ("M" not in a):
    print "M 不在变量 a 中"
else:
    print "M 在变量 a 中"

print r'\n'
print R'\n'
print "My name is %s and weight is %d kg!" % ('Zara', 21)

print '---------'

ticks = time.time()
print "当前时间戳为:", ticks
localtime = time.localtime(time.time())
print "本地时间为 :", localtime
localtime = time.asctime(time.localtime(time.time()))
print "本地时间为 :", localtime

# 格式化成2016-03-20 11:45:39形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))

cal = calendar.month(2016, 1)
print "以下输出2016年1月份的日历:"
print cal
print '---------'


# 定义函数
def printme(str):
    "打印任何传入的字符串"
    print str;
    return;

# 调用函数
printme("我要调用用户自定义函数!");
printme("再次调用同一函数");


def ChangeInt(a):
    a = 10

b = 2
ChangeInt(b)
print b  # 结果是 2


def ChangeInt(b):
    b = 10

b = 2
ChangeInt(b)
print b  # 结果是 2
print '---------'


# 可写函数说明
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print "Name: ", name;
    print "Age ", age;
    return;


# 调用printinfo函数
printinfo("zhangsan");
printinfo(age=50, name="miki");
printinfo(name="miki");
print '---------'


# 可写函数说明
def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print "输出: "
    print arg1
    for var in vartuple:
        print var
    return;


# 调用printinfo 函数
printinfo(10);
printinfo(70, 60, 50);
print '---------'
# 可写函数说明
sum = lambda arg1, arg2: arg1 + arg2;

# 调用sum函数
print "相加后的值为 : ", sum(10, 20)
print "相加后的值为 : ", sum(20, 20)


# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2
    print "函数内 : ", total
    return total;


# 调用sum函数
total = sum(10, 20);
print '---------'
total = 0;  # 这是一个全局变量

# 可写函数说明
def sum(arg1, arg2):
    # 返回2个参数的和."
    total = arg1 + arg2;  # total在这里是局部变量.
    print "函数内是局部变量 : ", total
    return total;


# 调用sum函数
sum(10, 20);
print "函数外是全局变量 : ", total
print '---------'
# 导入模块
import support

# 现在可以调用模块里包含的函数了
support.print_func("Runoob")
print '---------'
Money = 2000


def AddMoney():
    # 想改正代码就取消以下注释:
    print globals().keys()
    print locals().keys()
    global Money
    Money = Money + 1


print Money
AddMoney()
print Money
print '---------'
# 打开一个文件
fo = open("/Users/apple/workspaces/github/myPython/README.md", "r+")
print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode
print "末尾是否强制加空格 : ", fo.softspace
str = fo.read(100)
print "读取的字符串是 : ", str
# 关闭打开的文件
fo.close()
print '---------'
try:
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    fh.close()
print '---------'
# 定义函数
def temp_convert(var):
    try:
        return int(var)
    except ValueError, Argument:
        print "参数没有包含数字\n", Argument

# 调用函数
temp_convert("xyz");
print '---------'
# 定义函数
def mye( level ):
    if level < 1:
        raise Exception,"Invalid level!"
        # 触发异常后，后面的代码就不会再执行
try:
    mye(0)            # 触发异常
except Exception,err:
    print 1,err
else:
    print 2
print '---------'
class Networkerror(RuntimeError):
    def __init__(self, arg):
        self.args = arg

try:
    raise Networkerror("Bad hostname")
except Networkerror,e:
    print e.args
print '---------'
print '---------'
print '---------'
print '---------'
print '---------'
print '---------'
print '---------'
print '---------'
print '---------'