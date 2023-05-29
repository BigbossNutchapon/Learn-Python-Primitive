#สร้างภาพวาด 4เหลี่ยมจตุรัส

num = int(input("ป้อนขนาด: "))
for row in range(num):
    for column in range(num):
        if column % 2 ==0:
            print("x",end='')
        else:
            print('o',end='')
    print('')