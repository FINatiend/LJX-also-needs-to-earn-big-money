def maxInWindow(num,size):
    if not num or size<=0:
        return []
    res = []
    maxNum = max(num[0],max(num[0],num[1]))
    window = [num[0],num[1],num[2]]
    res.append(maxNum)
    for i in range(3,len(num)):

        window.pop(0)
        window.append(num[i])

        if num[i] > maxNum:
            maxNum = num[i]
            res.append(maxNum)


