from typing import List


class Solution:
    def duplicate(self,numbers:List[int]) ->int:
        numlength = len(numbers)
        i =j= 0
        if numlength<=0:
            return False
        for i in range(numlength):
            if numbers[i]<0 or numbers[i]>numlength-1:
                return False
        for j in range(numlength):
            while numbers[j] != j:
                if numbers[j] == numbers[numbers[j]]:
                    return numbers[j]
                else:
                    temp = numbers[j]
                    numbers[j] = numbers[temp]
                    numbers[temp] = temp
        return -1

if __name__=='__main__':
    s = Solution()
    numbers = [2,3,1,0,2,5,3]
    print(s.duplicate(numbers))