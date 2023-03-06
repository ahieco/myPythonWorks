while True:
    reply = input("Enter a number bigger than 20: ")
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Your input is not digit, please try again: ')
    else:
        if int(reply) < 20:
            print('Too small digit,try again: ')
        else:
            print('%d squared is %d' % (int(reply),int(reply)**2))
print('Thanks,BYE')

