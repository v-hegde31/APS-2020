def padovan(n):
    if n<3:
        return 1
    return padovan(n-2) + padovan(n-3)
    
for i in range(20):
    print(padovan(i))
