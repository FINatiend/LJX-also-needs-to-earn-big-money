from typing import List
class Solution:
    def findNum(self,array: List[List[int]],number:int)->bool:
        rows = len(array)
        columns = len(array[0])
        if rows>0 and columns>0:
            row = 0
            column = columns-1
            while row<rows and column>=0:
                if array[row][column] ==number:
                    return True
                elif array[row][column]>number:
                    column = column-1
                else:
                    row = row+1
        return False


if __name__=='__main__':
    array = [[1,2,8,9],
             [2,4,9,12],
             [4,7,10,15],
             [6,8,11,15]]
    print(s.findNum(array,7))
    s = Solution()