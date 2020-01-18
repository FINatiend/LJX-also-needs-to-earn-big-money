class Solution:
    def movingCount(self,threashold,rows,cols):
        if threashold < 0 and rows <= 0 and cols <= 0:
            return 0
        visited = []
        for i in range(0,rows*cols):
            visited.append(False)

        count = self.movingCountCore(threashold,rows,cols,0,0,visited)
        return count

    def movingCountCore(self,threashold,rows,cols,row,col,visited):
        count = 0

        if self.check(threashold,rows,cols,row,col,visited):
            visited[row * cols + col] = True

            count = 1 + self.movingCountCore(threashold,rows,cols,row-1,col,visited) \
                    + self.movingCountCore(threashold,rows,cols,row+1,col,visited) \
                    + self.movingCountCore(threashold,rows,cols,row,col-1,visited) \
                    + self.movingCountCore(threashold,rows,cols,row,col+1,visited)
        # print("colount:",count)
        return count


    def check(self,threashold,rows,cols,row,col,visited):
        if row >=0 and row < rows and col >= 0 and col < cols\
                and (self.getDigitSum(row) + self.getDigitSum(col)) <= threashold\
                and not(visited[row*cols + col]):
            return True
        return  False



    def getDigitSum(self,number):
        # print("number:",number)
        sum = 0
        while(number > 0):
            sum += number %10
            number = number //10
        # print("sum:",sum)
        return sum

    def test(self,testName,threshold,rows,cols,expected):
        if len(testName) != 0:
            print("{}begins\n".format(testName))
        if self.movingCount(threshold,rows,cols) == expected:
            print("passed\n")
        else:
            print("failed\n")

if __name__ == "__main__":
    s = Solution()
    s. test("Test1", 5, 10, 10, 21)#多行多列
    s.test("Test3", 10, 1, 100, 29)#一行到达部分方格
    s.test("Test5", 15, 100, 1, 79)#一列到达部分方格
    s.test("Test4", 10, 1, 10, 10)#一行到达所有方格
    s.test("Test6", 15, 10, 1, 10)#一列到达所有方格
    s.test("Test7", 0, 1, 1, 1)#一行一列
    s.test("Test9", -10, 10, 10, 0)#不能进入任意一个方格






