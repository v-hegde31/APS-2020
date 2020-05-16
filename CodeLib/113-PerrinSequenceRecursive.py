def perrin(n):
    if n == 0:
        return 3
    if n == 1:
        return 0
    if n == 2:
        return 2
    return perrin(n-2) + perrin(n-3)
    
 for i in range(20):
    print(perrin(i))
