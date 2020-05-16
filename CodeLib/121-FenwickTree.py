def isolateOneBit(n):
    return n & -n

def getSum(BIT, ind):
    s = 0
    num = ind
    while num > 0:
        s += BIT[num]
        # print(bin(num))
        num -= isolateOneBit(num)
    return s

def rangeSum(BIT,l,u):
    uSum = getSum(BIT, u)
    lSum = getSum(BIT,l-1)
    return uSum-lSum

def updateSums(BIT, nBIT, ind, delta):
    while(ind<=nBIT):
        # print(bin(ind))
        BIT[ind] += delta
        ind += isolateOneBit(ind)

def constructTree(arr, n):
    BIT = [ 0 for _ in range(n+1) ]
    for i in range(n):
        updateSums(BIT,n+1,i+1,arr[i])
    return BIT


def main():
    arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
    BIT = constructTree(arr, 12)
    print(getSum(BIT, 12))
    print(rangeSum(BIT, 1,5))

if __name__ == "__main__":
    main()
