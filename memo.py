#coding=gbk
'''
下面是最简单的lambda用法。lambda是表达式，不是函数。

s = lambda x,y,z : x+y+z
print s(2,3,5)

#默认参数也能够在lambda中使用
f = (lambda a = "anhui, ", b = "imp, ", c = "exp, ": a+b+c)
print f("aniec, ")





lower = (lambda x,y:  x if x < y else y)
print lower("bb", "ae")




def fibs(num):

 result=[0,1]
 for i in range(num-2):
  result.append(result[-2]+result[-1])
 return result

num=input('Enter the number for fibs:')
print fibs(num)
print sum(fibs(num))


#lambda 用来作为跳转表使用，也就是行为的列表
L = [(lambda x: x**2),(lambda x: x**3),(lambda x: x**4)]
for m in L:
    print m(2)
print L[2](3)





key = 'got'
print {'already':   (lambda: 2+2),
     'got':        (lambda: 2*4),
     'one':        (lambda: 2**6)}[key]()


#lambda函数中来实现选择逻辑。
lower = (lambda x,y: x if x<y else y)
print lower('bb','aaaa')
'''


