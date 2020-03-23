# 按位与 & 两位相等为1
# 按位异或 ^ 两位不等为1
def findNumsAppearOnce(data,length):
    if not data or length < 2:
        return
    resEOR = 0
    for i in data:
        resEOR = resEOR ^ i
    indexOf1 = findFirstBits1(resEOR)
    res1,res2 = 0,0

    for i in data:
        if isBit1(i,indexOf1):
            res1 = res1 ^ i
        else:
            res2 = res2 ^ i
    return [res1,res2]


#  在整数num中找到最右边是1的位
def findFirstBits1(num):
    indexBit = 0
    while ((num&1) == 0 and indexBit < 32):
        num = num >> 1
        indexBit += 1
    return indexBit

#  判断从num开始的第index位是不是1
def isBit1(num,index):
    num = num >> index
    a = (num&1)
    return (num & 1)

data = [2,4,3,6,3,2,5,5]
print(findNumsAppearOnce(data,8))