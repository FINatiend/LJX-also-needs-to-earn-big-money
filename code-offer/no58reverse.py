def reverseSentence(data):
    if not data:
        return None

    dataList = data.split()
    # data.split()和data.split(" ")有区别，前者是一个空列表，后者是含两个空字符串的列表
    # 一定要加这层判断，否则不能通过" "
    if len(dataList) == 0:
        return data
    # dataList.reverse()

    # result = ''
    # for i in dataList:
    # 这样最后一个会多一个空格
    #     result = result + str(i) + ' '
    result = ' '.join(data.split()[::-1])
    return result


# reverseSentence("i am a student.")
print(reverseSentence(' '))

