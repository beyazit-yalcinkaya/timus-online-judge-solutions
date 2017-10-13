h, w, n=map(int, raw_input().strip().split())
k=[len(raw_input().strip()) for y in xrange(n)]
s=[k[0]]
for i in xrange(1, n):
	if s[-1]+k[i]+1<=w:
		s[-1]=s[-1]+k[i]+1
	else:
		s.append(k[i])
if len(s)%h==0:
	print len(s)/h
else:
	print len(s)/h+1