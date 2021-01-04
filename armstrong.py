num=int(input("ENTER THE NUMBER "))
z=num
sum=0
while num!=0:
    rem=num%10
    sum = sum + (rem * rem * rem)
    num=num//10
print(sum)
if sum==z:
 print("armstrong")
else:
 print("not armstrong")
