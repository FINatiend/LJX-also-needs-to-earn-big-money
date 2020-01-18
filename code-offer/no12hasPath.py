class Solution:
    def hasPath(self, matrix, rows, cols, path):
        if len(matrix) == 0 or rows < 1 or cols < 1:
            return False
        visited = []

        pathLength = 0
        for row in range(0,rows):
            for col in range(0,cols):
                if self.hasPathCore(matrix,rows,cols,row,col,path,pathLength,visited):
                    return True
        return False

    def hasPathCore(self,matrix,rows,cols,row,col,path,pathLength,visited):
        if len(path) == pathLength:
            return True
        visited.append(False)
        hasPath = False
        if row >= 0 and row < rows and col >= 0 and col < cols and matrix[row * cols + col] == path[pathLength] and (not visited[row * cols + col]):
            pathLength += 1
            visited[row * cols + col] = True
            hasPath = self.hasPathCore(matrix,rows,cols,row,col-1,path,pathLength,visited) \
                      or self.hasPathCore(matrix,rows,cols,row-1,col,path,pathLength,visited) \
                      or self.hasPathCore(matrix,rows,cols,row,col+1,path,pathLength,visited) \
                      or self.hasPathCore(matrix,rows,cols,row+1,col,path,pathLength,visited)
            if(not hasPath):
                pathLength -= 1
                visited[row * cols + col] = False

        return hasPath

    def Test(self,testName,matrix,rows,cols,str,expected):
        print("begin:",testName)
        if self.hasPath(matrix,rows,cols,str) == expected:
            print("passed!")
        else:
            print("failed!")

    def Test1(self):
        matrix = "ABTGCFCSJDEH"
        str = "BFCE"
        self.Test("Test1",matrix,3,4,str,True)



if __name__ == "__main__":
    s = Solution()
    s.Test1()

