def f(n):
    result = [0,1]
    if n == 1:
        return result[n]
    for i in range(2,n+1):
        result.append(1)
        j = i-1
        while j >0:
            result[i] += result[j]
            j -= 1
    return result[n]

print(f(6))