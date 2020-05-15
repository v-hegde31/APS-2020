import math
import os
import random
import re
import sys

alpha = "abcdefghijklmnopqrstuvwxyz"
def pangrams(s):
    #s = s.strip(' ')
    if len(s)==1:
        return "not pangram"
    s = set(s.lower().strip(" "))
    s.remove(' ')
    if len(s)<26:
        return "not pangram"
    else:
        return "pangram"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')
    fptr.close()
