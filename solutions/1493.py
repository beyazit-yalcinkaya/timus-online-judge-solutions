a=int(raw_input())
def f(x):
	if len(x)==5: x.insert(0, 0)
	return x
b=f(map(int, list(str(a+1))))
c=f(map(int, list(str(a-1))))
if sum(b[:3])==sum(b[3:]) or sum(c[:3])==sum(c[3:]): print 'Yes'
else: print 'No'