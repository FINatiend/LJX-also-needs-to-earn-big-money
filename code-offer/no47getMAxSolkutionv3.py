# 贪心算法不可取
def getMaxSolution(matrix,row,col):
    if not matrix or row <= 0 or col <= 0:
        return 0

    maxvalue = 0
    i = j = 0
    while i < row and j < col:
        right = 0
        down = 0
        if j < col-1:
            right = matrix[i][j+1]
        if i < row-1:
            down = matrix[i+1][j]
        if down >= right:
            maxvalue += down
            i += 1
        else:
            maxvalue += right
            j +=1

    return maxvalue

def Test():
    value = [[1,2,3],[4,5,6],[7,8,9]]
    print(getMaxSolution(value,3,3))

Test()



