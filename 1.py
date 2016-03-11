sum3 = 0
sum5 = 0
sum3_5 = 0

counter = 1

while counter < 1000:
	
	if counter%3 == 0:
		sum3+=counter
	elif counter%5 == 0:
		sum5+=counter
	elif counter%3 == 0 and counter%5 == 0:
		sum3_5+=couter
	print 'counter='
	print counter
	print sum3+sum5-sum3_5

	counter+=1
print sum3+sum5-sum3_5
