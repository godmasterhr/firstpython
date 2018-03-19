#!/usr/lib/python
# -*- coding: utf-8 -*-
'''编码要在文件开头指定    #coding=utf-8  = 号两边不要空格  或者   # -*- coding: utf-8 -*-  '''

print("hello world!")

print("hello\n"
      'world')


x = input("请输入你的年龄：")
x=int(x)
print(isinstance(x,int))

if x>=20:
    print('你是成年人，你的年龄是：%d' % x)
else:
    print("你是未成年人，你的年龄是：%d,%s" %(x,'hr'))



var1 = 1
print(var1)
del var1   #删除var1变量
# print(var1)




