principal=float(input("ENTER THE PRINCIPAL AMOUNT"))
interest=float(input("ENTER THE INTEREST RATE"))
time=float(input("ENTER THE TIME IN YEARS"))
def simple_interest(principal,interest,time):
    z=(principal*interest*time)/100
    print("SIMPLE INTEREST FOR PRINCIPAL AMOUNT =",principal,"INTEREST RATE =",interest,"& TIME =",time,"IS",z)
simple_interest(principal,interest,time)
