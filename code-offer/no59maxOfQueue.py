class maxOfQueue:
    def __init__(self):
        self.maximuns = []
        self.data = []

    def pushback(self,number):
        while len(self.maximuns) != 0 and number >= self.data[self.maximuns[-1]]:
            self.maximuns.pop()
        self.data.append(number)
        self.maximuns.append(len(self.data)-1)

    def popFront(self):
        if len(self.data) == 0:
            return
        if self.data[self.maximuns[0]] == self.data[0]:
            self.maximuns.pop(0)

        self.data.pop(0)

    # 保存的是下标的话，pop操作的时候data的数字的数值都会变化，而max的不变，从而导致出错
    def getMax(self):
        if len(self.maximuns) == 0:
            return
        return self.data[self.maximuns[0]]

if __name__ == '__main__':
    s = maxOfQueue()
    s.pushback(2)
    print(s.getMax())
    s.pushback(3)
    print(s.getMax())
    s.pushback(4)
    print(s.getMax())
    s.pushback(2)
    print(s.getMax())
    s.popFront()
    print(s.getMax())


