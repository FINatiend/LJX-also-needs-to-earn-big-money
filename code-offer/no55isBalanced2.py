def isBalanced(proot,depth):
    if not proot:
        depth = 0
        return True

    leftDepth = rightDepth = -1
    if isBalanced(proot.left,leftDepth) and isBalanced(proot.right,rightDepth):
        diff = leftDepth - rightDepth
        if diff <= 1 and diff >= -1:
            depth = max(leftDepth,rightDepth)+1
            return True

    return False


def isBalanced(proot):
    return isBalanced(proot,0)
