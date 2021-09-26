password = 'a123456'
i = 3
while True:
	pw = input('Please enter password: ')
	if pw ==password:
		print('password match')
		break
	else:
		i = i - 1
		print('Wrong password' , i , 'more time')
		if i == 0:
			break


	
