import math
import os
import random
import re
import sys

def flippingBits(n):
    Bin = int(bin(2**32-1)[2:])
    BinN = int(bin(n)[2:])
    Diff = "0b"+str(Bin - BinN)
    return int(Diff,2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        n = int(input())
        result = flippingBits(n)
        fptr.write(str(result) + '\n')
    fptr.close()
