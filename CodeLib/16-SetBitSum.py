"""
Mar 5, 2020 
Number of set bits in the binary representation of each number in given range. 0 to 2**n.
"""

N = int(input())
Permute = [list(map(int,bin(i)[2:])) for i in range(2**N)]
k = []
for i in range(2**N):
    if len(Permute[i]) < N:
        for j in range(N-len(Permute[i])):
            Permute[i].insert(0,0)
    k.append(sum(Permute[i]))

print(k)
