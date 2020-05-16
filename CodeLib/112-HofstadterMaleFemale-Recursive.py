def F(n):
    if n == 0:
        return 1
    return n - M(F(n-1))
def M(n):
    if n == 0:
        return 0
    return n - F(M(n-1))

for i in range(20):
    print(F(i),end = " ")
for i in range(20):
    print(M(i),end = " ")

    
