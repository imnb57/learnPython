sub1 = int(input('Enter marks of subject 1:\n'))
sub2 = int(input('Enter marks of subject 2:\n'))
sub3 = int(input('Enter marks of subject 3:\n'))
sub4 = int(input('Enter marks of subject 4:\n'))

totalMarks = sub1+sub2+sub3+sub4
percentage = (totalMarks/400)*100

print(f'Your total mark is : {totalMarks}')
print(f'Your percentage is : {percentage}')

if percentage>70:
    print('Your grade is distinction')
elif percentage> 60:
    print('Your grade is first')
elif percentage>40:
    print('Your grade is pass')
elif percentage<40:
    print("Your grade is fail")
else:
    print('Error occured')