def isBalanced(proot,depth):
    if not proot:
        depth = 0
        return True

    leftDepth = rightDepth = -1
    # 递归，一步步往下判断左右是否是平衡树，不是就返回，是的话记录当前的深度
    if isBalanced(proot.left,leftDepth) and isBalanced(proot.right,rightDepth):
        diff = leftDepth - rightDepth
        if diff <= 1 and diff >= -1:
            depth = max(leftDepth,rightDepth)+1
            return True

    return False


def isBalanced(proot):
    return isBalanced(proot,0)
