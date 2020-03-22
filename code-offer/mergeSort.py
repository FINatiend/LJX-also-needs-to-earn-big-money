# 这里一定要记得起始位置，不是从0开始

def merge(arr,start,middle,end):
    len1 = middle - start + 1
    len2 = end - middle
    L_list = [0]*len1
    R_list = [0]*len2

    for i in range(len1):
        L_list[i] = arr[start+i]

    for i in range(len2):
        R_list[i] = arr[i+middle+1]

    i = 0
    j = 0
    # 归并数组的索引,k从start开始！！！
    k = start

    while i < len1 and j <len2:
        if L_list[i] <= R_list[j]:
            arr[k] = L_list[i]
            i+=1
        else:
            arr[k] = R_list[j]
            j+=1
        k += 1
    # 拷贝剩下的
    while i < len1:
        arr[k] = L_list[i]
        i+=1
        k+=1
    while j < len2:
        arr[k] = R_list[j]
        j+=1
        k+=1

def mergeSort(arr,start,end):
    # 这里一定要记得起始位置，不是从0开始
    if start < end:
        middle = (end+start)//2

        mergeSort(arr,start,middle)
        mergeSort(arr,middle+1,end)
        merge(arr,start,middle,end)


arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("给定的数组")
for i in range(n):
    print("%d " % arr[i],end='')

mergeSort(arr, 0, n - 1)
print("\n\n排序后的数组")
for i in range(n):
    print("%d " % arr[i],end='')



