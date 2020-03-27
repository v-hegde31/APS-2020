"""
Created on Sat Feb 29 11:16:25 2020
UnionFind-Root for Weighted Union
"""
def root(ar,i):
    while ar[i]!=i:
        i = ar[i]
    return i

def find(ar, u, v):
    if root(ar,u) == root(ar,v):
        return True
    else:
        return False

def union(ar, u, v, n,size):
    rootu = root(ar,u)
    rootv = root(ar,v)
    if size[rootu]<size[rootv]:
        ar[rootu] = ar[rootv]
        size[rootv]+=size[rootu]
    else:
        ar[rootv] = ar[rootu]
        size[rootu]+=size[rootv]

if __name__ == "__main__":
    n = int(input())
    ar = [i for i in range(n)]
    size = [1 for i in range(n)]
    k = int(input())
    for i in range(k):
        o = input()
        a,b = map(int,input().split(" "))
        if o == "u":
            union(ar,a,b,n,size)
        else:
            out = find(ar,a,b)
            if out:
                print(a,"is in the same set as",b)
            else:
                print(a,"is not in the same set as",b)
