def rule1(st):
	count = 0;
	for x in range(len(st)):
		if((st[x]=='a') or (st[x]=='i') or (st[x]=='o') or (st[x]=='e') or (st[x]=='u')):
			count+=1
			if count==3:
				return True
	return False


def rule2(st):
	for x in range (len(st)):
		if x!= ((len(st))-1):
			if st[x]==st[x+1]:
				return True

	return False

def rule3(st):
	for x in range (len(st)):
		if x!= ((len(st))-1):
			if ((st[x:x+2]=='ab') or (st[x:x+2]=='cd') or (st[x:x+2]=='pq') or (st[x:x+2]=='xy')):
				return True
	return False

with open("input.txt") as f:
	count = 0
	while(True):
		line = f.readline()
		if not line:
			break
		if rule1(line) and rule2(line) and not rule3(line):
			count+=1
	print "Total nice strings are: ", count


	
