"""
https://itu.kattis.com/courses/KSALDES1KU/KSALDES1KU-2024/assignments/nmchzj/problems/grass
Greedy approach
Sort the sprinklers by the lefmost coordinate they can cover
Iterate through the sorted sprinklers and choose the 
one that starts before or at the current position and has highest rightmost coordinate
"""
import sys

for line in sys.stdin:
    line = line.strip()
    if not line: 
        break
    
    n, l, w = map(int, line.split())  # sprinklers, length, width
    sprinklers = []  # [(leftmost point, rightmost point)]
    
    for i in range(n):
        line = sys.stdin.readline().strip()
        x, r = map(int, line.split())
        if r * 2 >= w:  # Only add sprinklers that can cover the width
            left, right = x - r, x + r
            sprinklers.append((left, right))  
    
    sprinklers.sort(key=lambda x: (x[0], -x[1]))  # Sort by leftmost point ascending, then rightmost point descending
    
    current_right = 0  # Rightmost point of the last chosen sprinkler    
    farthest_right = 0  # Fartherst right point reached at the moment
    no_of_sprinklers = 0
    i = 0
