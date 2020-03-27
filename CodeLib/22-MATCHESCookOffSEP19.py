"""
Sep 24, 2019
MATCHES - Cook Off Sep 2019
"""
matchArr = [6,2,5,5,4,5,6,3,7,6]
T = int(input())
for _ in range(T):
    (A,B) = list(map(int,input().split(" ")))
    Sum = str(A+B)
    match = 0
    for i in range(len(Sum)):
        match += matchArr[int(Sum[i])]
    print(match)
