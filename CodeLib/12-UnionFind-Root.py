"""
Created on Sat Feb 22 10:45:33 2020
Union - Find - Root
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

def union(ar, u, v, n):
    ar[root(ar,u)] = root(ar,v)

if __name__ == "__main__":
    n = int(input())
    ar = [i for i in range(n)]
    k = int(input())
    for i in range(k):
        o = input()
        a,b = map(int,input().split(" "))
        if o == "u":
            union(ar,a,b,n)
        else:
            out = find(ar,a,b)
            if out:
                print(a,"is in the same set as",b)
            else:
                print(a,"is not in the same set as",b)
