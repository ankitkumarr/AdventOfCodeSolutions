with open("input.txt") as f:
	d = 0
	sum1 = 0
	mult = 1
	flag = 0
	while True:
		
		nu = ''
		#c = f.read(1)
		#if not c:
		#	break	
	#	flag = 0	
		c = ''
		while (c!='x') :
			nu = nu + c
			c = f.read(1)
			if (c=='\n'):
				c = f.read(1)
			if not c:
				break		
				flag = 1
		if flag==1 :
			break
		d = d+1
		print "this is " + chr(flag)
#		mult = mult* int(nu)
		if (d%3)==0 :
			sum1 = sum1 + mult
			mult = 1

print "Sum = ", sum1, nu


