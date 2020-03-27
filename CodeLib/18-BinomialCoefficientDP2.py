"""
Feb 26, 2020
Binomial Coefficient Dynamic Programming - O(n)
"""

if __name__ == '__main__':
    n,k = map(int,input().split(" "))
    C = [0 for i in range(n+2)]
    C[0],C[1]=1,1
    for i in range(1,n+2):
        for j in range(min(i,k+1),1,-1):
            C[j]+=C[j-1]
    print(C[k+1])
