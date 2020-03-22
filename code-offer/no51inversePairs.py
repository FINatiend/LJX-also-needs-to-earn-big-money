import copy
def inverPair(data):
    if not data or len(data) <= 0:
        return 0

    count = 0
    copyData = copy.copy(data)
    copyData.sort()

    # 先排序，排序后的数组从小到大，那么排序数组中的最小的在原数组中的index是多少，
    # 它前面就有多少个大于它的数
    for i in range(len(copyData)):
        count += data.index(copyData[i])
        data.remove(copyData[i])

    return count % 1000000007

def Test():
    data1 = [1, 2, 1, 2, 1]
    print(inverPair(None))
Test()