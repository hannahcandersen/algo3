"""
https://itu.kattis.com/courses/KSALDES1KU/KSALDES1KU-2024/assignments/bs7ggr/problems/everywhere
"""

t = int(input())

for i in range(t):
    n = int(input()) # number of trips
    cities = set() 
    for j in range(n):
        city = input()
        cities.add(city)
    print(len(cities))
    