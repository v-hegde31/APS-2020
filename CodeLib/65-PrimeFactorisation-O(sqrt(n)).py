import math 
def fact(X): 
    count = 0
    while ((X % 2 > 0) == False): 
        X >>= 1 
        count += 1
    if (count > 0): 
        print(2,count)
    for i in range(3, int(math.sqrt(X)) + 1): 
        count = 0 
        while (X % i == 0): 
            count += 1
            X = X//i
        if (count > 0):
            print(i,count) 
        i += 2 
    if (X > 2): 
        print(X,1)

T = int(input())
for _ in range(T):
    X = int(input())
    fact(X)
