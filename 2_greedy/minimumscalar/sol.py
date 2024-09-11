"""
https://itu.kattis.com/courses/KSALDES1KU/KSALDES1KU-2024/assignments/nmchzj/problems/minimumscalar
Use greedy approach to find the minimum scalar product, 
by sorting v1 by smallest number first and v2 by largest number first,
and then multiply the corresponding elements of the two vectors
Complexity: O(n log n) because of sorting
"""

t = int(input())

for i in range(t):
    n = int(input())
    v1 = list(map(int, input().split()))
    v2 = list(map(int, input().split()))
    
    # Sort the two vectors
    v1.sort()             # Smallest number first
    v2.sort(reverse=True) # Largest number first

    # Find the scalar product of the sorted vectors
    msp = 0
    for j in range(n):
        msp += v1[j]*v2[j]

    print(f"Case #{i+1}: {msp}")