def sequenceOfBST(sequence):
    length = len(sequence)
    if length == 0:
        return False

    root = sequence[-1]

    # 在二叉搜索树中左节点的值小于根节点的值
    i = 0
    # 这里是length是因为当没有右子树时，且只有两个数如[6,7]，如果判定到length-1，那么这里不会进入循环，j依然等于0，
    # 而此时j从0开始会使得j仍然在i的位置
    for i in range(length):
        if sequence[i] > root:
            break

    j = i
    # length-1是因为最后一个是根节点，这里可以用length-1是因为若j在最后一个节点，最后截取的时候不截取跟节点对结果不会造成影响
    for j in range(j,length-1):
        if sequence[j] < root:
            return False

    # 判断左子树
    left = True
    if i > 0:
        left = sequenceOfBST(sequence[:i])

    right = True
    if j < len(sequence)-1:
        right = sequenceOfBST(sequence[i:length-1])

    return left and right

if __name__ == '__main__':
    list = [4,8,7,5]
    if sequenceOfBST(list):
        print("pass")
    else:
        print("failed")