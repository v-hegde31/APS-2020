"""
Created on Mon Jan 27 23:50:51 2020
To encode a given text string into ascii code in a given base n.
"""
def reVal(num): 
    if (num >= 0 and num <= 9): 
        return chr(num + ord('0')); 
    else: 
        return chr(num - 10 + ord('A')); 
   
def convertbase(base, inputNum): 
    res = ""
    while (inputNum > 0): 
        res+= reVal(inputNum % base); 
        inputNum = int(inputNum / base) 
    res = res[::-1]; 
    return res; 

text = input()
n = int(input())
A = []
for i in range(len(text)):
    A.append(int(ord(text[i])))
    A[i] = convertbase(n,A[i])

print(" ".join(A))
