import ListNode
def findMeetingNode(pHead):
    if pHead == None:
        return None
    pSlow = pHead.next
    if pSlow == None:
        return None
    pFast = pSlow.next
    # if pFast == None:
    #     return None
    # 判断快的指针和慢的指针是否会相遇，相遇代表有环
    while pSlow and pFast:
        if pSlow == pFast:
            return pFast

        pSlow = pSlow.next
        pFast = pFast.next
        # 快的指针先走一步，注意判断
        if pFast:
            pFast = pFast.next

    return None

# 有相遇的情况下，在相遇点再走一圈可以求的环的步数，从而可以求的环的入口
def entryNodeOfLoop(pHead):
    meetingNode = findMeetingNode(pHead)
    if not meetingNode:
        return None

    # 求的环中节点的数目
    nodeInLoop = 1
    pNode_1 = meetingNode
    while pNode_1.next != meetingNode:
        nodeInLoop += 1
        pNode_1 = pNode_1.next

    # 从第一个节点开始，设置两个链表，第一个比第二个先走nodeInLoop步
    pFast = pHead
    for i in range(0,nodeInLoop):
        pFast = pFast.next

    pSlow = pHead
    while pFast != pSlow:
        pFast = pFast.next
        pSlow = pSlow.next

    return pFast