import BinaryTreeNode
def printTreeFromTop(rootNode):
    if not rootNode:
        return []

    printList = []
    nodeQueue = []

    nodeQueue.append(rootNode)

    nextLevel = 0  #下一层要打印的节点数
    toBePrinted = 1 #这一层还没有打印的节点数
    temp = []
    while(len(nodeQueue)):
        node = nodeQueue.pop(0)
        temp.append(node.value)
        toBePrinted -= 1

        if node.left:
            nodeQueue.append(node.left)
            nextLevel += 1

        if node.right:
            nodeQueue.append(node.right)
            nextLevel += 1

        if toBePrinted == 0:
            printList.append(temp)
            temp = []
            toBePrinted = nextLevel
            nextLevel = 0

    # return printList
    for i in printList:
        print(i,end='')

def Test(name,rootnode):
    if len(name):
        print(name+"begin")

    rootnode.printTree(rootnode)

    print("The nodes from top to bottom, from left to right are: \n");
    printTreeFromTop(rootnode)

    print("\n\n");

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

    Test("test1",pNode10)

if __name__ == '__main__':
    Test1()


