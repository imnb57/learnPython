firstName='ram'
lastName='kc'
print(id(firstName))
print(id(lastName))
print(firstName is lastName)

   

### for small integers
a = 10
b = 10

print(id(a))  # Memory address of 'a'
print(id(b))  # Memory address of 'b'
print(a is b)  # True because integers in the range -5 to 256 are interned

### for large integers 
x = 1000
y = 1000

print(id(x))
print(id(y))
print(x is y)  # False because integers outside the range -5 to 256 are not interned

### for float
x = 10.5
y = 10.5

print(id(x))  # Memory address of 'x'
print(id(y))  # Memory address of 'y'
print(x is y)  # False because floats are not interned

### for list
list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(id(list1))  # Memory address of 'list1'
print(id(list2))  # Memory address of 'list2'
print(list1 is list2)  # False because lists are mutable and stored separately

### for tuples
tup1 = (1, 2, 3)
tup2 = (1, 2, 3)

print(id(tup1))  # Memory address of 'tup1'
print(id(tup2))  # Memory address of 'tup2'
print(tup1 is tup2)  # False: Tuples with same values may still be different objects

### for dictionaries 
dict1 = {'a': 1, 'b': 2}
dict2 = {'a': 1, 'b': 2}

print(id(dict1))  # Memory address of 'dict1'
print(id(dict2))  # Memory address of 'dict2'
print(dict1 is dict2)  # False because dictionaries are mutable and stored separately

### for sets
set1 = {1, 2, 3}
set2 = {1, 2, 3}

print(id(set1))  # Memory address of 'set1'
print(id(set2))  # Memory address of 'set2'
print(set1 is set2)  # False because sets are mutable and stored separately


