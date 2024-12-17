#9
char = input('Enter a character:\n')
vowel = ['a','e','i','o','u']
if char.lower() in vowel:
    print('vowel')
else:
    print('consonant')