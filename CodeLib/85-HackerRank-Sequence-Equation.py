import math
import os
import random
import re
import sys

def permutationEquation(p):
    l = []
    for i in range(len(p)):
        k = p.index(i+1)+1
        l.append(p.index(k)+1)
    return l

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
