"""
Feb 17, 2019
SECPASS - Cook Off Feb 2019
"""
t=int(input())
for k in range(t):
    n=int(input())
    inp=input()
    tmpstr=""
    subarr = []
    freqarr = []
    for i in range(n):
        tmpstr = tmpstr + inp[i]
        subarr.append(tmpstr)
    for i in range(n):
        freqarr.append(inp.count(subarr[i]))
    maxindex=0
    for i in range(n):
        if freqarr[i]>=freqarr[maxindex]:
            maxindex=i
    print(subarr[maxindex])
