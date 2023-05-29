#c=(f-32)*(5/9)
#f=(c*(9/5)+32)

temp = input("ป้อนอุณหภูมิ (องศา): ")

degree = int(temp[:-1]) #เลขอุณหภูมิ
unit = temp[-1].upper() #หน่วย
result=0
if unit == "C":
    result=(degree*(9/5)+32)
    unit_result = "ฟาเรนไฮน์"
    #แปลงเป็นF
if unit == "F":
    #แปลงเป็นC
    result=(degree-32)*(5/9)
    unit_result = "เซลเซียส"

print(f"แปลงตัวเลข = {degree} {unit} เป็น {result} {unit_result}")