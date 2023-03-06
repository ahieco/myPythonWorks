#coding=gbk
fileName = raw_input("Enter the file name: ")
fobj = open(fileName, 'r')
for eachLine in fobj:
    print eachLine,
fobj.close()
