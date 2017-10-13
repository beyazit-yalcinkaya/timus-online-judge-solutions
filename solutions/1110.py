n, m, y = map(int, raw_input().split())
out = []
for x in range(1, m):
	if (x ** n) % m == y:
		out.append(x)
	else:
		continue
if out == []:
	print -1
else:
	for i in sorted(out):
		print i,