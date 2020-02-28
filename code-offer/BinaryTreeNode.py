class BinaryTreeNode():
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

    def connectTreeNodes(self,pParent,pLeft,pRight):
        if pParent:
            pParent.left = pLeft
            pParent.right = pRight

    def printTree(self,root):
        if not root:
            return False

        print(root.value,end='')
        if root.left:
            self.printTree(root.left)
        if root.right:
            self.printTree(root.right)

