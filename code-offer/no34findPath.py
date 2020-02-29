# 找到二叉树中某一值和的路径
def findPath(root,expectedSum):

    if not root:
        return []
    result = []

    def findPathCore(root,path,currentSum):
        currentSum += root.val
        path.append(root)

        ifLeaf = not (root.left or root.right)
        # 是叶子节点，且和为目标和
        if ifLeaf and currentSum==expectedSum:
            # result.append(path) 这里要加入节点的值，不能直接加入节点
            tempPath = []
            for node in path:
                tempPath.append(node.val)
            result.append(tempPath)

        # 是叶子节点，和大于目标和，直接pop，不是叶子节点同理
        # 不是叶子节点且和小于目标和，遍历其左右子树
        if (not ifLeaf) and currentSum<expectedSum:
            if root.left:
                findPathCore(root.left,path,currentSum)

            if root.right:
                findPathCore(root.right,path,currentSum)

        path.pop()


    findPathCore(root,[],0)
    return result
