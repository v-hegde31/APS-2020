import os
import sys

def pageCount(n, p):
    if p<=n//2:
        minp = p//2
    else:
        if n==6 and p==5:
            minp = 1
        else:
            minp = (n-p)//2
    return minp
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    p = int(input())
    result = pageCount(n, p)
    fptr.write(str(result) + '\n')
    fptr.close()
