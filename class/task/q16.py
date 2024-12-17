#16
order = input('What would you like to have?(pizza, burger, pasta)\n').lower()
if order == 'pizza':
    print('the price is $10.')
elif order == 'burger':
    print('the price is $7.')
elif order == 'pasta':
    print('the price is $8')
else:
    print('invalid order')