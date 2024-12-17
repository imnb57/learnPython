#21
salary = float(input("enter your monthly salary:\n"))
credit = int(input("enter your credit score:\n"))

if salary >= 50000 and credit >= 700:
    print("eligible for a car loan")
else:
    print("not eligible for a car loan")
