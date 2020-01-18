# def Test(num,expected):
#     count = 0
#     while(num):
#         count += 1
#         num = (num-1) & num
#         # print("num:",num)
#     if count == expected:
#         print("pass")
#     else:
#         print("failed")

def Test(num,expected):
    count = 0
    flag = 1
    while(flag):
        if (flag & num):
            count += 1
        flag = flag << 1

    if count == expected:
        print("pass")
    else:
        print("failed")

# // 输入0，期待的输出是0
Test(0, 0)

# // 输入1，期待的输出是1
Test(1, 1)
#
# // 输入10，期待的输出是2
Test(10, 2)

# // 输入0x7FFFFFFF，期待的输出是31
Test(0x7FFFFFFF, 31)

# // 输入0xFFFFFFFF（负数），期待的输出是32
Test(0xFFFFFFFF, 32)

# // 输入0x80000000（负数），期待的输出是1
Test(0x80000000, 1)
