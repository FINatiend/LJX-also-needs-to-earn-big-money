import copy
def inverPair(data):
    if len(data) <= 0:
        return 0

    count = 0
    copyData = copy.copy(data)
    copyData.sort()

    for i in range(len(copyData)):
        count += data.index(copyData[i])
        data.remove(copyData[i])

    return count % 1000000007

def Test():
    data1 = [1, 2, 1, 2, 1]
    print(inverPair(data1))
Test()