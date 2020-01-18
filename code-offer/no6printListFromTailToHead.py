#输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
from typing import List


class ListNode:
    def __init__(self,x):
        #init相当于构造方法，初始化时自动调用
        self.val = x
        self.next = None

    def generateList(self,l:list):
        preNode = self
        lastNode = preNode
        for val in l:
            lastNode.next = ListNode(val)
            lastNode = lastNode.next
        #print(preNode.next.val)
        return preNode.next

    def printList(self):
        while self:
            print(self.val)
            self = self.next

    def addList(self, x):
        preNode = self
        while self.next != None:
            self = self.next
        self.next = ListNode(x)
        self = self.next
        return preNode

    def deleteList(self,x):
        preNode = self
        pNode = self.next
        if self.val == x:
            self = self.next
        while pNode:
            if pNode.val == x:
                preNode.next = pNode.next
            pNode = pNode.next
            preNode = preNode.next
        return self

    def findList(self, x) -> bool:
        while self:
            if self.val == x:
                return True
            self = self.next
        return False

class Stack(object):
    def __init__(self):
        self.items = []

    """判断是否为空"""
    def is_empty(self):
        return self.items == []

    """添加元素"""
    def push(self,x):
        self.items.append(x)

    """弹出元素"""
    def pop(self):
        return self.items.pop()

    """返回栈顶元素"""
    def peek(self):
        return self.items[len(self.items)-1]

    """返回栈的大小"""
    def size(self):
        return len(self.items)


class Solution:
    def printListFromTailToHead(self,l:ListNode):
        tempStack = Stack()
        pNode = l
        while pNode:
            tempStack.push(pNode)
            pNode = pNode.next

        while not tempStack.is_empty():
            print(tempStack.pop().val)


s1 = ListNode(0)
l = [1,2,3,4,5,6,7]
s1 = s1.generateList(l)
ss = Solution()
ss.printListFromTailToHead(s1)

s2 = ListNode(0)
l2 = [1]
s2 = s2.generateList(l2)
ss.printListFromTailToHead(s2)
s3 = ListNode(0)
l3 = []
s3 = s3.generateList(l3)
ss.printListFromTailToHead(s3)
#s.printList()
#s.addList(9)
#s.deleteList(1)
#print(s.findList(2))
#s.printList()

