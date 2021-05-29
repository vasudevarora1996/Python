#!/bin/python3
"""
Picking Tickets HackerRank Problem
Consider an array of n tickets prices, tickets. A number, m, is defined as the size of some subsequence, s, of tickets where each element covers an unbroken range of integers. That is to say, if you were to sort the elements in s, the absolute difference between any elements j and j+1 would be either 0 or 1. Determine the maximum length of a subsequence chosen from the tickets array.
"""

def MaxTickets(tickets):
    length = len(tickets)
    tickets = sorted(tickets)
    count = 1
    arr = []
    for i in range(0, length-1):
        if(tickets[i] - tickets[i+1] == 0) or (tickets[i] - tickets[i+1] == -1):
            count = count + 1
        else:
            arr.append(count)
            count = 1
    return max(arr)