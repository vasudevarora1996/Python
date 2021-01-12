num=int(input("ENTER A NUMBER TO CALCULATE FACTORIAL"))
def factorial(num):
    fact=1
    for i in range(num,1,-1):
        fact = fact * i
    print("FACTORIAL OF {} is {}".format(num,fact))    
    print("MADE BY AKHIL")
factorial(num)
