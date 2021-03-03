# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    def f(num):
        fact=0
        while(num!=1):
            rem=num%10
            num=num/10
            fact+=factorial(rem)
        return fact

    def factorial(number):
        while(number!=1):
            if number==1:
                return 1
            else:
                output=number*factorial(number-1)
        return output
    
    def sf(num):
        score=0
        output=f(num)
        while(output!=1):
            rem=output%10
            output=output/10
            score+=rem
        return score

    def g(n):
        smallest = 0
        i = 1
        while(smallest==0):
            if sf(i) == n:
                smallest = i
            else:
                i = i+1
        return smallest
    
    def sg(n):
        output=g(n)
        add=0
        while(output>1):
            add+=output%10
            output=output/10
        return add
    q=int(input())
    n, m=list(map(int,input().split()))
    sg(n)
