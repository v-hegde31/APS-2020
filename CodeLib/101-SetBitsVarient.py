def countSetBits(n):
    count = 0
    while n>0:
        n=n&(n-1)
        count+=1
    return count

if __name__ == "__main__":
    print(countSetBits(int(input()))
