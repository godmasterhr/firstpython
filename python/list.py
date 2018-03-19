#!/usr/lib/python
l = ['a','b',3,'c','d']
print("list的长度为: %d" % len(l))
print(l)

'''获取列表的某些值'''
print(l[0])
print(l[0:3])
print(l[0:])
print("----------")
print(l[4:5])



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

'''count方法  参数为元素值   返回列表中有多少个元素'''
count = l.count(0)
print(count)

'''index()方法 可给定三个参数 值  开始查询下标 结束查询下表 返回列表中这个值所在的下标'''
index = l.index('d');
print(index)

'''insert()方法  可以在给定下标之前 插入值'''
l.insert(2,'呵呵');
print(l)

'''reverse 列表翻转'''
l.reverse();
print(l)

'''remove方法  从队列中把值删除'''
l.remove("呵呵");
print(l)

'''获取列表长度'''
len = len(l)
print(len)



'''元组'''
tuple = ('aaa','bbb','ccc')
print(tuple[0])


ll = list(tuple)
print(ll)