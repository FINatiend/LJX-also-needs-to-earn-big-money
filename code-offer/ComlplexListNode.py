class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
        self.sibling = None


    def printList(self):
        while self:
            print(self.val)
            if self.sibling:
                print("sibiling:",self.sibling.val)
            self = self.next
        print("\n")

    def connectNodes(self, pNext, pSibiling):
        self.next = pNext
        self.sibling = pSibiling
