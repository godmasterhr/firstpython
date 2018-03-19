#!/usr/lib/python
l = ['a','b',3,'c','d']
print("list的长度为: %d" % len(l))
print(l)
'''pop方法是出栈 并返回元素的值  不加下标队尾元素出栈，加上下标  下标元素出栈'''
# l.pop()
# print(l)
# a= l.pop(1)
# print(a)
# print(l)

'''append方法是添加元素  默认队尾添加'''
# l.append('e');
# print(l)

'''clear方法是清空元素'''
# l.clear()
# print(l)

'''copy方法是克隆一个一模一样的列表'''
lc = l.copy()
print(lc)
