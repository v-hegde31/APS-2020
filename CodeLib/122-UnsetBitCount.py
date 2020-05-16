def main():
    n = int(input())
    if n==0:
        print(1)
    else:
        print(pow(2,bin(n).count("0")-1))

if __name__ == "__main__":
    main()
