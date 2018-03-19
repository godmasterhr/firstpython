#!/usr/lib/python
# -*- coding: utf-8 -*-

d={1:'a',2:'b','c':'d'}
d[1]='aa'
print(2 in d)
print(d.get(3))
d.pop(2)
print(d)
