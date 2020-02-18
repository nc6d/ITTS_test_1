#5
m = int(input('Input year'))
if 0<m<=10000:
	if m%100 != 0 :
		if m%4 == 0:
			print('Yes')
		else:
			print('No')
	elif m%100 == 0 and m%400 == 0 :
		print('Yes')
	else:
		print('No')
else:
	print('Wrong value')