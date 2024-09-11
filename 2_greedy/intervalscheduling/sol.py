"""
https://itu.kattis.com/courses/KSALDES1KU/KSALDES1KU-2024/assignments/nmchzj/problems/intervalscheduling
Solved using greedy algorithm (earliest-finish-time-first algorithm)
Complexity: O(n log n) because of sorting
"""

# Read events
n = int(input())
events = []
for i in range(n):
    start, finish = map(int, input().split())
    events.append((start, finish))

# Sort by finish time, earliest to latest
events.sort(key=lambda a: a[1])

# When the most recently added event finishes
current_finish = 0 

no_of_events = 0
for event in events: 
    if event[0] >= current_finish: # Events start after the current event finishes
        no_of_events += 1
        current_finish = event[1]
        
print(no_of_events)

