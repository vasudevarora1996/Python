'''Given two strings, determine if they share a common substring. A substring may be as small as one character.
Example 
 

These share the common substring .
 

These do not share a substring.
Function Description
Complete the function twoStrings in the editor below.
twoStrings has the following parameter(s):
string s1: a string
string s2: another string
Returns
string: either YES or NO
Input Format
The first line contains a single integer , the number of test cases.
The following  pairs of lines are as follows:
The first line contains string .
The second line contains string .
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
   str1=set(s1)
   str2=set(s2)
   if str1.intersection(str2):
    return "YES"
   else:
    return "NO"
   
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()
