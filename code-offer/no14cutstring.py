#大问题->小问题->小问题最优解组合->大问题最优解----->可以用动态规划
def maxProductAfterCutting_DP(length):
    if length <2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    products = [0,1,2,3]
    max = 0

    for i in range(4,length+1):
        max = 0
        products.append(0)
        for j in range(1,i//2+1):
            product = products[j] * products[i-j]
            if max < product:
                max = product

            products[i] = max

    max = products[length]
    return max

def maxProductAfterCutting_TX(length):
    if length <2:
        return 0
    if length == 2:
        return 1
    if length == 3:
        return 2

    timesOf3 = length//3
    if (length - timesOf3 * 3 == 1):
        # timesOf3 -= 1
        timesOf2 = 2
    # timesOf2 = (length - timesOf3 * 3)//2
    timesOf2 = 1
    return int(pow(3,timesOf3)) * int(pow(2,timesOf2))

print(maxProductAfterCutting_DP(8))
print(maxProductAfterCutting_TX(8))