def Reverse(data,start,end):

    while start < end:
        temp = data[start]
        data[start] = data[end]
        data[end] = temp

        start += 1
        end -= 1
    return data
def reverseSentence(data):
    if not data:
        return ''
    datalist = list(data)

    start = 0
    end = len(data)-1

    # 翻转整个句子
    datalist = Reverse(datalist,start,end)
    print(datalist)
    # 翻转句子中的每个单词
    start,end = 0,0

    while start < len(datalist):
        if end == len(datalist)-1:
            datalist = Reverse(datalist,start,end)
            break
        elif datalist[end] == ' ':
            datalist = Reverse(datalist,start,end-1)
            start = end+1
        end += 1
    result = " ".join(datalist)
    return result

print(reverseSentence("i am a student.")
)



