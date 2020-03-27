"""
Feb 26, 2020
Binomial Coefficient DP - O(n*k)
"""

def binomialTable(C):
    for i in range(n+1):
        for j in range(0,min(i+1,k+1)):
            if j == 0 or j==i:
                C[i][j]=1
            else:
                C[i][j] = C[i-1][j-1]+C[i-1][j]
    return(C)



if __name__ == '__main__':
    n,k = map(int,input().split(" "))
    C = [[0 for i in range(k+1)]for j in range(n+1)]
    Coef = binomialTable(C)
    for i in Coef:
        print(i)
    print(Coef[n][k])
