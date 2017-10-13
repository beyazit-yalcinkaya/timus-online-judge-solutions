k=int(raw_input().strip())
p=map(int, raw_input().strip().split())
t=[]
for i in xrange((k/2)+1):
	t.append((min(p)/2)+1)
	p.remove((min(p)))
print sum(t)