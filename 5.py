import math

def checkEvenlyDivisible(n, from_n, to):
    i = from_n
    while i <= to:
        if n%i != 0:
            break
        i+=1
    if i > to:
        return 1#if evenly divisible
    return 0#if not



inc = 20 * 19

i = inc

while i <= math.factorial(20):
    if checkEvenlyDivisible(i,1,20):
        break
    i += inc

print i
        
