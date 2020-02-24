def merge(phead1,phead2):
    if not phead1:
        return phead2
    elif not phead2:
        return phead1
    # 每选出一个新链表的头节点，剩下的过程是一个递归的过程，
    # 用递归就不存在之后再进行尾节点的判断以及记录节点的下一个节点，前一个节点之类的问题
    if phead1.val <= phead2.val:
        pMergeHead = phead1
        pMergeHead.next = merge(phead1.next,phead2)

    # 两个 <= 会递归死循环
    # if phead2.val <= phead1.val:
    else:
        pMergeHead = phead2
        pMergeHead.next = merge(phead1,phead2.next)

    return pMergeHead