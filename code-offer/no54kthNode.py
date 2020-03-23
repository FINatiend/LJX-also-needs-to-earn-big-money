def kthNode(proot,k):
    if not proot or k <= 0:
        return None
    res = []
    def core(proot):
        if not proot:
            return
        core(proot.left)
        res.append(proot)
        core(proot.right)
        return res
    core(proot)

    if len(res) < k:
        return None
    return res[k-1]

