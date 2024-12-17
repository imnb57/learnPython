def fibo(n):
   a,b = 0,1
   while a<=n:
     print(a)
     a,b = b,a+b

num = int(input("Enter number"))
fibo(num)