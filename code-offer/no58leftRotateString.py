def leftRotateString(s,n):
    # 注意三个判断条件！！
    if not s:
        return ''
    if s == ' ':
        return s
    if len(s) <= n:
        return s

    return s[n:]+s[:n]

def leftRotateStringv2(s,n):
    if not s or len(s)<= 0:
        return ''
    if s == ' ' or len(s) <= n:
        return s
    s = list(s)
    s = Reverse(s,0,n-1)
    s = Reverse(s,n,len(s)-1)
    return "".join(Reverse(s,0,len(s)-1))

def Reverse(data,start,end):

    while start < end:
        temp = data[start]
        data[start] = data[end]
        data[end] = temp

        start += 1
        end -= 1
    return data