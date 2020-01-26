"""
To create permutatoins of 0,1 to N numbers using binary.
"""
N = int(input())
Permute = [list(map(int,bin(i)[2:])) for i in range(2**N)]
for i in range(2**N):
    if len(Permute[i]) < N:
        for j in range(N-len(Permute[i])):
            Permute[i].insert(0,0)
print(Permute)
