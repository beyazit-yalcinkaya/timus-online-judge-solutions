n=int(raw_input().strip())
k=[raw_input().strip() for i in xrange(n)]
for q in k:
	if q.startswith('A')==True or q.startswith('P')==True or q.startswith('O')==True or q.startswith('R')==True:
		k[k.index(q)]=1
	elif q.startswith('B')==True or q.startswith('M')==True or q.startswith('S')==True:
		k[k.index(q)]=2
	else:
		k[k.index(q)]=3
k.insert(0, 1)
r=[abs(k[t]-k[t+1]) for t in xrange(len(k)-1)]
print sum(r)