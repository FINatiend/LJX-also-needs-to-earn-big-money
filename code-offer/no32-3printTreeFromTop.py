import BinaryTreeNode
def printTreeFromTop(rootNode):
    if not rootNode:
        return

    printList = []
    nodeList = []
    temp = []

    nodeList.append(rootNode)
    ifLeftToRight = True

    nextLevel = 0  #下一层要打印的节点数
    toBePrinted = 1 #这一层还没有打印的节点数

    while(len(nodeList)):

        node = nodeList.pop(0)
        temp.append(node.value)
        toBePrinted -= 1

        if node.left:
            nodeList.append(node.left)
            nextLevel += 1
        if node.right:
            nodeList.append(node.right)
            nextLevel += 1

        if toBePrinted == 0:
            if not ifLeftToRight:
                temp.reverse()
            printList.append(temp)
            temp = []
            toBePrinted = nextLevel
            nextLevel = 0
            ifLeftToRight = not ifLeftToRight


    for i in printList:
        print(i,end='')

def Test1():
    pNode10 = BinaryTreeNode.BinaryTreeNode(10);
    pNode6 = BinaryTreeNode.BinaryTreeNode(6);
    pNode14 = BinaryTreeNode.BinaryTreeNode(14);
    pNode4 = BinaryTreeNode.BinaryTreeNode(4);
    pNode8 = BinaryTreeNode.BinaryTreeNode(8);
    pNode12 = BinaryTreeNode.BinaryTreeNode(12);
    pNode16 = BinaryTreeNode.BinaryTreeNode(16);

    pNode10.connectTreeNodes(pNode10,pNode6, pNode14);
    pNode6.connectTreeNodes(pNode6,pNode4, pNode8);
    pNode14.connectTreeNodes(pNode14,pNode12, pNode16);

    pNode10.printTree(pNode10)

    print("The nodes from top to bottom, from left to right are: \n");
    printTreeFromTop(pNode10)

if __name__ == '__main__':
    Test1()

