def isPopOrder(pPush,pPop):
    statck = []

    #  对输出序列进行遍历
    while(pPop):
        # 若输入序列的第一个与输出序列的第一个相同，代表该入栈就出栈
        if pPush and pPop[0] == pPush[0]:
            pPush.pop(0)
            pPop.pop(0)
        # 若辅助栈的第一个元素为输出序列的第一个元素，则直接弹出
        elif statck and statck[-1] == pPop[0]:
            statck.pop()
            pPop.pop(0)
        # 若输出序列的元素还没有出现，则把输入序列的元素逐个压栈
        elif pPush:
            statck.append(pPush.pop(0))
        # 若输入序列已为空，则表示该输出序列不是栈的输出序列
        else:
            return False

    return True


