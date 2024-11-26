""" List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members."""

list = ['apple','orange','grapes',40,40.09]
for x in list:
    print(x)
print(len(list))

### indexing in list starts from 0, lists are mutable , lists use square bracket
### lists also allow duplicates meaning if you store the same value again then it gets stored in another index
### lists can contain multiple data types
### we can use append() to add a single element to our list
### we can use extend() to add a single element to our list
a =list[0]
list.append(78)
list.extend(("strawberry",69,420))
print(a)
print(list)
