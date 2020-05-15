import math
import os
import random
import re
import sys

def countingValleys(n, s):
    count = 0
    track = [0 for i in range(n+1)]
    for i in range(1,n+1):
        if s[i-1] == "U":
            track[i]=track[i-1]+1
        else:
            track[i]=track[i-1]-1
        if track[i-1]>=0 and track[i]<0:
            count+=1
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()
