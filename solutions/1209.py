import math
n=int(raw_input().strip())
a=[int(raw_input().strip()) for i in xrange(n)]
a=map(lambda x: (-1+math.sqrt(8.0*x-7))/2, a)
for w in range(n):
	if a[w]==int(a[w]): print 1
	else: print 0