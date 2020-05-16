def pell(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return 2*pell(n-1)+pell(n-2)

for i in range(1,11):
    print(pell(i),end=" ")
