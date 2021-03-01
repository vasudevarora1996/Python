"""You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.
For example, given the array arr=[7,1,3,2,4,5,6]. It took  swaps to sort the array.
Function Description
Complete the function minimumSwaps in the editor below. It must return an integer representing the minimum number of swaps to sort the array.
minimumSwaps has the following parameter(s):
arr: an unordered array of integers
Input Format
The first line contains an integer, , the size of . 
The second line contains  space-separated integers .
Constraints


Output Format
Return the minimum number of swaps to sort the given array.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    tmp = {}

    for i, val in enumerate(arr):
        tmp[val] = i

    for i in range(len(arr)):
        
        if arr[i] != i+1:
            swaps += 1
            t = arr[i]
            arr[i] = i+1
            arr[tmp[i+1]] = t
            tmp[t] = tmp[i+1]

    return swaps   
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
