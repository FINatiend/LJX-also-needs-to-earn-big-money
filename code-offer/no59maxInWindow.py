def maxInWindow(num,size):
    if not num or size<=0 or len(num) <= 0 or len(num)<size:
        return []
    res = []
    window = []


    window.append(0)
    for i in range(1,size):

        if num[i] > num[window[0]]:
            window.pop(0)
        # 注意保存的是下标
        window.append(i)

    for i in range(size,len(num)):

        res.append(num[window[0]])
        # 这里是从后边的小的开始比较，一个个把当前窗口内比num[i]小的删掉
        while window and num[i] >= num[window[-1]]:
            window.pop()

        if window and window[0]  <= i - size:
            window.pop(0)
        window.append(i)
    res.append(num[window[0]])

    return res

print(maxInWindow([2,3,4,2,6,2,5,1],3))


