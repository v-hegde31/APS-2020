"""
Created on Mon Apr 20 01:36:56 2020
Recursive code for triangular numbers
"""

def triangular(n):
    if n < 1:
        return 1
    return (n+1) + triangular(n-1)


N = int(input())
for i in range(N):
    print(i+1,triangular(i))
