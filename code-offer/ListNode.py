class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

    def generateList(self,l:list):
        preNode = self
        lastNode = preNode
        for val in l:
            lastNode.next = ListNode(val)
            lastNode = lastNode.next
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

    def deleteList(self, x):
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

