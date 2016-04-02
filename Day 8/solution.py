
def fstlit(st):
	return len(st)+2

def fstval(st2):
	count = 0
	x = 0
	while(True):

		if x+1 == len(st2):
			break
		if st2[x] == '/' and st2[x+1] == 'x':
			x+=2
			count+=1
		elif st2[x] == '/':
			x+=1
			continue
		else: 
			count+=1
		x+=1

	
	return count


	

with open("input.txt") as f:
	stlit = 0
	stval = 0
	while(True):
		line = f.readline()
		if not line:
			break
		stlit = stlit + fstlit(line)
		stval = stval - fstval(line)
	print stlit - stval


