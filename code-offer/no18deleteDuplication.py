class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteDuplication_1(pHead):

    # 头节点也可能被删除！！！链表最高都先做个头节点备份
    firstNode = ListNode(-1)
    firstNode.next = pHead
    # lastNode跟着pnode行动，一直表示pnode的前一个
    lastNode = firstNode
    # while pHead.next:
    # 当为111111时，如果不判断pHead是否为空，在内层循环时pHead已经为None，会出错
    while pHead and pHead.next:
        if pHead.val == pHead.next.val:
            val = pHead.val
            while pHead and pHead.val == val:
                pHead = pHead.next
            lastNode.next = pHead
        else:
            lastNode = pHead
            pHead = pHead.next
    return firstNode.next

# 将链表元素保存在列表中，然后过滤掉出现次数大于1的值，只保留出现次数为1的值，再将新的列表建成链表的形式
def deleteDuplication_2(pHead):
    res = []
    while pHead:
        res.append(pHead.val)
        pHead = pHead.next
    # filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回一个迭代器对象，
    # 如果要转换为列表，可以使用 list() 来转换。
    # filter(function, iterable)
    # function – 判断函数。
    # iterable – 可迭代对象
    #count 统计某个字符出现的次数，c为遍历的数字，对每一个c求它出现的次数，过滤掉只出现一次的生成新列表
    res = list(filter(lambda c: res.count(c) == 1, res))

    newList = ListNode(0)
    pre = newList
    for i in res:
        node = ListNode(i)
        pre.next = node
        pre = pre.next
    return newList.next

