import math

n = int(input())
if n&(n-1)==0:
    print(1)
else:
    k = 2*(n - math.pow(2,math.floor(math.log2(n)))) + 1
    print(k)
