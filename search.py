'''Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.'''

class Solution:
    def searchInsert(self, nums, target):
        index=0
        if nums[-1]<target:
            return len(nums)
        for i in range(0,len(nums)):
            if target==nums[i]:
                return i
            elif nums[i]<target:
                index+=1
            else:
                return index

def main():
    result=Solution()
    print(result.searchInsert([1,3,5,6],5))
main()
                
                    
