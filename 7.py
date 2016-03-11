def checkPrime(n):
    """Check prime or not

    if n = prime :return 1
    if not       :return 0
    """

    tmp = 2
    tail = n
    isPrime = 1

    while tmp < tail:
        if n % tmp == 0:
            isPrime = 0
            break
        tail = n/tmp + 1
        tmp += 1


    return isPrime


i = 1
primeCount = 0

while primeCount < 10001:
    i += 1
    if checkPrime(i) == 1:
        primeCount += 1

print i
