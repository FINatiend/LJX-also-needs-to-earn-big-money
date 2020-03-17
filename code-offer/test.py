def test():
    str = '7,8,9,0'
    # print(str[1])
    str = str.split(',',1)
    str = str[1:]
    print(str)

def test1():
    str1 = str(931886)
    str1 = str1[1:4]
    num = int(str1)
    print(len(str1))
    print(num)
    print(type(num))

def test2():
    count = [1]*10
    print(len(count))
    count[2] = 2
    for i in count:
        print(i)

test2()