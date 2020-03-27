"""
Mar 22, 2020
Allocation - Google KickStart Round A
"""

T = int(input())
for _ in range(1,T+1):
    N,B = map(int,input().split(" "))
    A = list(map(int,input().split(" ")))
    count = 0
    A.sort()
    for i in range(N):
        if A[i]<=B:
            count+=1
            B-=A[i]
    print("Case #"+str(_)+": "+str(count))
