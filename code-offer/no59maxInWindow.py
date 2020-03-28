def maxInWindow(num,size):
    if not num or size<=0 or len(num) <= 0 :
        return []
    res = []
    window = []
    maxNum = -1

    window.append(num[0])
    for i in range(1,size):

        if num[i] > maxNum:
            window.pop(0)
        window.append(i)

    for i in range(size,len(num)):

        res.append(num[window[0]])

        while window and num[i] >= num[window[-1]]:
            window.pop()

        if window and window[0]  <= i - size:
            window.pop(0)
        window.append(i)

    return res


