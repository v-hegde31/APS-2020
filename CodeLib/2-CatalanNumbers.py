"""
Recursive Code to print N Catalan number
"""
def Catalan(n):
    if n == 1:
        return 1
    else:
        return (4*n - 2)*Catalan(n-1)//(n+1)
N = int(input()) 
for i in range(1,N+1):
    print(Catalan(i))
