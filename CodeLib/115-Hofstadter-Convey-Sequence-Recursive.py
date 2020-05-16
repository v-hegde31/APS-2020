def hc(n):
    if n<2:
        return 1
    return hc(hc(n-1) + hc(n - hc(n-1)))

for i in range(20):
    print(hc(i))
