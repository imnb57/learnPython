print('Welcome to Treasure land')
choice = input('Choose either left or right:\n')
if choice == 'right':
    print('game over')
elif choice == 'left':
    choice = input('swim or wait:\n')
    if choice == 'swim':
        print('game over')
    elif choice == 'wait':
        choice= input('choose a color(red,blue,yellow):\n')
    if choice == 'blue' or 'red':
        print('game over')
    elif choice == 'yellow':
        print('game over')
else:
    print('invalid choice')
    

    

