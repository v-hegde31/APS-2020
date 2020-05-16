def checkSetBit(n, i):
    if n & (1<<i) == 0:
        return False
    else:
        return True

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n,i = map(int,input().split(" "))
        print(checkSetBit(n,i))
