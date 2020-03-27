"""
Created on Sat Feb 15 13:24:18 2020
Union-Find
"""
def find(ar, u, v):
    if ar[u] == ar[v]:
        return True
    else:
        return False

def union(ar, u, v, n):
    for i in range(n):
        if ar[i] == ar[u]:
            ar[i] = ar[v]

if __name__ == "__main__":
    n = int(input())
    ar = [i for i in range(n)]
    k = int(input())
    for i in range(k):
        o = input().split(" ")
        a,b = map(int,input().split(" "))
        if o == "u":
            union(ar,a,b,n)
        else:
            out = find(ar,a,b)
            if out:
                print(a,"is in the same set as",b)
            else:
                print(a,"is not in the same set as",b)
