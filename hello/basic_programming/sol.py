"""
https://itu.kattis.com/courses/KSALDES1KU/KSALDES1KU-2024/assignments/bs7ggr/problems/basicprogramming1
"""

def one(A): 
    """
    Print 7 regardless of the content of A
    """
    print(7)
    
def two(A):
    """
    Print "Bigger if A[0] > A[1] 
    Print "Equal" if A[0] == A[1]
    Print "Smaller" if A[0] < A[1]
    """
    if A[0] > A[1]:
        print("Bigger")
    elif A[0] == A[1]:
        print("Equal")
    else:
        print("Smaller")

def three(A):
    """
    Print the median of A[0], A[1], A[2]
    By sorting the first three elements and printing the middle element
    """
    first_three = sorted(A[:3])
    print(first_three[1])
    
def four(A):
    """
    Print the sum of all elements of A
    """
    print(sum(A))

def five(A):
    """
    Print the sum of all even elements of A
    """
    print(sum([i for i in A if i % 2 == 0]))

def six(A):
    """
    Apply modulo 26 to each element of A.
    Then map the result to the corresponding letter in the alphabet
    Print the resulting string
    """
    mod_26 = [i % 26 for i in A]
    # Map integers to characters. chr(97) = unicode for 'a', chr(98) = unicode for 'b' etc.
    characters = [chr(97 + i) for i in mod_26]
    print("".join(characters))
    
def seven(A):
    """
    Start from i = 0
    Jump to the index corresponding to the value of A[i]
    If the index is out of bounds, print "Out" and stop
    If the index is N-1, print "Done" and stop
    Otherwise, continue to jump, where i = A[i]
    If the index is visited twice, print "Cyclic" and stop
    """
    i = 0
    visited = [False] * len(A)
    while i < len(A):
        if i == len(A) - 1:
            print("Done")
            return
        if visited[i]:
            print("Cyclic")
            return
        visited[i] = True
        i = A[i]
    print("Out")
    
N, t = list(map(int, input().split()))
A = list(map(int, input().split()))

if t == 1:
    one(A)
elif t == 2:
    two(A)
elif t == 3:
    three(A)
elif t == 4:
    four(A)
elif t == 5:
    five(A)
elif t == 6:
    six(A)
elif t == 7:
    seven(A)