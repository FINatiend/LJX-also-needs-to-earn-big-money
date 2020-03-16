import maxHeap
import minHeap
class Solution:
    def __init__(self):
        arr = []
        self.minHeap = minHeap.MinHeap(arr)
        self.maxHeap = maxHeap.MaxHeap(arr)

    def insert(self,num):
        # 这里实际奇数次时插入了小根堆，因为奇数次时count为偶数
        # 奇数时插入大根堆
        if (self.minHeap.count + self.maxHeap.count) & 1 == 1:
            # 如果奇数位时插入的数字比大小根堆的最小值还要大，就先插入小根堆，再把小根堆中的最小的数插入大根堆
            if self.minHeap.count > 0 and num > self.minHeap.data[0]:
                self.minHeap.insert(num)
                num = self.minHeap.extractMin()
            self.maxHeap.insert(num)

        # 偶数时插入小根对
        else:
            # 如果偶数位时插入的数字比大根堆的最大值还要小，，就先插入大根堆，再把大根堆中的最大的数插入小根堆
            if self.maxHeap.count > 0 and num < self.maxHeap.data[0]:
                self.maxHeap.insert(num)
                num = self.maxHeap.extractMax()
            self.minHeap.insert(num)

    def getMedian(self):
        size = self.maxHeap.count + self.minHeap.count
        if size == 0:
            return
        medium = 0
        if size & 1 == 1:
            medium = self.minHeap.data[0]
        else:
            medium = (self.minHeap.data[0]+self.maxHeap.data[0])/2
        return medium

    def Test(self,expected):


        if (abs(self.getMedian() - expected) < 0.0000001):
            print("Passed.\n")
        else:
            print("FAILED.\n")


if __name__ == '__main__':
    s = Solution()
    nums = [5,2,3,4,1,6,7,0,8]
    rightnum = [5,3.5,3,3.5,3,3.5,4,3.5,4]
    if not s.getMedian() and s.maxHeap.isEmpty() and s.minHeap.isEmpty():
        print("Passed.\n")
    else:
        print("FAILED.\n")

    for i in range(0,9):

        s.insert(nums[i])
        s.Test(rightnum[i])








