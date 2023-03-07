#coding=gbk
#题目3，一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，import math

import math
i = 0

while True:
    i+=1
    a = math.sqrt(i+100)
    b = math.sqrt(i+268)
    if (a != int(a)) and (b != int(b)): continue

    break
print i