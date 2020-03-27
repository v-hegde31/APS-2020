"""
Created on Sun Jun 23 01:40:38 2019
Euler #12
"""
n = 100000
from math import sqrt
from functools import reduce
def fact(n):
    step = 2 if n%2 else 1
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(sqrt(n))+1, step) if n % i == 0)))

for i in range(1,n+1):
    k = i*(i+1)//2
    l = fact(k)
    if len(l)>=500:
        print(i,k, len(l))
        break
