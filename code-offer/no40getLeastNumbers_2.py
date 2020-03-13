def getLeastNumbers(arr,k):
    if not arr or not k or k < 1 or len(arr) <= 0:
        return

    start = 0
    end = len(arr) - 1
    index = partition(arr,start,end)

    while(index != k-1):
        if index > k-1:
            end = index -1
            index = partition(arr,start,end)
        else:
            start = index +1
            index = partition(arr,start,end)

    return arr[:k]

def partition(data,start,end):
    if start >= end:
        return start

    index = start - 1
    pivot = data[end]

    for i in range(start,end+1):
        if data[i] <= pivot:
            index += 1
            data[i],data[index] = data[index],data[i]

    return index

if __name__ == "__main__":
    arr1 = [4, 5, 1, 6, 2, 7, 3, 8]
    res = getLeastNumbers(arr1,6)
    for item in res:
        print(item)
    # arr2 = [4, 5, 1, 6, 2, 7, 3, 8]
    # getLeastNumbers(arr2,None)
    # arr3=[4, 5, 1, 6, 2, 7, 2, 8]
    # getLeastNumbers(arr2,2)


