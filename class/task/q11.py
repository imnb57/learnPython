#11
age = int(input("Enter the person's age: \n"))

if age < 13:
    print("Category: Child")
elif 13 <= age <= 19:
    print("Category: Teenager")
elif age > 19:
    print("Category: Adult")
else:
    print("Invalid age input.")
