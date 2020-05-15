import math
import os
import random
import re
import sys

def maximizingXor(l, r):
    k = []
    for i in range(l,r+1):
        for j in range(l+1,r+1):
            k.append(i^j)
    return(max(k))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    l = int(input())
    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')
    fptr.close()
