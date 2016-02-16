

a = [[0 for x in range(1000)] for y in range(1000) ]
i = 0
j = 0
a[0][0] = 1
count = 0
with open("input.txt") as f:
	while True:
		c = f.read(1)
		if not c:
			break
		if c=='^':
			i+=1
			a[i][j] = 1
		if c == 'v':
			i-=1
			a[i][j] = 1
		if c == '>':
			j+=1
			a[i][j] = 1
		if c == '<':
			j-=1
			a[i][j] = 1
for x in range(1000):
	for y in range(1000):
		if a[x][y]==1 :
			count+=1

print "Count is ", count


