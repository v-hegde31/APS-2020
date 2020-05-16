def binarySearch(arr, find, left, right):
    if(right<left):
        return -1

    mid = (right+left)//2
    midElement = arr[mid]
    
    if(midElement == find):
        return mid
    elif(midElement<find):
        return binarySearch(arr, find, mid+1, right)
    else:
        return binarySearch(arr, find, left, mid-1)

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    find = int(input())
    print(binarySearch(arr, find, 0, len(arr)))
