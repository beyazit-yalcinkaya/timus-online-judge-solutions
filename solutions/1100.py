n=int(raw_input().strip())
k=[map(int, (raw_input().strip().split())) for w in xrange(n)]
k.reverse()
k.sort(key=lambda x: x[1])
k.reverse()
for q in xrange(n):
	print k[q][0], k[q][1]