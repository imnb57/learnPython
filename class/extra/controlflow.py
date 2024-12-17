## control flow -> selection statement/conditional statement(if, elif, else),   iterative statement(for, while),   transfer statements(break, continue,return try except if else finally)

## if, if if, if else, if elif else, if elif elif else
# 6 marks

#1
a = 10
b = 20

if a == b:
    print('1')

elif a>b:
    print('2')

else:
    print('3')

#2
num = int(input("Enter a number:\n"))
if num%2 == 0:
    print('The number is even')
else:
    print('The number is odd')

#3
num = int(input("please enter a number in a range of 1 to 12:\n"))
if num == 1:
    print('January')
elif num == 2:
    print('February')
elif num == 3:
    print('March')
elif num == 4:
    print('April')
elif num == 5:
    print('May')
elif num == 6:
    print('June')
elif num == 7:
    print('July')
elif num == 7:
    print('August')
elif num == 8:
    print('September')
elif num == 9:
    print('October')
elif num == 10:
    print('November')
elif num == 11:
    print('December')
else:
    print('out of range')

#4
marks = int(input('Enter your marks:\n'))
if marks<25:
    print('F')
elif marks>25:
    print('E')
elif marks>45:
    print('D')
elif marks>50:
    print('C')
elif marks>60:
    print('B')
elif marks>80:
    print('A')
else:
    print('invalid input!')
