"""
Created on Thu Jan 16 14:04:39 2020
KnapSack Problen
"""
N = int(input())
Weight = []
Val = []
for i in range(N):
    (w,v) = list(map(int,input().split(" ")))
    Weight.append(w)
    Val.append(v)
W = int(input())
K = [[0 for i in range(W+1)] for j in range(N+1)]

for i in range(1,N+1):
    for j in range(1,W+1):
        if Weight[i-1] <= j:
            K[i][j] = max(K[i-1][j],Val[i-1]+K[i-1][j-Weight[i-1]])
        else:
            K[i][j] = K[i-1][j]
print(K[N][W])
