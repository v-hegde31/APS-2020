"""
Created on Thu Dec 13 14:42:45 2018
"""

t = int(input())
while t!=0:
    new = []
    n = int(input())
    for i in range(1,n-1):
        print(1,i,i+1,i+2,flush=True)
        k = int(input())
        if k%2 == 0:
            k=k+1
        else:
            k=k-3
        new.append(str(k))
        if(i==n-2):
            print(1,n-1,n-1,n-1)
            k = int(input())
            new.append(str(k))
            print(1,n,n,n)
            k = int(input())
            new.append(str(k))
    k = " ".join(new)
    print(2,k,flush=True)
    l = int(input())
    if l == -1:
        exit(0)
    t-=1
