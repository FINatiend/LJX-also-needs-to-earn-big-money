import BinaryTreeNode
def serialize(proot):
    if not proot:
        return '#'

    return str(proot.value)+','+serialize(proot.left)+','+serialize(proot.right)


def deSerialize(astr):
    if len(astr)==0:
        return None
    alist = astr.split(',', 1)
    num = alist[0]
    astr = str(alist[-1])
    root = None
    if num != '#':
        root = BinaryTreeNode.BinaryTreeNode(num)
        root.left,astr = deSerialize(astr)
        root.right,astr = deSerialize(astr)

    return root,astr

def Test():
    pNode8 = BinaryTreeNode.BinaryTreeNode(8);
    pNode6 = BinaryTreeNode.BinaryTreeNode(6);
    pNode10 = BinaryTreeNode.BinaryTreeNode(10);
    pNode5 = BinaryTreeNode.BinaryTreeNode(5);
    pNode7 = BinaryTreeNode.BinaryTreeNode(7);
    pNode9 = BinaryTreeNode.BinaryTreeNode(9);
    pNode11 = BinaryTreeNode.BinaryTreeNode(11);

    pNode8.connectTreeNodes(pNode8, pNode6, pNode10);
    pNode6.connectTreeNodes(pNode6, pNode5, pNode7);
    pNode10.connectTreeNodes(pNode10, pNode9, pNode11);

    astr = serialize(pNode8)
    print(astr)
    root,astr = deSerialize(astr)
    root.printTree(root)

Test()