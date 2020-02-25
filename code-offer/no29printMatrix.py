def printMatrix(matrix):
    # # matrix类型为二维列表，需要返回列表
    #*matrix 将返回值其作为一个元组保存
    #[::-1]，即将列表第一个至最后一个复制，并且倒序
    # zip x = [1,2]
    #     y = [3,4]
    # zip(xy)
    # x = [1,3]
    # y = [2,4]
    return matrix and  list(matrix.pop(0)) + printMatrix(zip(*matrix)[::-1])

# matrix and [*matrix.pop(0)]是为了防止matrix为空时进行pop出错，and短路机制：matrix为[]时不再执行and后的语句。
# [::-1]每次都要进行旋转

def printMatrixClockwisely(matrix):
    if not matrix or len(matrix) <= 0 or len(matrix[0]) <= 0:
        return

    start = 0
    rows = len(matrix)
    cols = len(matrix[0])
    res = []

    while(cols > start *2 and rows > start * 2):
        printMatrixInCircle(matrix,cols,rows,start,res)
        start += 1

    return res

def printMatrixInCircle(matrix,columns,rows,start,res):
    endX = columns - start -1
    endY = rows - start -1

    # 从左到右打印第一行
    for i in range(start,endX+1):
        res.append(matrix[start][i])

    # 从上到下打印一列,，需要这一步的条件是至少有两行
    if start < endY:
        # 这一步的第一个也是上一步的最后一个，start+1
        for i in range(start+1,endY+1):
            res.append(matrix[i][endX])

    # 从右到左打印，需要这一步的条件是至少有两行两列
    if start < endX and start < endY:
        # 因为这一步的第一个是上一步的最后一个，因此这里的第一个是endx-1
        for i in range(endX-1,start-1,-1):
            res.append(matrix[endY][i])

    # 从下往上，需要这一步的条件是至少有三行两列
    if start < endX and start < endY -1:
        for i in range(endY-1,start,-1):
            res.append(matrix[i][start])

if __name__ == '__main__':
    matrix = [[1],[2],[3],[4],[5]]
    print(printMatrixClockwisely(matrix))


