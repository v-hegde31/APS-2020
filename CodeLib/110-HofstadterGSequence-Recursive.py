def G(n):
    if n==0:
        return 0
    return n - G(G(n-1))

for i in range(31):
    print(G(i),end=" ")
