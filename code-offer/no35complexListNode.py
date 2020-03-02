import ComlplexListNode



def cloneNode(pHead):
    pNode = pHead
    while pNode:
        pClone = ComlplexListNode.ListNode(pNode.val)
        pClone.next = pNode.next
        pNode.next = pClone
        pNode = pClone.next

def connectSiblingNode(pHead):
    pNode = pHead

    while pNode:
        pClone = pNode.next
        # 这里要加一层判断
        if pNode.sibling:
            pClone.sibling = pNode.sibling.next
        pNode = pClone.next

def reconnectNode(pHead):
    pNode = pHead
    pCLoneHead = pCloneNode =pNode.next
    pNode.next = pCloneNode.next
    pNode = pNode.next

    while pNode:
        pCloneNode.next = pNode.next
        pCloneNode = pCloneNode.next
        pNode.next = pCloneNode.next
        pNode = pNode.next
    return pCLoneHead


def Clone(pHead):
    if not pHead:
        return None
    cloneNode(pHead)
    connectSiblingNode(pHead)
    return reconnectNode(pHead)

def Test1():
    pNode1 = ComlplexListNode.ListNode(1)
    pNode2 = ComlplexListNode.ListNode(2)
    pNode3 = ComlplexListNode.ListNode(3)
    pNode4 = ComlplexListNode.ListNode(4)
    pNode5 = ComlplexListNode.ListNode(5)

    pNode1.connectNodes(pNode2,pNode3)
    pNode2.connectNodes(pNode3,pNode5)
    pNode3.connectNodes(pNode4,None)
    pNode4.connectNodes(pNode5,pNode2)

    pNode1.printList()

    Clone(pNode1)

    pNode1.printList()


if __name__ == '__main__':
    Test1()