n, m=map(int, raw_input().strip().split())
arr=[[] for i in xrange(n)]
k=0
for i in xrange(m):
	a=int(raw_input())
	arr[a-1].append(a)
for t in xrange(n):
	print '%.2f%s' %(len(arr[t])*100.0/m, '%')