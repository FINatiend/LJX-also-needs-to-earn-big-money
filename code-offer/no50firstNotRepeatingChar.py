class Solution:
    def __init__(self):
        self.alist = []
        self.dic = {}

    def insert(self,char):
        if char not in self.dic:
            self.alist.append(char)
            self.dic[char] = 1
        else:
            self.dic[char] += 1

    def fisrtAppearOnce(self):
        while len(self.alist) > 0 and self.dic[self.alist[0]] > 1:
            self.alist.pop(0)
            #注意判断不符合条件的情况
        if len(self.alist) > 0:
            return self.alist[0]
        return '#'

    def Test(self,expected):
        if (self.fisrtAppearOnce() == expected):
            print("Passed.\n")
        else:
            print("FAILED.\n");
if __name__ == '__main__':
    s = Solution()
    s.Test('#')
    s.insert('g')
    s.Test('g')
    s.insert('o')
    s.Test('g')
    s.insert('o')
    s.Test('g')
    s.insert('g')
    s.Test('#')
    s.insert('l')
    s.Test('l')
    s.insert('e')
    s.Test('l')




