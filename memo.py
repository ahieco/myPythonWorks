#coding=gbk
'''
��������򵥵�lambda�÷���lambda�Ǳ��ʽ�����Ǻ�����

s = lambda x,y,z : x+y+z
print s(2,3,5)

#Ĭ�ϲ���Ҳ�ܹ���lambda��ʹ��
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


#lambda ������Ϊ��ת��ʹ�ã�Ҳ������Ϊ���б�
L = [(lambda x: x**2),(lambda x: x**3),(lambda x: x**4)]
for m in L:
    print m(2)
print L[2](3)





key = 'got'
print {'already':   (lambda: 2+2),
     'got':        (lambda: 2*4),
     'one':        (lambda: 2**6)}[key]()


#lambda��������ʵ��ѡ���߼���
lower = (lambda x,y: x if x<y else y)
print lower('bb','aaaa')
'''


