def lucas(n):
    if n==1:
        return 1
    if n==2:
        return 3
    return lucas(n-1)+lucas(n-2)

for i in range(1,11):
    print(lucas(i),end=" ")
