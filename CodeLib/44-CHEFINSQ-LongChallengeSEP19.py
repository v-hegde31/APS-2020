from math import factorial

def comb(n,r):
    return(factorial(n)//(factorial(n-r)*factorial(r)))

T = int(input())
for _ in range(T):
    N,K = list(map(int,input().split(" ")))
    A = list(map(int,input().split(" ")))
    A.sort()
    freq = {} 
    for item in A: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    v = list(freq.values())
    ans = 1
    for i in range(len(v)):
        if K>=v[i]:
            K-=v[i]
        else:
            ans = comb(v[i],K)
            break
    print(ans)
