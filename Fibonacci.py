def fibonnacci(num):
   a=0
   b=1
   print("Fibonacci Series is: ")
   print(a)
   print(b)
   for i in range(num-2):
     c=a+b
     a=b
     b=c
     print(c)

z=int(input("Enter the length of Fibonacci Series"))
fibonnacci(z)
