"""
Python program to find the absolute difference between the sums of both diagonals of a square matrix.
"""

def diagonalDifference(arr):
    sum1,sum2=0,0
    n=len(arr)
    for i in range(n):
        sum1+=arr[i][i]
        sum2+=arr[i][n-i-1]
    return abs(sum1-sum2)  

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
    print(result)
