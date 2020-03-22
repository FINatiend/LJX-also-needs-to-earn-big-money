# 这题画图可以得知：第一个公共节点出现后后面都相同，因此只要让那个长的先走，再两个一起走进行判断
def findFirstNode(pHead1,pHead2):
    length1 = pHead1.getLength()
    length2 = pHead2.getLength()
    subLength = length1 - length2

    # 关于链表的都不要用直接用头节点操作

    pListLong = pHead1
    pListShort = pHead2

    if length2 > length1:
        pListLong = pHead2
        pListShort = pHead1
        subLength = length2 - length1

    # 长链先走
    for i in range(subLength):
        pListLong = pListLong.next

    while pListLong and pListShort and pListLong!=pListShort:
        pListLong = pListLong.next
        pListShort = pListShort.next

    return pListLong


