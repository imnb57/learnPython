#10
marks = int(input("Enter your marks : "))

if 90 <= marks <= 100:
    print("Grade: A")
elif 80 <= marks <= 89:
    print("Grade: B")
elif 70 <= marks <= 79:
    print("Grade: C")
elif 0 <= marks < 70:
    print("Grade: Fail")
else:
    print("Invalid marks! Please enter a value between 0 and 100.")
