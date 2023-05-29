#เกมทายเลขลูกเต๋า
#1,2,3,4,5,6

import random

my_random = random.randrange(1,7)
count = 1
correct = False
while True:
    num = int(input("ป้อนคำตอบของคุณ: "))
    if num < 0 or count == 3:
        break
    correct = (num == my_random)#true / false
    if not correct:
        if(num>my_random):
            print("คำตอบน้อยกว่า")
        elif(num<my_random):
            print("คำตอบมากกว่า")
    if correct:
        print("ตอบถูกรับไปเลย 1 ล้านบาท")
        break
    count+=1
if not correct:
    print("เสียใจด้วยนะครับ")
    print(f"เฉลย : {my_random}")
    