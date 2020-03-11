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
# 23ms 5828k

# -*- coding:utf-8 -*-

class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        length = len(numbers)
        if not numbers or length <= 0:
            return 0
        dic = {}
        for item in numbers:
            if not (item in dic):
                dic[item] = 0
            dic[item] += 1
            if dic[item] * 2 > length:
                return item
        return 0
#21ms 差不多