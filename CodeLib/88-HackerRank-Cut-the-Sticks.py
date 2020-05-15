import math
import os
import random
import re
import sys

def cutTheSticks(arr):
    arr.sort()
    freq = {} 
    for item in arr: 
        if (item in freq): 
            freq[item] += 1
        else: 
            freq[item] = 1
    K = list(freq.values())
    Count = len(arr)
    countArr = []
    print(freq)
    for i in range(len(K)):
        countArr.append(Count)
        Count -= K[i]
    return countArr
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
