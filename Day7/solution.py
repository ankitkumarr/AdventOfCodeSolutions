def findar(str, arr):		
	for xy in range(len(str)):
		if arr[xy] == str:
			return xy


	return -1

with open("input.txt") as f:
	x = 0
	arr = ["" for z in range (100000)]
	arrv = [0 for z in range (100000)]
	for line in f:
		word = line.split();
		if word[1] == '->':
		#	print (x, word)
		#	num = int(word[0])
			find = findar(word[2], arr)
			find2 = findar(word[0], arr)
			if find == -1:
				arr[x] = word[2]
				if find2 == -1:
					arrv[x] = int(word[0])
				else:
					arrv[x] = arrv[find2]
				x+=1
			else:
				if find2 == -1:
					arrv[find] = int(word[0])
				else:
					arrv[find] = arrv[find2]

		if word[0] == 'NOT':
			find = findar(word[3], arr)
			if find == -1:
				arr[x] = word[3]
				arrv[x] = ~(arrv[findar(word[1], arr)])
				x+=1
			else:
				arrv[find] = ~(arrv[findar(word[1], arr)])

		if word[1] == 'AND':
			find = findar(word[4], arr)
			if find == -1:
				arr[x]  = word[4]
				arrv[x] = arrv[findar(word[0], arr)] & arrv[findar(word[2], arr)]
				x+=1
			else:
				arrv[find] = arrv[findar(word[0], arr)] & arrv[findar(word[2], arr)]

		if word[1] == 'OR':
			find = findar(word[4], arr)
			if find == -1:
				arr[x]  = word[4]
				arrv[x] = arrv[findar(word[0], arr)] | arrv[findar(word[2], arr)]
				x+=1
			else:
				arrv[find] = arrv[findar(word[0], arr)] | arrv[findar(word[2], arr)]

		if word[1] == 'LSHIFT':
			find = findar(word[4], arr)
			if find == -1:
				arr[x] = word[4]
				arrv[x] = arrv[findar(word[0], arr)] << int(word[2])
				x+=1

			else:
				arrv[find] = arrv[findar(word[0], arr)] << int(word[2])

		if word[1] == 'RSHIFT':
			find = findar(word[4], arr)
			if find == -1:
				arr[x] = word[4]
				arrv[x] = arrv[findar(word[0], arr)] >> int(word[2])
				x+=1

			else:
				arrv[find] = arrv[findar(word[0], arr)] >> int(word[2])

	


				
				
