import hashlib


def hashfunction1(stri):
	m = hashlib.md5()
	m.update(stri)
	return m.hexdigest()

m = hashlib.md5()
s = 'iwrupvqb'
x = 0
while (True):
	st = s + str(x)
	if hashfunction1(st)[:6] == '000000':
		break
	x+=1
print "The answer is: ", x


