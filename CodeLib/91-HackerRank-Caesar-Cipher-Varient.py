import math
import os
import random
import re
import sys

cip = "abcdefghijklmnopqrstuvwxyz"
cip = [ord(i) for i in cip]
CIP = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CIP = [ord(i) for i in CIP]
def caesarCipher(s, k):
    code = []
    for i in range(len(s)):
        if ord(s[i]) in cip:
            index = cip.index(ord(s[i]))+k
            flag = 0
        elif ord(s[i]) in CIP:
            index = CIP.index(ord(s[i]))+k
            flag = 1
        else:
            index = -1
        while index>=26:
                index-=26
        if index != -1:
            if flag == 0:
                code.append(chr(cip[index]))
            else:
                print(index)
                code.append(chr(CIP[index]))
        else:
            code.append(s[i])
        
    return ("").join(code)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')
    fptr.close()
