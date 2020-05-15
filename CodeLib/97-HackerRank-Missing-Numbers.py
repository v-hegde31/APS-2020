import math
import os
import random
import re
import sys

def missingNumbers(arr, brr):
    arr.sort()
    brr.sort()
    afreq = {} 
    for item in range(len(arr)): 
        if (arr[item] in afreq): 
            afreq[arr[item]] += 1
        else: 
            afreq[arr[item]] = 1
    bfreq = {} 
    for item in range(len(brr)): 
        if (brr[item] in bfreq): 
            bfreq[brr[item]] += 1
        else: 
            bfreq[brr[item]] = 1
    ans = []
    for i in bfreq:
        try:
            if afreq[i]==bfreq[i]:
                continue
            else:
                ans.append(i)
        except:
            ans.append(i)
    ans.sort()
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    m = int(input())
    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
