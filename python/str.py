#!/usr/lib/python
# -*- coding: utf-8 -*-

'''字符串的操作'''

'''str[a:b]  包含下标为a不包含下标为b    :左边缺省表示左边全要   右边缺省表示右边全要'''
str = 'hello World'
print(str)
len = len(str)-2
print(str[0])
print(str[:len])
print(str[len:])
print((str+" ") * 3)

print("-------------华丽的分割线-------------")

'''index方法 返回给定字符的下标 可以给定开始下标和结束下标查找 没找到会报错'''
index = str.index('Wo')
print(index)

'''count方法 出现字符的次数'''
count = str.count('l')
print(count)

'''capitalize 字符串首字母大写 其他小写'''
c = str.capitalize()
print(c)

'''casefold  也可以吧字符串变小写 对Unicode时候使用'''
b= str.casefold()
print(b)

'''center 定义长度 和左右两边的东西  让字符串放中间   类似上边的华丽的分割线'''
a =  str.center(50,'-')
print(a)

'''判断字符串是否以什么结尾'''
d = str.endswith("d")
print(d)
'''判断字符串以什么开头'''
str.startswith("H")

'''将tab转换成几个空格  默认八个'''
str.expandtabs(2)


'''find寻找子序列的位置 如果没找到返回-1  与index不同的是  index找不到会报错'''
loc = str.find('Wo')
print(loc)


'''
format函数用于字符串的格式化
第一种： 字符串是{变量}    字符串.format(变量名=值)
第二种   字符串是{0},{1}   字符串.format(第0个变量值，第1个变量值)
第三种   字符串是{变量}    字符串.format(**字典) 字典中的key与变量名对应
'''
nstr = "我叫{name},今年23岁了！"
n = nstr.format(name='何睿')
print(n)

nstr = "我叫{name},今年{age}岁了！"
dir = {"name":"何睿","age":"18"}
n = nstr.format(**dir)
print(n)



print("-------------华丽的分割线-------------")


'''split 将字符串按照什么切成list'''
list = str.split(" ")
print(list)


'''upper 转成大写'''
s = str.upper();
print(s)


'''strip去掉两边什么字符  默认空格'''
nnstr = "    sss    "
n = nnstr.strip(s)
ln = nnstr.lstrip()
rn = nnstr.rstrip()
print(n)
print(ln)
print(rn)


'''替换字符'''
s = str.replace("l","b")
print(s)






str.isalnum() #是否全是字母和数字，并至少有一个字符
str.isalpha() #是否全是字母，并至少有一个字符
str.isdigit() #是否全是数字，并至少有一个字符
str.isspace() #是否全是空白字符，并至少有一个字符
str.islower() #S中的字母是否全是小写
str.isupper() #S中的字母是否全是大写
str.istitle() #S是否是首字母大写的