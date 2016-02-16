address = open("input.txt")
floor = 0
index = 0
while True:
	c = address.read(1)
	if not c:
		break
	index+=1
	#floor = 0;
	if c == '(':
		floor = floor +1
	else:
		floor = floor -1
	if (floor<0) :
		break;
print "Answer is: ", floor, " ", index
address.close()
