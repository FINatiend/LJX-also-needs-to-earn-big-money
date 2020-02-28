def printFromTopToBottom(pTreeNode):
    if not pTreeNode:
        # 不能直接：  return
        # 这样做的话return出去仍然会进行执行下面的程序
        return []

    nodeQueue = []
    printList = []

    nodeQueue.append(pTreeNode)

    while(len(nodeQueue)>0):

        node = nodeQueue.pop(0)
        printList.append(node.val)

        if node.left:
            nodeQueue.append(node.left)

        if node.right:
            nodeQueue.append(node.right)

    return printList


