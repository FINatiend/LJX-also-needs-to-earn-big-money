from collections import defaultdict
def MoreThanHalfNum(numbers,length):

    if not numbers or length <= 0:
        return 0

    dic = defaultdict(int)
    for item in numbers:
        dic[item] += 1
        if dic[item]*2 > length:
            return item
    # 当for循环中不存在满足条件的值时，返回0。这一步不要漏掉了
    return 0