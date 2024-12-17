#12
char = input('Enter a char:\n')
if char.islower():
    print('lower')
elif char.isupper():
    print('upper')
elif char.isnumeric():
    print('number')
else:
    print('invalid input')