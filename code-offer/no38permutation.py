def permutation(pstr):
    if not pstr:
        return []
    resultStr = []
    # pstr = list(pstr)

    return core(pstr,0,resultStr)

def core(pstr,begin,resultStr):
    if len(pstr)==begin:
        resultStr.append(pstr)
        return resultStr

    for i in range(begin,len(pstr)):
        temp = pstr[i]
        pstr = pstr.replace(pstr[i],pstr[begin],1)
        pstr = pstr.replace(pstr[begin],temp,1)
        # pstr[i] = pstr[begin]
        # pstr[begin] = temp

        core(pstr,begin+1,resultStr)

        temp = pstr[i]
        pstr = pstr.replace(pstr[i], pstr[begin], 1)
        pstr = pstr.replace(pstr[begin], temp, 1)
        # pstr[i] = pstr[begin]
        # pstr[begin] = temp
    return resultStr

def test():
    print(permutation('abc'))

test()


