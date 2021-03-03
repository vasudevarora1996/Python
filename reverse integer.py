'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.'''

class Solution:
    def reverse(self, x):
        max=+2147483647
        min=-2147483648
        rev=0
        num=x
        if x==0:
            return 0
        if x<1:
            x=x*-1
        while(x):
            if(x>max and x<min):
                return 0
            else:
                rev=(rev*10)+(x%10)
                x=x//10
        if num<1:
            return(-1*rev)
        else:
            return (rev)
def main():
    obj=Solution()
    ans=obj.reverse(123)
    print(ans)
main()
