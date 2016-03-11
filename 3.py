#-*- coding: utf-8 -*-

prime_factors = []
qnumber = 600851475143
qnumbe = 13195
i=2
j=2
max=0


# 素数を見つけてqnumberを割る
while i < qnumber/2:
  # 素数を見つける
  j=2
  while j < i/2:
    #iがjで割り切れちゃったら終わり
    if i%j == 0:
      break
    j+=1
  #jがi/2以上になってたらiは素数。
  if j >= i/2:
    #qnumberがiで割り切れたらiは素因数なのでprime_factorsに追加してqnumberを割る
    while qnumber%i==0:
      prime_factors.append(i)
      qnumber = qnumber/i
      
  i+=1

prime_factors.append(qnumber)

for value in prime_factors:
  print value
  if max < value:
    max = value

print u"max=%d"%max
