### escape characters

## \
a ='python\'s escape methods'
print(a)

## /n
a = 'python\n'
b = 'new line'
print(a)
print(b)

## \t
a = 'python\t\tafter four spaces'
print(a)
print(a.upper())
print(a.lower())

# Using expandtabs to replace tabs with spaces
text = '\tpython'.expandtabs(tabsize=4)
print(text)  # Output: "    python" (tab replaced with 4 spaces)

## \r
a = 'python\rabc'
print(a)

a = "example Of Text"
print(a.upper())
print(a.lower())
print(a.strip())
print(a.capitalize())

## for centering if length of string is odd : formula = n-1\2(leftside) and n+1\2(right), and for even length just reverse the formula
print(a.center(25,'*')) 

## ljust()
## rjust()
## rfind()

### difference between find and index is that if there is absence of character we want to find then index returns zero and find returns error.

a = 'python'
print(a.ljust(10,'*'))
print(a.rjust(10,'*'))
print(a.rfind('t'))