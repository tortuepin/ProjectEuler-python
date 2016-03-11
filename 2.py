prepre = 0
pre = 1
Fibo = 1
sum = 0

while Fibo < 4000000:
  if Fibo%2 == 0: 
    sum+=Fibo
  prepre=pre
  pre=Fibo
  Fibo = pre+prepre

  print u"Fibo=%d" %Fibo
  print u"pre=%d" %pre
  print u"prepre=%d" %pre
  print u"sum=%d" %sum

print sum
