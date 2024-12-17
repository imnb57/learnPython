#6
num1 = int(input('Enter a number:\n'))
num2 = int(input('Enter another number:\n'))
opr = input('Enter an operator(+,-,/,*):\n')

operator = ['+','-','*','/']

if opr == operator[0]:
    print(num1+num2)
elif opr == operator[1]:
    print(num1-num2)
elif opr == operator[2]:
    print(num1*num2)
elif opr == operator[3]:
    print(num1/num2)
else:
    print("invalid operation!")