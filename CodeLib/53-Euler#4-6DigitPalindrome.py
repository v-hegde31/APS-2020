"""
Created on Fri Jun 21 01:16:55 2019
Euler #4
"""
Palindromes = []
for j in range(999,100,-1):
    for i in range(999,100,-1):
        s = str(j*i)
        if len(s)==6 and s[0]==s[5] and s[1]==s[4] and s[2]==s[3]:
            Palindromes.append(s)
Palindromes = list(set(Palindromes))
palindromes = list(map(int,Palindromes))
palindromes.sort()
