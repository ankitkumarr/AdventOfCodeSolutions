def rule1(st):
	for x in range ((len(st)-1)):
		if rule1test (st[x:x+2], st, x)==True:
			return True

	return False


def rule1test(st1, st2, y):
	for x in range (len(st2)):
		if (x< ((len(st2))-1)) and x!= y and x!=y-1 and x!=y+1 :
			if st2[x:x+2]==st1:
				return True
	return False




def rule2(st):
	for x in range (len(st)):
		if x < ((len(st))-2):
			if st[x]==st[x+2]:
				return True	
	return False






with open("input.txt") as f:
	count = 0
	while(True):
		line = f.readline()
		if not line:
			break
		if (rule2(line) and rule1(line)):
			count+=1
	print "Total nice strings are: ", count


	
