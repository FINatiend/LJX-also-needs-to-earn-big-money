class Solution:
    g_Invalid_input = False
    def power(self,base,exponent):
        if base == 0 and exponent < 0:
            self.g_Invalid_input = True
            return 0

        absExponent = exponent

        if exponent < 0:
            absExponent = -exponent

        result = self.powerCal_2(base,absExponent)
        if exponent < 0:
            result = 1 / result
        return result

    def powerCal(self,base,exponent):
        result = 1
        for i in range(0,exponent):
            result *= base
        return result

    def powerCal_2(self,base,exponent):

        if exponent == 0:
            return 1
        if exponent == 1:
            return base

        result = self.powerCal_2(base,exponent>>1)
        result *= result

        #判断奇偶
        if exponent & 0x1 == 1:
            result *= base

        return result


    def Test(self,base,exponent,expected,inputerror):

        if self.power(base,exponent) == expected and inputerror == self.g_Invalid_input:
            print("passed")
        else:
            print("failed")

if __name__ == '__main__':
    s = Solution()
    # 底数、指数都为正数
    s.Test(2, 3, 8, False)
    #底数为负数、指数为正数
    s.Test(-2, 3, -8, False)
    #指数为负数
    s.Test( 2, -3, 0.125, False)
    #指数为0
    s.Test(2, 0, 1, False)
    #底数、指数都为0
    s.Test(0, 0, 1, False)
    #底数为0、指数为正数
    s.Test(0, 4, 0, False)
    #底数为0、指数为负数
    s.Test(0, -4, 0, True)

