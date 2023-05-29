#โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
#สมการ BMI = น้ำหนัก(kg) / ส่วนสูง * ส่วนสูง (m)
#input
# weight = int(input("กรุณาป้อนน้ำหนักของคุณ (kg): "))
# height = int(input("กรุณาป้อนส่วนสูงของคุณ (cm) : "))

# #process
# #cm => m
# height = height/100
# #calculate bmi
# bmi = weight/height**2
# #output
# print("BMI = ",bmi)

#Program Calculate BMI Ver.Modified
weight = int(input("กรุณาป้อนน้ำหนักของคุณ (kg): "))
height = int(input("กรุณาป้อนส่วนสูงของคุณ (cm) : "))/100

bmi = weight/(height**2)

if bmi < 18.5 :
    result = "ต่ำกว่าเกณฑ์"
elif bmi >= 18.5 and bmi <=22.9 :
    result = "สมส่วน"
elif bmi >= 23 and bmi <=24.9 :
    result = "น้ำหนักเกิน"
elif bmi >= 25 and bmi <=29.9 :
    result = "โรคอ้วนระดับ1"
elif bmi > 30:
    result = "โรคอ้วนระดับอันตราย"
else:
    result = "ไม่ทราบค่าชัดเจน"

print(f"ค่า BMI = {bmi} ผลคือ= {result}")
