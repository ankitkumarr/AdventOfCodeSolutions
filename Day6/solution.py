with open("input.txt") as f:
	
	a = [[0 for x in range (1000)] for x in range(1000)]
	while(True):
		inst = f.readline()
		if not inst:
			break
	#	for word in inst.split():

		word1 = inst.split()
		ct = 1
		if word1[0]=='turn':
		#	word1 = inst.split()
			ct+=1
		num11 = int ((word1[ct].split(','))[0])
		num12 = int ((word1[ct].split(','))[1])
		ct+=2
		num21 = int ((word1[ct].split(','))[0])
		num22 = int ((word1[ct].split(','))[1])
		for x1 in range (1 + num21-num11):
			for x2 in range(1 + num22 - num12 ):
	#			print x1+num11, x2+num12
				if word1[0] == 'turn':
					
					if word1[1] == 'on':
						a[x1+num11][x2+num12] = 1
					if word1[1] == 'off':
						a[x1+num11][x2+num12] = 0
				if word1[0] == 'toggle':
					if a[x1+num11][x2+num12] == 0:
						a[x1+num11][x2+num12] = 1
					else: 
						a[x1+num11][x2+num12] = 0

	count = 0
	for x in range (1000):
		for x2 in range (1000):
			if a[x][x2] == 1:
				count+=1
	print count
			

				
			



		

