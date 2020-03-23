def find(arr):
    from collections import Counter
    count = Counter(arr)
    # count = {2:2,3:2...}字典
    # most_common将其转为元组列表，且参数不能为负数。因此只能在后面[-2]取列表后两个
    # res = [(4,1),(6,1)]
    res = Counter(arr).most_common()[-2:]
    return list(map(lambda x:x[0],res))

print(find([ 2, 4, 3, 6, 3, 2, 5, 5] ))