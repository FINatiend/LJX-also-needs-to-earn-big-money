import maxHeap
def getLeastNumbers(arr,k):
    if not k or not arr or k < 1 or len(arr) < k :
        return
    heap = maxHeap.MaxHeap(arr[:k])
    for item in arr[k:]:
        if item < heap.data[0]:
            heap.extractMax()
            heap.insert(item)

    for item in heap.data:
        print(item)

if __name__ == "__main__":
    # arr1 = [4, 5, 1, 6, 2, 7, 3, 8]
    # getLeastNumbers(arr1,4)
    arr2 = [4, 5, 1, 6, 2, 7, 3, 8]
    getLeastNumbers(arr2,None)
    # arr3=[4, 5, 1, 6, 2, 7, 2, 8]
    # getLeastNumbers(arr2,2)