import math
import os
import random
import re
import sys

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    count,iflag,lflag,uflag,sflag = 0,0,0,0,0
    for i in password:
            if i in numbers:
                iflag = 1
            if i in lower_case:
                lflag = 1
            if i in upper_case:
               uflag = 1
            if i in special_characters:
                sflag = 1
    count+=(4-(iflag+lflag+uflag+sflag))
    if n<6:
        k = 6-n
        if k>=count:
            count = k
    return count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')
    fptr.close()
