"""
Assignment: https://itu.kattis.com/courses/KSALDES1KU/KSALDES1KU-2024/assignments/xmhbrn/problems/elementarymath

Exam where there are n questons. In each they have to add, subtract or multiply a pair of numbers.
All n questions should give different answers (e.g. two answers can't give 6)
Figure out if you need to add, subtract or multiply the numbers to get different answers for all questions.

Solve it as a flow problem. 
Each pair has a edge to the result of the three operations, with capacity 1.
Each result has an edge to the sink with capacity 1, as only one question can have that result
"""
from collections import defaultdict
from flow import flow

n = int(input()) # Number of questions
pairs = [tuple(map(int, input().split())) for _ in range(n)] # Pairs of numbers
#print(pairs)

#### GRAPH REPRESENTATION ####
# Source -> Pair -> Each operation result -> Sink. 
graph = defaultdict(lambda: defaultdict(int)) # vertex -> (vertex -> capacity).
source_v = "source"
results = set() # Keep track of the results to be able to add edges between them and the sink

#### BUILD GRAPH ####
for pair in pairs:
    
    # Edges between source and pair
    graph[source_v][pair] = 1
    
    # Edges between pair and results
    addition = pair[0] + pair[1]
    subtraction = pair[0] - pair[1]
    multiplication = pair[0] * pair[1]
    graph[pair][addition] = 1
    graph[pair][subtraction] = 1
    graph[pair][multiplication] = 1
    results.add(addition)
    results.add(subtraction)
    results.add(multiplication)
        
# Edges between results and sink
for result in results:
    graph[result]["sink"] = 1

print(graph)

#### FIND MAX FLOW ####
(max_flow, residual_graph, visited) = flow(graph, source_v, "sink")
if max_flow == n:
else:
    print("Impossible")