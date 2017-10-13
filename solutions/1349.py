n = int(raw_input())
out=[]
if n != 0:
	for a in range(1, 101):
		for b in range(1, 101):
			c=(a**n+b**n)**(1.0/n)
			if c in range(1, 101) and a != b and b != c and a != c:
				out.append([a, b, int(c)]) 
if len(out)>0:
	for i in min(out):
		print i,
else:
	print -1
