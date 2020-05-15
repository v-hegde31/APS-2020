import math
import os
import random
import re
import sys

def findDigits(n,N):
    count = 0
    K = list(map(int,N))
    for i in K:
        if i!=0:
            if n%i==0:
                count+=1
    return count
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        N = input()
        n = int(N)
        result = findDigits(n,N)
        fptr.write(str(result) + '\n')
    fptr.close()
