"""
Python code to print the sequence of number and number of letters in a given number until a terminating number 4 is reached.
24-06-2019
"""

alpha = [4,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8]
ten = [6,6,5,5,5,7,6,6]
h = [7]
for i in range(1,9):
    h.append(h[0]+alpha[i+1])  
for i in range(8):
        alpha.append(ten[i])
        for j in range(1,10):
            alpha.append(ten[i]+alpha[j])            
for k in range(9):
    alpha.append(h[k])
    for a in range(1,20):
        alpha.append(h[k]+alpha[a])
    for i in range(8):
        alpha.append(h[k]+ten[i])
        for j in range(1,10):
            alpha.append(h[k]+ten[i]+alpha[j])
   
T = int(input())
for iterations in range(T):
    N = int(input())
    while(N!=4):
        print(alpha[N])
        N = alpha[N]
    print(N)
