"""
https://itu.kattis.com/courses/KSALDES1KU/KSALDES1KU-2024/assignments/s2jich/problems/itu.closestpairnicer
Find closest pair of points 2D.
Divide and conquer approach by sorting by x, recursively finding the closest pair in the left and right half.
When recursion is done, check the middle part by sorting by y and checking 11 neighbors.
Running time: O(n log n)
"""

from math import sqrt

def closest_pair_rec(lo, hi, Px, Py): # O(n log n)
    n = hi - lo
    
    ## BASE CASE
    if n <= 128:  
        return closest_pair_brute_force(lo, hi, Px)

    ## DIVIDE
    mid = lo + n // 2
    mid_x = Px[mid][0]

    l_Py = [p for p in Py if p[0] <= mid_x]
    r_Py = [p for p in Py if p[0] > mid_x]

    l_pair = closest_pair_rec(lo, mid, Px, l_Py)
    r_pair = closest_pair_rec(mid, hi, Px, r_Py)

    ## COMBINE
    min_pair = l_pair if sq_distance(l_pair[0], l_pair[1]) < sq_distance(r_pair[0], r_pair[1]) else r_pair
    min_dist = sq_distance(min_pair[0], min_pair[1])
    min_dist_sqrt = sqrt(min_dist)

    # Build the strip with points within min_dist_sqrt from the middle and find the closest pair in the strip
    strip = [p for p in Py if abs(p[0] - mid_x) < min_dist_sqrt]
    s_pair = closest_pair_in_strip(strip, min_dist)

    # Compare the closest pair in the strip with the closest pair from the left and right
    if s_pair and sq_distance(s_pair[0], s_pair[1]) < min_dist:
        return s_pair
    else:
        return min_pair

def closest_pair_brute_force(lo, hi, Px): # O(n^2)
    min_dist = float('inf')
    min_pair = None
    for i in range(lo, hi):
        for j in range(i + 1, hi):
            if sq_distance(Px[i], Px[j]) < min_dist:
                min_dist = sq_distance(Px[i], Px[j])
                min_pair = (Px[i], Px[j])
    return min_pair

def closest_pair_in_strip(strip, d): # O(n)
    min_dist = d
    min_pair = None
    for i in range(len(strip)):
        for j in range(i + 1, min(i + 11, len(strip))):  # Check distance to up to 11 neighbors
            if (strip[j][1] - strip[i][1]) ** 2 < min_dist:
                dist = sq_distance(strip[i], strip[j])
                if dist < min_dist:
                    min_dist = dist
                    min_pair = (strip[i], strip[j])
    return min_pair

def sq_distance(p1, p2): # O(1)
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 # Distance is squared to avoid using sqrt (slow)

# Read input
n = int(input())
points = []
for _ in range(n):
    x, y = map(float, input().split())
    points.append((x, y))

# Sort - O(n log n)
Px = sorted(points)                      # Sorted by x
Py = sorted(points, key=lambda p: p[1])  # Sorted by y

# Find closest pair
closest_pair = closest_pair_rec(0, n, Px, Py)
print(f"{closest_pair[0][0]} {closest_pair[0][1]}")
print(f"{closest_pair[1][0]} {closest_pair[1][1]}")