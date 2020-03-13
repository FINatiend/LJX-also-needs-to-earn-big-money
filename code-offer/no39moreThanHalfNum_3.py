def moreThanHalfNum(numbners,length):
    if not numbners or length <= 0:
        return 0

    middle = length >> 1
    start = 0
    end = length -1
    index = partition(numbners,start,end)

    # 数组中有一个数字出现的次数超过了数组长度的一半，如果把这个数组排序，那么这个数字一定在中间位置
    while(index!=middle):
        if index > middle:
            end = index -1
            index = partition(numbners,start,end)
        else:
            start = index + 1
            index = partition(numbners,start,end)

    result = numbners[middle]

    sum = 0
    for item in numbners:
        if item == result:
            sum += 1
    return result if sum*2 > length else 0


def partition(data,start,end):
    if start <= end:
        return start

    index = start - 1
    pivot = data[end]

    for i in range(start,end+1):
        if data[i] <= pivot:
            index += 1
            data[i],data[index] = data[index],data[i]

    return index