def replaceBlank(string):
    length = len(string)

    if not string or length <= 0:
        return
    # 输入''的情况
    if length == 0:
        return ''

    s_list= list(string)

    numberOfBlank = 0
    for i in s_list:
        if i==' ':
            numberOfBlank += 1

    newlength = length + numberOfBlank*2

    frontIndex = length-1
    endIndex = newlength-1

    append_list = [0] * (numberOfBlank * 2)
    s_list+=append_list

    while frontIndex >= -1:
        if s_list[frontIndex] == ' ':
            s_list[endIndex] = '0'
            endIndex -= 1
            s_list[endIndex] = '2'
            endIndex -= 1
            s_list[endIndex] = '%'
            endIndex -= 1
        else:
            s_list[endIndex] = s_list[frontIndex]
            endIndex -= 1
        frontIndex -= 1

    return ''.join(s_list)

print(replaceBlank('hello world'))








