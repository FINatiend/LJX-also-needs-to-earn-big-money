class BinaryTreeNode():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def connectTreeNodes(self,pParent,pLeft,pRight):
        if pParent:
            pParent.left = pLeft
            pParent.right = pRight
