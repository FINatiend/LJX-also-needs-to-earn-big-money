def multiply(a_array,b_array):
    length1 = len(a_array)
    length2 = len(b_array)

    if length1 == length2 and length2 > 1:
        b_array[0] = 1
        for i in range(1,length1):
            b_array[i] = b_array[i-1]*a_array[i-1]

        temp = 1
        for i in range(length1-2,-1,-1):
            temp *= a_array[i+1]
            b_array[i] *= temp
    return b_array