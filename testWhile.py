'''
while True:
    reply = input("Enter int number(stop for exit): ")
    if reply == "stop":break
    print (int(reply)**2)
print("BYE")
'''

while True:
    reply = input('Enter a date for **2 ("stop" to exit):')
    if reply =='stop':
        break
    elif not reply.isdigit():
        print('Please input a int date, try again')
    elif int(reply) < 20:
        print('Please input a int date equal or bigger than 20')
        
    else:
        print(int(reply)**2)
print('Bye')