#หาตัวเลขมาก/น้อย

num1 = int(input("Enter your number1: "))
num2 = int(input("Enter your number2: "))

if num1>num2:
    print(f"result: {num1} > {num2}")
elif num1<num2:
    print(f"result: {num1} < {num2}")
else:
    print(f"result: {num1} = {num2}")
