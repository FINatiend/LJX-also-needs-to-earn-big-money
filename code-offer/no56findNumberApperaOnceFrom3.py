def findNumber(numbers,length):
    if not numbers or length <= 0:
        return None

    bitSum = [0 for i in range(32)]

    for i in range(length):
        bitMask = 1
        for j in range(32):
            bit = numbers[i] & bitMask
            if bit != 0:
                bitSum[j] += 1
            bitMask << 1
    result = 0
    # 每一位相加，再对每一位判断能不能被3整除
    for i in range(32):
        result = result << 1
        result += bitSum[i] % 3
    return result

