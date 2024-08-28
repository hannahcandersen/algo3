"""
https://itu.kattis.com/courses/KSALDES1KU/KSALDES1KU-2024/assignments/bs7ggr/problems/backspace
"""

input = input()
output = [] # stack
for char in input:
    if char == "<":
        output.pop()
    else:
        output.append(char)
print("".join(output))