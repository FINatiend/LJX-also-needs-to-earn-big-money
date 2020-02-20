# str[i]
# pattern[j]
# （1）pattern为.---匹配，都后移一位
# （2）pattern为ch，且str为ch，匹配，都后移一位
# pattern第二个字符不为* ，（1）（2）
# pattern第二个字符为*，第一个字符匹配0次，str不变，pattern移两位；
#                     第一个字符可匹配，即（1）（2），str移一位，pattern不变
def match(str,pattern):
    if len(str) == 0 and len(pattern)== 0:
        return True
    if len(str) != 0 and len(pattern)== 0:
        return False
    if len(pattern) > 1  and pattern[1] == '*':
        if len(str) > 0 and (pattern[0] == str[0] or pattern[0] == '.'):
            # 进入有限状态机的下一个状态
            # 继续留在有限状态机的当前状态
            # 略过一个'*'
            # 不能用i和j，因为用i和j时递归时字符串长度还是原长度
            # return match(str,pattern,i+1,j) or match(str,pattern,i,j+2)
            return match(str[1:], pattern) or match(str, pattern[2:])

        else:
            # 略过一个'*'
            return match(str,pattern[2:])

    if len(str) > 0 and (str[0] == pattern[0] or pattern[0] == '.'):
        return match(str[1:],pattern[1:])

    return False
# ====================测试代码====================
def Test(testName,string,pattern,expected):

    if(len(testName) != 0):
        print(testName+"begins: " );

    if(match(string, pattern) == expected):
        print("Passed.\n");
    else:
        print("FAILED.\n");


def main():
    Test("Test01", "", "", True);
    Test("Test02", "", ".*", True);
    Test("Test03", "", ".", False);
    Test("Test04", "", "c*", True);
    Test("Test05", "a", ".*", True);
    Test("Test06", "a", "a.", False);
    Test("Test07", "a", "", False);
    Test("Test08", "a", ".", True);
    Test("Test09", "a", "ab*", True);
    Test("Test10", "a", "ab*a", False);
    Test("Test11", "aa", "aa", True);
    Test("Test12", "aa", "a*", True);
    Test("Test13", "aa", ".*", True);
    Test("Test14", "aa", ".", False);
    Test("Test15", "ab", ".*", True);
    Test("Test16", "ab", ".*", True);
    Test("Test17", "aaa", "aa*", True);
    Test("Test18", "aaa", "aa.a", False);
    Test("Test19", "aaa", "a.a", True);
    Test("Test20", "aaa", ".a", False);
    Test("Test21", "aaa", "a*a", True);
    Test("Test22", "aaa", "ab*a", False);
    Test("Test23", "aaa", "ab*ac*a", True);
    Test("Test24", "aaa", "ab*a*c*a", True);
    Test("Test25", "aaa", ".*", True);
    Test("Test26", "aab", "c*a*b", True);
    Test("Test27", "aaca", "ab*a*c*a", True);
    Test("Test28", "aaba", "ab*a*c*a", False);
    Test("Test29", "bbbba", ".*a*a", True);
    Test("Test30", "bcbbabab", ".*a*a", False);

main()
# Test("Test08", "a", ".", True);





