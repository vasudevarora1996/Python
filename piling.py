'''There is a horizontal row of  cubes. The length of each cube is given. You need to create a new vertical pile of cubes. The new pile should follow these directions: if  is on top of  then .
When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.
Input Format
The first line contains a single integer , the number of test cases. 
For each test case, there are  lines. 
The first line of each test case contains , the number of cubes. 
The second line contains  space separated integers, denoting the sideLengths of each cube in that order.'''

from collections import deque
for _ in range(int(input())):
    flag = True
    input()
    d = deque(map(int, input().strip().split()))
    if (d[0] >= d[-1]):
        max = d.popleft()
    else:
        max = d.pop()
    while d:
        if (len(d) == 1):
            if (d[0] <= max):
                break
            else:
                flag = False
                break
        else:
            if d[0] <= max and d[-1] <= max:
                if d[0] >= d[-1]:
                    max = d.popleft()
                else:
                   max = d.pop()
            elif d[0] <= max:
                max = d.popleft()
            elif d[-1] <= max:
                max = d.pop()
            else:
                flag = False
                break
    if flag:
        print("Yes")
    else:
        print("No")
