import os
import re
import sys

def funnyString(s):
    K = [abs(ord(s[i])-ord(s[i-1])) for i in range(1,len(s))]
    flag = 0
    for i in range(len(K)//2):
        if K[i] != K[len(K)-i-1]:
            flag = 1
            break
    if flag == 0:
        return "Funny"
    else:
        return "Not Funny"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())
    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')
    fptr.close()
