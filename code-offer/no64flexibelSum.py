def sum_1(n):
    # iterable – 可迭代对象，
    # 如：列表(list)、元组(tuple)、集合(set)、字典(dictionary)。

    # Python  list() 函数是对象迭代器，可以把range()返回的可迭代对象转为一个列表，
    # 返回的变量类型为列表。
    # list() 方法用于将元组转换为列表。
    return sum(list(range(1,n+1)))

# 终止递归采用逻辑与的短路特性
def sum_2(n):
    return n and n + sum_2(n-1)

# 采用两个函数，一个作为终止函数，一个作为计算函数
def sum_3_cal(n):
    flag = {False:sum_3_judge,True:sum_3_cal}
    return n + flag[not not n](n-1)

def sum_3_judge(n):
    return 0

print(sum_1(3))
print(sum_2(3))
print(sum_3_cal(3))


