while True:
    ipt = input()
    if ipt == '0':
        break
    else:
        if ipt == ipt[::-1]:
            print('yes')
        else:
            print('no')