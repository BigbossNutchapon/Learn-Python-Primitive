#แลกเงินและหาจำนวนแบงค์

money = int(input(" Enter your money to exchang money: "))

if money >= 1000:
    print(f"  1000 bath = {money//1000} ใบ")
    money = money % 1000 #หารเอาเศษ

if money >= 500:
    print(f"  500 bath  = {money//500} ใบ")
    money = money % 500

if money >= 100:
    print(f"  100 bath  = {money//100} ใบ")
    money = money % 100
if money >= 50:
    print(f"  50 bath   = {money//50} ใบ")
    money = money % 50
if money >= 20:
    print(f"  20 bath   = {money//20} ใบ")
    money = money % 20
if money <20:
    print(f" เงินสะสมในระบบของท่านมี {money} bath")

else:
    print("  !!plese enter money > 20 bath!!")