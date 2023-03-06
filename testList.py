'''
squared = [x ** 2 for x in range(4)]
for i in squared:
    print i



foo = "abcdef"
for j in range(len(foo)):
    print "(%d)" % (j+1),foo[j] 



sqdEvens = [y ** 2 for y in range(100) if not y % 2]
for k in sqdEvens:
    print k,
'''

counter = 0
str = 'adfeafg23tm'
while counter < len(str):
    print "(%d)" %(counter+1),str[counter]
    counter += 1