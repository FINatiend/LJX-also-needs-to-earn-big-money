class Solution:
    def replaceBlank(self, s: str) -> str:
        return s.replace(' ','%20')
        '''
        length = len(s)
        if length<=0:
            return
        originalLength = length
        numOfBlank = 0
        for i in range(len(s)):
            if s[i]==" ":
                numOfBlank = numOfBlank + 1

        newLength = originalLength + 2*numOfBlank
       ##for i in range(originalLength,newLength):
          ##  s[i] = ''
        indexOfNew = newLength
        indexOfOrigial = originalLength-1

       while indexOfOrigial>=0 and indexOfNew > indexOfOrigial:
            if s[indexOfOrigial] == ' ':
                s[indexOfNew] = ['0']
                s[indexOfNew-1] = ['2']
                s[indexOfNew-2] = ['%']
                indexOfNew -=2
            else:
                s = s[:inde]
                s[indexOfNew] = [s[indexOfOrigial]]
            indexOfOrigial-=1
            indexOfNew-=1
            '''

if __name__ == '__main__':
    s = Solution()
    print(s.replaceBlank("We Are Happy"))