# 数字格式 A[.[B]][e|EC] or  .[B][e|EC]
# A 整数部分  B小数部分  C指数部分
# A和C： + -开头'0-9'数字串  B不能有+-

def isNumeric(str):
    if len(str) == 0:
        return False
    numeric , str = scanInterger(str)

    # 若出现'.'，则接下来为小数部分
    # 小数点前后都有数字-->true
    # 小数点前有数字 12. 表示12.0 true
    # 小数点后有数字 .12 表示0.12 true
    # 前后都无数字，false
    if len(str) > 0 and str[0] == '.':
        str = str[1:]
        numericTemp , str = scanUnsignedInterger(str)
        numeric = numericTemp or numeric
    # 若出现'E''e'，则接下来为指数部分

    if len(str) > 0 and str[0] in ('e','E'):
        str = str[1:]
        numericTemp , str = scanInterger(str)
        # e前没有数字或者后没有数字都不行，所以这里用and
        numeric = numericTemp and numeric
    #这里必须加判断len(str) == 0，可以解决诸如1a3.14和1.1.1之类的判断错误
    return numeric and len(str) == 0

#     匹配A和C中的符号部分
def scanInterger(str):
    if len(str) > 0 and (str[0] == '+' or str[0] == '-'):
        str = str[1:]
    return scanUnsignedInterger(str)

# 匹配数字部分
def scanUnsignedInterger(str):
    i = 0
    numeric = False
    if len(str) > 0:
        while len(str) > i and (str[i] >= '0' and str[i] <= '9'):
            i += 1
    #表示在.Ee之前有数字
    if i > 0:
        numeric = True
        str = str[i:]
    return numeric,str

def Test(testname,str,expected):
    if len(testname) > 0:
        print(testname+'begin:')
    if isNumeric(str) == expected:
        print("passed")
    else:
        print("failed")

if __name__ == '__main__':
    Test('test1','1a3.14',False)
