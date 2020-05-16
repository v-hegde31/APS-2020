def H(n):
    if n==0:
        return 0
    return H(H(H(n-1)))

for i in range(1,31):
    print(H(i),end=" ")
