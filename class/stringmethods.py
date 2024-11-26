### upper,lower,title,capitalize,swapcase,replace,translate,center,zfill,startswith,endswith,ljust,rjust,count,index,find,rfind,rjust,rindex,isupper,islower,istitle,isalpha,isdigit,isalnum,isidentifier,isprintable,isspace,indexing,slicing


### a-z = 97-122; A-Z = 65-90; 0-9 = 48-57 
import math
a = 'python'
print(a.replace('p','j'
))

a = 'apple'
b = a.maketrans('a','t')
print(a.translate(b))

r = 'python'
u = r.maketrans('pxk','wxk')
print(u)

a= "python"
i=a.rjust(7,'*')
print(i)

a= "python"
i=a.ljust(7,'*')
print(i)

a= 64
print(math.sqrt(a))

