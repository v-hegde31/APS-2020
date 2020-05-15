def kaprekarNumbers(p, q):
    kaprekar = []
    if p == 1:
        kaprekar.append(1)
        p = 4
    for i in range(p,q+1):
        k = str(i*i)
        l = len(k)
        rem = l-len(str(i))
        l = k[:rem]
        l = int(l)
        r = k[rem:]
        r = int(r)
        if l+r==i:
            kaprekar.append(i)
    if len(kaprekar)==0:
        print("INVALID RANGE")
    else:
        for i in kaprekar:
            print(i,end = " ")

if __name__ == '__main__':
    p = int(input())
    q = int(input())

    kaprekarNumbers(p, q)
