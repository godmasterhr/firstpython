#!/usr/lib/python
# -*- coding: utf-8 -*-

import time


'''时间戳'''
t = time.time()
print("时间戳",t)


'''本地时间 '''
localtime = time.localtime(time.time())
print(localtime)

tt = time.localtime()
print(tt)

'''格式化时间'''

yy = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(yy)


'''互相转化  先弄成时间戳 怎么都好转'''
a = "Sat Mar 28 22:24:24 2016"
ttt = time.strptime(a,"%a %b %d %H:%M:%S %Y")
now = time.strftime("%Y-%m-%d %H:%M:%S",ttt)
print(now)
