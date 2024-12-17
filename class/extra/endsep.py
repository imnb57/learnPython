### end and sep  used in print function for separation of parameters and changing the default new line feature of the print statement

### eg: print('hello',end='')
### print('world')
### print('hello','world',sep='')

"""
    .format()
    a ='ram'
    b = 'hari'
    c = 10

    print("hello{},hi{}.format(a,b)) #default argument
    print("hello{0},hi{1}.format(a,b)) #positional argument
    print("hello{a},hi{b}.format(a='krishna',b='raj')) #keyword argument
      ## keyword argument should be after default argument

    print("hello{0},hi{b}.format(a,b='andy')) #mixed argument
    print("hello{},hi{b},{}.format(a,c,b='sujal')) #mixed argument

    eval(input("enter your name"))
      # can take input for any datatype

"""
a ='ram'
c = 10
print("hello{},hi{b},{}".format(a,c,b='sujal'))