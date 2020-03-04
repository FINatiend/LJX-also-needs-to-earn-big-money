def convert(pRootOfTree):
    if not pRootOfTree:
        return
    phead = proot = pRootOfTree

    while phead.left:
        phead = phead.left
    core(proot)
    return phead

def core(proot):
    if not proot.left and not proot.right:
        return
    if proot.left:
        preRoot = proot.left
        core(proot.left)
        # 根节点左边是左子树中最大的
        while preRoot.right:
            preRoot = preRoot.right

        preRoot.right = proot
        proot.left = preRoot

    if proot.right:
        # 根节点右边是右子树中最小的
        nextRoot = proot.right
        core(proot.right)
        while nextRoot.left:
            nextRoot = nextRoot.left

        proot.right = nextRoot
        nextRoot.left = proot