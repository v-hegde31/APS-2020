"""
Created on Sat Feb 1 10:38:41 2020
Coin Change Problem
"""

def nways(N,A):

    K = [0 for i in range(N+1)]
    K[0]=1
    for j in range(len(A)):
        for i in range(A[j],N+1):
            if K[i-A[j]] != 0:
                K[i] = K[i-A[j]]+K[i]
    return K
   
N = int(input())
A = list(map(int,input().split(" ")))
K = nways(N,A)   
print(K)
