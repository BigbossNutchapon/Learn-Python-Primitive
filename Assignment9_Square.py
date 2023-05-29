#สร้างภาพวาด 4เหลี่ยมจตุรัส

num = int(input("ป้อนขนาด: "))
for row in range(num):
    for column in range(num):
        print("x",end='')
    print('')