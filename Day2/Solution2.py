with open("input.txt") as f:
	d = 0
	sum1 = 0
	flag = 0
	a= [0 for x in range(3)]

	while True:
		
		
		mult = 1
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
				#flag = 1
				break
				#c = f.read(1)
			if not c:
				flag = 1
				break		
		if flag==1 :
			break
		d = d+1
		if(d%3)!=0 :
			a[(d%3)-1] = int(nu)
			print "this is " , a[(d%3)-1], d%3
		#print "this is " , nu
	#	mult = mult* int(nu)
		if (d%3)==0 :
			a[2] = int(nu)
			a.sort()
			#print a
			mult = a[0]*a[1]*a[2]
			sum1 = sum1 + mult + 2*(a[0]+a[1])
		#	mult = 1

print "Sum = ", sum1


