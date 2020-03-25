def reverse(data,start,end):
    if not start or not end:
        return

    while start < end:
        temp = data[start]
        data[start] = data[end]
        data[end] = temp

        start += 1
        end -= 1
def reverseSentence(data):
    if not data:
        return None
    start = 0
    end = len(data)

    # 翻转整个句子
    reverse(data,start,end)
    # 翻转句子中的每个单词
    start,end = 0,0

    while
    while start < len(data):
        if data[start] == ' ':
            start += 1
            end += 1
        elif
