"""
https://itu.kattis.com/courses/KSALDES1KU/KSALDES1KU-2024/assignments/g9pcgr/problems/itu.weightedintervalscheduling
Intervals has a start time, end time, and a weight.
Goal is to find the maximum weight of non-overlapping intervals.
Dynamic programming recursive approach.
Running time: O(n log n) because of sorting and binary search.
"""
from bisect import bisect_right
from sys import setrecursionlimit
setrecursionlimit(10**6)

n = int(input()) # Number of intervals
intervals = []
intervals.append((0, 0, 0)) # dummy

for _ in range(n):
    start, end, weight = map(int, input().split())
    intervals.append((start, end, weight))

# Sort by end time - O(n log n)
intervals.sort(key=lambda x: x[1])

# Precompute the indices of the previous non-overlapping intervals using binary search - O(n log n)
end_times = [interval[1] for interval in intervals]
previous_non_overlapping = [0] * (n + 1)
for i in range(1, n + 1):
    # Find the last interval that ends before the start of the current interval
    previous_non_overlapping[i] = bisect_right(end_times, intervals[i][0]) - 1

# Memo
memo = [-1] * (n+1) # memo[1] is max weight for solve(1)

def solve(i): # i is index of interval - O(n)
    # Base case, no intervals gives 0 weight
    if i == 0:
        return 0
    
    # Check memo
    if memo[i] != -1:
        return memo[i]
    
    # Include interval and move on to next non-overlapping event
    weight_with_event = intervals[i][2] + solve(previous_non_overlapping[i]) 

    # Include interval and move on to next event
    weight_without_event = solve(i - 1) 
    
    # Find max of the two weigths
    max_weight = max(weight_with_event, weight_without_event)
    
    # Save to memo
    memo[i] = max_weight

    return max_weight

print(solve(n)) # Start from last interval


