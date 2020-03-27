"""
Created on Sat Dec  7 10:41:37 2019
"""

def binaryToDecimal(binary): 

    decimal, i = 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal

T = int(input())
for _ in range(T):
    A = input()
    B = input()
    if((len(set(A)) == 1 and A[0] == "1") and (len(set(B)) == 1 and B[0] == "1")):
        if(len(A)>len(B)):
            print(len(A)-len(B)+2)
        else:
            print(len(B)-len(A)+2)
    else:
        A = binaryToDecimal(int(A))
        B = binaryToDecimal(int(B))
        count = 0
        while B > 0:
            U = A ^ B
            V = A & B
            A = U
            B = V*2
            count+=1
        print(count)
