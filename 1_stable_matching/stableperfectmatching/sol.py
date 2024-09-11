"""
https://itu.kattis.com/courses/KSALDES1KU/KSALDES1KU-2024/assignments/ov8dt8/problems/itu.stableperfectmatching
This solution implements Gale-Shapley's Propose-Reject algorithm for finding stable matchings between two disjoint sets. 
The worst-case time complexity of the algorithm is O(n^2), where n is the number of people. 
This occurs when all men propose to all women. 
The preferences and rankings are stored in deques, which have O(1) time complexity for append and pop operations at both ends.
"""

from collections import defaultdict, deque

n, m = map(int, input().split()) # n = number of people, number of edges

# Initialize data structures
free_proposers = deque() # stack
proposers_prefs = defaultdict(deque) # m -> [] = stack of women on man m’s preference list 
rejectors_prefs = defaultdict(deque) # w -> [] = stack of men on woman w’s preference list
engagements = {} # woman -> current partner
ranking = defaultdict(dict) # woman -> man -> rank - lower numbers = high rank

# Read input and fill in data structures
for i in range(n//2): # Read proposers
    p, *p_prefs = input().split()
    free_proposers.append(p)
    for pref in p_prefs:
        proposers_prefs[p].append(pref)
for i in range(n//2): # Read rejectors
    r, *r_prefs = input().split()
    for pref in r_prefs:
        rejectors_prefs[r].append(pref)
    for rank, p in enumerate(r_prefs):
        ranking[r][p] = rank

while free_proposers:
    # Pop first free proposer
    p = free_proposers.popleft()
    
    # Pop first rejector from proposer's preference stack
    if proposers_prefs[p]:
        r = proposers_prefs[p].popleft()
    else: # If proposer has proposed to all rejectors and is still free, no stable matching possible
        print("-")
        exit()
    
    # If rejector is free, they become engaged
    if r not in engagements:
        engagements[r] = p
    else: # If rejector is not free, they compare their current partner to the proposer
        current_partner = engagements[r]
        # If new proposer has better rank than current partner
        if ranking[r][p] < ranking[r][current_partner]:
            engagements[r] = p
            free_proposers.append(current_partner)
        else: # If current partner has better rank than new proposer
            free_proposers.append(p)

# Stable matching found
if len(engagements) == n//2:
    for pair in engagements.items():
        print(pair[1], pair[0])      