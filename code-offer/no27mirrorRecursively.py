def mirrorRecursively(pNode):
    if not pNode:
        return

    pTemp = pNode.left
    pNode.left = pNode.right
    pNode.right = pTemp

    if pNode.left:
        mirrorRecursively(pNode.left)
    if pNode.right:
        mirrorRecursively(pNode.right)