"""
Feb 26, 2020
Binomial Coeffiicent Using Recursion
"""
def binomVal(n,k):
    if n==k or k==0:
        return 1
    else:
        return binomVal(n-1,k-1)+binomVal(n-1,k)

if __name__ == '__main__':
    n,k = map(int,input().split(" "))
    print(binomVal(n,k))
