def treeDepth(proot):
    if not proot:
        return 0
    left = treeDepth(proot.left)
    right = treeDepth(proot.right)
    return max(left,right)+1

def isbalance(proot):
    if not proot:
        return True

    left = treeDepth(proot.left)
    right = treeDepth(proot.right)

    diff = left - right
    if diff <=1 or diff >= -1:
        return True
    return isbalance(proot.left) and isbalance(proot.right)


