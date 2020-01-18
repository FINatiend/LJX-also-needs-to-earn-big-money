class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.rightChild = None
        self.leftChild = None

    def insertLeftChild(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRightChild(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        if self == None:
            return -1
        return self.key

    def printPreTree(self):
        if self == None:return
        print(self.key,end=' ')
        if self.leftChild :
            self.leftChild.printPreTree()
        if self.rightChild:
            self.rightChild.printPreTree()

    def printInTree(self):
        if self == None: return
        if self.leftChild:
            self.leftChild.printInTree()
        print(self.key, end=' ')
        if self.rightChild:
            self.rightChild.printInTree()


def construct(preorder:list,inorder:list,length:int):
    if preorder == None or inorder == None or length <= 0:
        return None
    stratPreorder = 0
    endPreorder = stratPreorder +length -1
    startInorder = 0
    endInorder = startInorder + length -1
    return constructCore(preorder,stratPreorder,endPreorder,inorder,startInorder,endInorder)

def constructCore(preorderList,startPreorder,endPreorder,inorderList,startInorder,endInorder):

    #前序遍历的第一个数字是根结点的值
    rootValue = preorderList[startPreorder]
    root = BinaryTree(rootValue)


    if startPreorder == endPreorder:
        if startInorder == endInorder and preorderList[startPreorder] == inorderList[startInorder]:
            return root
        else:
            print("invalid input")

    #在中序遍历序列中找到根结点的值
    rootInorder = startInorder
    while rootInorder <= endInorder and inorderList[rootInorder] != rootValue:
        rootInorder += 1

    if rootInorder == endInorder and inorderList[rootInorder] != rootValue:
        print("invalid input")

    leftLength = rootInorder - startInorder
    leftPreorderEnd = startPreorder + leftLength

    if leftLength > 0:
        #构建左子树
        #root.insertLeftChild(constructCore(preorderList,startPreorder+1,leftPreorderEnd,
        #                               inorderList,startInorder,rootInorder-1))
        root.leftChild = constructCore(preorderList,startPreorder+1,leftPreorderEnd,
                                       inorderList,startInorder,rootInorder-1)

    if leftLength < endPreorder - startPreorder:
        #构建右子树
        # #root.insertRightChild(constructCore(preorderList,leftPreorderEnd+1,endPreorder,
        #                                 inorderList,rootInorder+1,endInorder))
        root.rightChild = constructCore(preorderList,leftPreorderEnd+1,endPreorder,
                                       inorderList,rootInorder+1,endInorder)
    print('\ntest:')
    root.printPreTree()
    return root


def test(testName:str,preorder:list,inorder:list,length:int):
    print(testName +"begins:")
    print("the preorder sequence is:")
    for i in preorder:
        print(i,end='')
    print("\nthe inorder sequence is:")
    for i in inorder:
        print(i,end='')

    root = construct(preorder,inorder,length)
    print("\npreorder:")
    root.printInTree()
    print("\ninorder:")
    root.printPreTree()

def test1():
    length = 8
    preorder = [1, 2, 4, 7, 3, 5, 6, 8]
    inorder = [4, 7, 2, 1, 5, 3, 8, 6]
    test("test1",preorder,inorder,length)

if __name__=="__main__":
    test1()

