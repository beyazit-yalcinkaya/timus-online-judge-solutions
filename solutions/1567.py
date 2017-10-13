a=list(raw_input())
for i in a:
	if i=='a' or i=='d' or i=='g' or i=='j' or i=='m' or i=='p' or i=='s' or i=='v' or i=='y' or i=='.' or i==' ':
		a[a.index(i)]=1
	elif i=='b' or i=='e' or i=='h' or i=='k' or i=='n' or i=='q' or i=='t' or i=='w' or i=='z' or i==',':
		a[a.index(i)]=2
	else:
		a[a.index(i)]=3
print sum(a)