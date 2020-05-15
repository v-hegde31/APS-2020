import math
import os
import random
import re
import sys

def utopianTree(n):
    count = 1
    for i in range(n):
        if i%2==0:
            count = 2*count
        else:
            count+=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        n = int(input())
        result = utopianTree(n)
        fptr.write(str(result) + '\n')
    fptr.close()
