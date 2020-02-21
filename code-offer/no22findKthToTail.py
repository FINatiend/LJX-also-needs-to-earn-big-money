import ListNode
#主要是要考虑
def findKthToTail(listHead,k):
    # 为空时的情况，求倒数第k个的情况
    if listHead == None or k <= 0:
        return None
    head = listHead
    for i in range(0,k-1):
        # 当k大于链表长度的情况
        if head.next:
            head = head.next
        else:
            return None

    kthTail = listHead
    while head.next:
        head = head.next
        kthTail = kthTail.next

    return kthTail


