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