def digitAnIndex(index):
    if index < 0:
        return -1

    digits = 1
    while True:
        numbers = countOfIntergers(digits)
        if index < numbers * digits:
            return digitAtIndex(index,digits)
        index -= digits * numbers
        digits += 1
    return -1

def countOfIntergers(digits):
    if digits == 1:
        return 10
    return 9 * pow(10,digits-1)

def digitAtIndex(index,digits):
    number = list(str(beingNumber(digits) + index/digits))
    indexFromLeft = index%digits
    return number[indexFromLeft]

def beingNumber(digits):
    if digits == 1:
        return 0
    return pow(10,digits-1)

print(digitAnIndex(10))