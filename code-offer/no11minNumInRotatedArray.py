# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        length = len(rotateArray)
        if length <= 0:
            return 0

        index1 = 0
        index2 = length - 1
        indexMid = index1

        while rotateArray[index1] >= rotateArray[index2]:
            if index2 - index1 == 1:
                indexMid = index2
                break
            indexMid = (index1 + index2) / 2

            if rotateArray[index1] == rotateArray[index2] and rotateArray[index2] == rotateArray[indexMid]:
                return self.minInOrder(rotateArray,index1,index2)


            if rotateArray[indexMid] >= rotateArray[index1]:
                index1 = indexMid
            elif rotateArray[indexMid] <= rotateArray[index2]:
                 index2 = indexMid

        return rotateArray[indexMid]

    def minInOrder(self,rotateArray,index1,index2):
        result = rotateArray[index1]

        for i in rotateArray:
            if result > i:
                result = i
        return result

