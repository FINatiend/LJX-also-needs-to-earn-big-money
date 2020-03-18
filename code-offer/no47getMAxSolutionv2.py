def getMaxSolution(matrix,row,col):
    if not matrix or row <= 0 or col <= 0:
        return 0
    # maxValues = [[0 for i in range(cols)] for j in range(rows)]
    maxValueList = [0 for i in range(col)]

    for i in range(0,row):
        for j in range(0,col):
            left = 0
            up = 0

            if i > 0:
                up = maxValueList[j]
            if j > 0:
                left = maxValueList[j-1]

            maxValueList[j] = max(up,left) + matrix[i][j]
    maxValue = maxValueList[col-1]

    del maxValueList

    return maxValue

def Test():
    value = [[1,2,3],[4,5,6],[7,8,9]]
    print(getMaxSolution(value,3,3))

Test()



