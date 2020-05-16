def S(n):
    if n==2 or n==1:
        return 1
    return (3*(2*n-3)*S(n-1) - (n-3)*S(n-2))//n

for i in range(1,11):
    print(S(i),end = " ")
