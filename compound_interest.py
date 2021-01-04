principal=float(input("ENTER THE PRINCIPAL "))
interest=float(input("ENTER THE INTEREST RATE "))
time=float(input("ENTER THE TIME IN YEARS "))
def compound_interest(principal,interest,time):
    amount=principal * pow(1+(interest/100),time)
    ci=amount-principal
    print("amount is",amount)
    print("compound interest is",ci)
compound_interest(principal,interest,time)
