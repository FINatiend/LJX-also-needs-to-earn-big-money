def Partition(data,length,start,end):
    if not data or length <= 0 or start < 0 or end < 0:
        return

    index = start - 1
    pivot = data[end]

    for i in range(start,end+1):
        if data[i] <= pivot:
            index += 1
            data[index],data[i] = data[i],data[index]

    return index

def quickSort(data,start,end):

    if start == end:
        return

    length = len(data)

    if start < end:
        p = Partition(data,length,start,end)
        quickSort(data,start,p-1)
        quickSort(data,p+1,end)

if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quickSort(arr, 0, n - 1)
    print("排序后的数组:")
    for i in range(n):
        print("%d" % arr[i]),