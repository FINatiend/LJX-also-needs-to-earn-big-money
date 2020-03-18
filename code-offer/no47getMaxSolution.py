def getMaxSolution(matrix,row,col):
    if not matrix or row <= 0 or col <= 0:
        return 0
    maxValue_row = [0] * col
    # maxValues = [[0 for i in range(cols)] for j in range(rows)]
    maxValueMatrix = [maxValue_row] * row

    for i in range(0,row):
        for j in range(0,col):
            left = 0
            up = 0

            if i > 0:
                up = maxValueMatrix[i-1][j]
            if j > 0:
                left = maxValueMatrix[i][j-1]

            maxValueMatrix[i][j] = max(up,left) + matrix[i][j]
    maxValue = maxValueMatrix[row-1][col-1]

    del maxValueMatrix

    return maxValue

def Test():
    value = [[1,2,3],[4,5,6],[7,8,9]]
    print(getMaxSolution(value,3,3))

Test()



