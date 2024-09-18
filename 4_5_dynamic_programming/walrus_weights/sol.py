"""
    https://itu.kattis.com/courses/KSALDES1KU/KSALDES1KU-2024/assignments/g9pcgr/problems/walrusweights
    Wallace has some weight plates with different weights.
    Goal is to add plates as close to 1000 kg as possible (+-).
    In case of a tie, choose the heaviest set of plates.
    Each plate can be used at most once.
    Using dynamic programming iterative approach.
    Running time: O(n * MAX)
"""
from math import inf
TARGET = 1000
MAX = 2000

n = int(input()) # Number of plates
plates = [int(input()) for _ in range(n)] # Weight of each plate

# Memo 
possible = [False] * (MAX+1)

# Base case - Weight 0 can be achieved with 0 plates
possible[0] = True

# Fill the memo
for plate_weight in plates: # O(n)
    for total_weight in range(MAX, plate_weight - 1, -1): # O(MAX)
        # If the weight can be achieved without the current plate, it can also be achieved by adding the current plate
        if possible[total_weight - plate_weight]:
            possible[total_weight] = True

# Find the closest weight to 1000 (plus/min)
closest_weight = inf
for i in range(MAX):
    if possible[i]:
        if abs(TARGET - i) <= abs(TARGET - closest_weight):
            closest_weight = i
        
print(closest_weight)
