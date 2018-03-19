#!/usr/lib/python
# -*- coding: utf-8 -*-



'''字典  相当于java中的map'''
d={1:'a',2:'b','c':'d'}
d[1]='aa'
print(2 in d)
print(d.get(3))
d.pop(2)
print(d)

'''获取key集合   value集合'''
print(len(d.keys()))
print(d.values())


'''获取entry集合'''
set = d.items()
print(set)



