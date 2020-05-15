import math
import os
import random
import re
import sys

def gameOfThrones(s):
    count = 0
    freq = {}
    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    k = list(freq.values())
    for i in k:
        if i%2!=0:
            count+=1
        if count>1:
            break
    if count <=1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')
    fptr.close()
