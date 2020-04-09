def maxFlex(num1,num2):
    while num2:
        sum = (num2 ^ num1) & 0xffffffff
        carry = ((num2 & num1)<<1) & 0xffffffff
        num1 = sum
        num2 = carry
    # 越界计算
    if num1 < 0xffffffff:
        return num1
    else:
        return -(num2 ^ 0xffffffff)

# 不用新的变量交换值
# 1。基于加减法
# a = a + b
# b = a - b
# a = a - b
# 基于异或
# a = a ^ b
# b = a ^ b
# a = a ^ b