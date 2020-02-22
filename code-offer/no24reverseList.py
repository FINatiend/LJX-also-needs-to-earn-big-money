# 分析，将链表倒转即将节点的next都指向pre，且不造成断裂，因此需知道节点的next和pre

import ListNode
def reverseList(pHead):
    pReverseHead = None
    pPre = None
    pNode = pHead
    while pNode:
        pNext = pNode.next

        if not pNext:
            pReverseHead = pNode

        pNode.next = pPre
        pPre = pNode
        pNode = pNext

    return pReverseHead

def Test(testname,pHead):
    if len(testname) != 0:
        print(testname+"begin")
    pHead.printList()
    print('\t')
    pHead = reverseList(pHead)
    pHead.printList()
    print('\t')


if __name__ == '__main__':
    node1 = ListNode.ListNode(1)
    node1.generateList([2,3,4,5])
    Test('test1',node1)

    node2 = ListNode.ListNode(1)
    node2.generateList([])
    Test('test2',node1)

    Test("test3",None)




