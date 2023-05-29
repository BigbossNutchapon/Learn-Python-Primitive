num = int(input("ป้อนขนาด: "))
for row in range(num):
    for column in range(num):
        if row == 0 or row == num-1 or column == 0 or column == num-1:
            print("x",end='')
        else:
            print(' ',end='')
    print('')