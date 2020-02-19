# o(1)时间删除节点i
# 数据结构方法，遍历后到下一节点为i时把指针指向i的下下一个节点，，因链表只有指向下一节点的指针o（n）
# 改进方法，直接将i的下一节点j复制到i，改为删除j
# 若要删除的节点为尾节点或者只有一个节点（也即为尾节点），另外考虑
# 1. 不是尾节点
# else：1.只有一个节点 2。否则
# 确保要删除的节点在链表中，否则判断的这一过程仍然需要o(n)
class ListNode:
    def __init__(self,x):
        self.value = x
        self.next = None

    def connectListNode(self,listnode):
        self.next = listnode

    def printList(self):
        while self:
            print(self.value)
            self = self.next

def deleteNode(listHead:ListNode,nodeToBeDeleted:ListNode):
    if not (listHead and nodeToBeDeleted):
        return
    # 要删除的不是尾节点
    if nodeToBeDeleted.next:
        pnext = nodeToBeDeleted.next
        nodeToBeDeleted.value = pnext.value
        nodeToBeDeleted.next = pnext.next
        pnext.value = None
        pnext.next = None
    # 只有一个节点
    elif listHead == nodeToBeDeleted:
        listHead.value = None
        nodeToBeDeleted.value = None
    # 删除尾节点，遍历
    else:
        pnode = listHead
        while pnode.next != nodeToBeDeleted:
            pnode = pnode.next
        pnode.next = None
        nodeToBeDeleted.value = None
        nodeToBeDeleted.next = None

def Test(pListHead,pNode):
    if not pListHead:
        print("empty")
        return
    print("original list:")
    pListHead.printList()
    print("the node to be deleted:")
    print(pNode.value)
    deleteNode(pListHead,pNode)
    print("the result:")
    pListHead.printList()

# 多个节点，删除中间节点
def Test1():
    print("111111begin")
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.connectListNode(node2)
    node2.connectListNode(node3)
    node3.connectListNode(node4)
    node4.connectListNode(node5)
    Test(node1,node3)

#   多个节点，删除尾节点
def Test2():
    print("222222begin")
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.connectListNode(node2)
    node2.connectListNode(node3)
    node3.connectListNode(node4)
    node4.connectListNode(node5)
    Test(node1,node5)

#  多个节点，删除头节点
def Test3():
    print("33333begin")

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.connectListNode(node2)
    node2.connectListNode(node3)
    node3.connectListNode(node4)
    node4.connectListNode(node5)
    Test(node1,node1)

#一个节点，删除头节点
def Test4():
    print("44444begin")

    node1 = ListNode(1)

    Test(node1,node1)

def Test5():
    print("55555begin")

    Test(None,None)

if __name__ == '__main__':
    Test1()
    Test2()
    Test3()
    Test4()
    Test5()





