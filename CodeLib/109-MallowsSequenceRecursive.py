def mallow(n):
    if n==1:
        return 1
    if n==2:
        return 1
    return mallow(mallow(n-2)) + mallow(n - mallow(n-2))

for i in range(1,31):
    print(mallow(i),end=" ")
