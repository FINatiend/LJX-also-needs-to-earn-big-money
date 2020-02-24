def isSymmetrical(pRoot):
    if not pRoot:
        return True

    return isEqual(pRoot.left,pRoot.right)


def isEqual(pLeft,pRight):
    if not (pLeft or pRight):
        return True
    if not (pLeft and pRight):
        return False
    if pLeft.val != pRight.val:
        return False
    return isEqual(pLeft.left,pRight.right) and isEqual(pLeft.right,pRight.left)

# 原版本
#
# def isEqual(pLeft,pRight):
# ！！！！1.这里不能直接判断，而要判断他们的值，因为有不同节点值相同的情况
# ！！！！2.先判断这一步再判断空的话，就会存在判断空指针的val的情况，所以要先判空
#     if pLeft != pRight:
#         return False
#     if not pLeft:
#         return
#     isEqual(pLeft.left,pRight.right)
#     isEqual(pLeft.right,pRight.left)
#     这样的话怎么着都只会返回true。。。silly
#     return True
