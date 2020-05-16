import math

a=list(map(int,input().split()))
n=len(a)
lookup=[[0 for i in range(math.ceil(math.log2(n)))] for j in range(n)]

for i in range(n):
    lookup[i][0]=i

j=1
while (1<<j)<n:
    i=0
    while i+(1<<j)-1 < n :
        if lookup[i][j-1]<=lookup[i+(1<<(j-1))][j-1]:
            lookup[i][j]=lookup[i][j-1]
        else:
            lookup[i][j]=lookup[i+(1<<(j-1))][j-1]
        i+=1
    j+=1

def query(L,R):
    j=int(math.log2(R-L+1))
    if a[lookup[L][j]]<=a[lookup[R-(1<<j)+1][j]]:
        return a[lookup[L][j]]
    else:
        return a[lookup[R-(1<<j)+1][j]]

L,R=map(int,input().split())
print(query(L,R))
