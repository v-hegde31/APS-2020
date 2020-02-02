def lonelyinteger(a,n):
    k = a[0]
    for i in range(1,n):
        k = k^a[i]
    return k

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    result = lonelyinteger(a,n)
    print(result)
