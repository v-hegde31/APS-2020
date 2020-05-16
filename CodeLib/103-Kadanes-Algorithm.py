"""
Maximum Subarray Sum - O(n)
"""

def kadane(a, size):
    maxVal, tempMax = float('-inf'), 0
    for i in range(size):
        tempMax += a[i]
        if maxVal < tempMax:
            maxVal = tempMax
        if tempMax < 0:
            tempMax = 0
    return maxVal
    
if __name__=='__main__':
    n = int(input())
    a = list(map(int,input().split(' ')))
    print('Maximum Subarray Sum =',kadane(a,n))
