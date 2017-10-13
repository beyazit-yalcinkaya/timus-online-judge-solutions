a=b=int(raw_input().strip())
c=[]
d=[]
while b<=1:
	c.append(b)
	b+=1
while b>=1:
	d.append(b)
	b-=1
if a<1: print sum(c)
elif a>1: print sum(d)
else: print a