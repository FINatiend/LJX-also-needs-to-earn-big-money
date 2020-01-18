from typing import List


class Solution:
    def countRange(self,numbrs:List[int],start:int,end:int) -> int:
        length = len(numbrs)
        count = 0
        for i in range(length):
            if numbrs[i] >= start and numbrs[i] <= end:
                count +=1
        return count

    def duplication(self,numbers:List[int]) -> int:
        length = len(numbers)
        if length <= 0 :
            return -1
        start = 1
        end = length - 1
        while end >= start:
            middle = ((end-start)>>1) +start
            count = self.countRange(numbers,start,middle)
            if end == start:
                if count > 1:
                    return start
                else:
                    return -1
            if count >(middle - start)+1:
                end = middle
            else:
                start = middle +1
        return -1

if __name__ == '__main__':
    s = Solution()
    numbers = [2,3,5,4,3,2,6,7]
    print(s.duplication(numbers))