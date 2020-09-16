"""
Using Hashmap to include already traversed part of list, while checking for the compliment of the current index in the list in the hashmap.
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
