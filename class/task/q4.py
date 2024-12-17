marks = int(input('Enter your marks:\n'))
if marks>80:
    print('A')
elif marks>60:
    print('B')
elif marks>50:
    print('C')
elif marks>40:
    print('D')
elif marks>30:
    print('E')
elif marks<20:
    print('F')
else:
    print('invalid input!')