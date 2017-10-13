n=int(raw_input())
lst=[map(int, raw_input().strip().split()) for o in xrange(n)]
lst_out=[]
for q in xrange(n):
	for i in xrange(q+1):
		lst_out.append(lst[xrange(q, -1, -1)[i]][xrange(0, q+1, 1)[i]])
for q in xrange(n-1, 0, -1):
	for i in xrange(q):
		lst_out.append(lst[xrange(n-1, q-n+1, -1)[i]][xrange(n-q, n, 1)[i]])
print ' '.join(map(str, lst_out))