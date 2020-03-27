"""
Created on Mon Oct  7 23:34:11 2019
SAKTAN
"""
T = int(input())

for _ in range(T):
    N,M,Q = list(map(int,input().split(" ")))
    r_list = [0] * N
    c_list = [0] * M
    for __ in range(Q):
        r,c = list(map(int,input().split(" ")))
        r_list[r-1]+=1
        c_list[c-1]+=1
    evenr = 0
    evenc = 0
    for i in range(N):
        if r_list[i]%2==0:
            evenr+=1
    for i in range(M):
        if c_list[i]%2==0:
            evenc+=1
    
    print(evenc*(N-evenr)+evenr*(M-evenc))
