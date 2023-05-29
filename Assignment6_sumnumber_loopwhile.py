
i = 1
summation = 0
average = 0
count = int(input("ระบุจำนวนรอบ :"))

while i<=count:
    summation+=i
    print(f"รอบที่ = {i} ค่า sum = {summation}")
    i+=1
average=summation/count
print(f"ผลรวมการบวกเลข ={summation}")
print(f"ค่าเฉลี่ย = {average}")