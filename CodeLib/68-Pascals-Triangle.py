"""
Python code to print Pascal's triangle of given size N. 
Input: N
Output: Triangle. 
Created on Fri Apr 10 01:11:44 2020
"""
N = int(input())
a = []
for i in range(N):
    a.append([])
    a[i].append(1)
    for j in range(1,i):
        a[i].append(a[i-1][j-1]+a[i-1][j])
    if i != 0:
        a[i].append(1)
        
for i in a:
    for j in i:
        print(j,sep=" ",end = " ")
    print(" ")     
