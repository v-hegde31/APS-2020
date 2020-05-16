def setBit(n, i):
    n = n | (1<<i)
    return n

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        print(setBit(map(int,input().split(" ")))
