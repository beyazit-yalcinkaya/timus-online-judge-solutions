n=int(raw_input())
lst_out=[['0' for u in xrange(n)] for o in xrange(n)]
arr=[[] for uu in xrange(n)]
num=1
for q in xrange(n):
	for i in xrange(q+1):
		lst_out[xrange(q, -1, -1)[i]][xrange(0, q+1, 1)[i]]=num
		num+=1
for q in xrange(n-1, 0, -1):
	for i in xrange(q):
		lst_out[xrange(n-1, q-n+1, -1)[i]][xrange(n-q, n, 1)[i]]=num
		num+=1
lst_out.reverse()
for t in xrange(n):
	for p in xrange(n):
		arr[t].append(lst_out[p][t])
for tt in xrange(n):
	print ' '.join(map(str, arr[tt]))