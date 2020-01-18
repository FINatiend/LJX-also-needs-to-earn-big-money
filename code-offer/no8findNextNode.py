class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        self.parent = None

def connectreeNodes(pParent:BinaryTree,pLeft:BinaryTree,pRight:BinaryTree):
    if pParent:
        pParent.leftChild = pLeft
        pParent.rightChild = pRight
        if pLeft:
            pLeft.parent = pParent
        if pRight:
            pRight.parent = pParent

def printTreeNode(pNode:BinaryTree):
    if pNode:
        print("value of this node is: %d\n", pNode.key)
        if pNode.leftChild:
            print("value of its left child is: %d.\n", pNode.leftChild.key)
        else:
            print("left child is null.\n")
        if pNode.rightChild:
            print("value of its right child is: %d.\n", pNode.rightChild.key)
        else:
            print("right child is null.\n")
    else:
        print("this node is null.\n")
    print("\n")

def printTree(pRoot:BinaryTree):
    printTreeNode(pRoot)
    if pRoot:
        if pRoot.leftChild:
            printTree(pRoot.leftChild)
        if pRoot.rightChild:
            printTree(pRoot.rightChild)

def getNext(pNode:BinaryTree):
        if not pNode :
            return None

        pNext = BinaryTree(0)
        if pNode.rightChild :
            pRight = pNode.rightChild
            while pRight.rightChild :
                pRight = pRight.leftChild

            pNext = pRight

        elif pNode.parent:
            pCurrent = pNode
            pParent = pNode.parent
            while pParent and pCurrent == pParent.rightChild:
                pCurrent = pParent
                pParent = pParent.parent
            pNext = pParent

        return pNext

def Test(testName:str,pNode:BinaryTree,expectedNode:BinaryTree):
    if testName:
        print(testName+" begins")

    pNext = getNext(pNode)
    if pNext == expectedNode:
        print("passed\n")
    else:
        print("failed\n")

def Test1_7():
    pNode8 = BinaryTree(8)
    pNode6 = BinaryTree(6)
    pNode10 = BinaryTree(10)
    pNode5 = BinaryTree(5)
    pNode7 = BinaryTree(7)
    pNode9 = BinaryTree(9)
    pNode11 = BinaryTree(11)

    connectreeNodes(pNode8,pNode6,pNode10)
    connectreeNodes(pNode6,pNode5,pNode7)
    connectreeNodes(pNode10,pNode9,pNode11)

    Test("Test1",pNode8,pNode9)

if __name__ == '__main__':
    Test1_7()







