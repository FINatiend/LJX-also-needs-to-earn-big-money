def hasSubTree(proot1,proot2):
    result = False

    if proot1 and proot2:
        if proot1.value == proot2.value:
            # 相等则判断各自的左右子树是否相等
            result =  ifEqual(proot1,proot2)

        if not result:
            result = hasSubTree(proot1.left,proot2)

        if not result:
            result = hasSubTree(proot1.right,proot2)


    return result

def ifEqual(proot1,proot2):

    # 若proot2为空，则是其子树
    if not proot2:
        return True
    if not proot1:
        return False

    if proot2.value != proot1.value:
        return False

    return ifEqual(proot1.left,proot2.left) and ifEqual(proot1.right,proot2.right)