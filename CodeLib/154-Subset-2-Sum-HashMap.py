"""
Using Hashmap to include already traversed part of list, while checking for the compliment (S-i) of the current index (i) in the list in the hashmap.

Space Complexity: O(n)
Time Complexity: O(n)
"""

T = int(input())
for _ in range(T):
    A = list(map(int,input().split(" ")))
    S = int(input())
    D = {}
    for i in A:
        if S - i in D:
            print(i,S-i)
        else:
            D[i]= True
    print(D)
