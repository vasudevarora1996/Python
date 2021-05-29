#!/bin/python3

"""
Given an array of integers, determine whether each is a power of 2, where powers of 2 are [1, 2, 4, 8, 16, 32, 64, ....].
For Each integer evaluated, append to an array a value of 1 if the number is a power of 2 or 0 otherwise.
"""

def isPower(arr):
    temp = 0
    arr1 = []
    for i in arr:
        temp = i
        if temp == 1:
            arr.append(1)
        elif temp == 0:
            arr.append(0)
        else:
            while temp % 2 == 0:
                temp = temp//2
            if temp == 1:
                arr1.append(1)
            else:
                arr1.append(0)
    return arr1