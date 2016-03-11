def checkPal(n):
    pal_str = str(n)
    pal_len = len(pal_str)
    i = 0
    
    while pal_str[i] == pal_str[pal_len-i-1] and i <= pal_len/2:
        i+=1

    if i > pal_len/2:
        return 0  #if pal return 0
    
    return 1  #if not pal return 1


k = 100
j = 100
p = 0
f = 0
maxk = 0
maxj = 0
kloop = 0
jloop = 0

while k < 1000:
    kloop += 1
    j=100
    while j < 1000:
        jloop += 1
        check = checkPal(k*j)
        if check == 0:
            if k*j > p:
                p = k*j
            f += 1
        j += 1
    k += 1

print u"kloop=%d \n jloop=%d \n f=%d"%(kloop,jloop,f)
print u"k=%d j=%d"%(k,j)
print p
