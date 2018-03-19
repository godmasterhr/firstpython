#!/usr/lib/python
# -*- coding: utf-8 -*-


var = 100;
sum = 0
while var >0:

    var -= 1
    if var==50:
        continue
    sum +=var
else:
    print("循环结束")
print(sum)
