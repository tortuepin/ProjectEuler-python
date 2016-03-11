def addSqurts(n):
    sum = 0
    i = 1
    while i <= n:
        sum += i**2
        i += 1

    return sum


def squareSum(n):
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1

    return sum**2


print squareSum(100)-addSqurts(100)
