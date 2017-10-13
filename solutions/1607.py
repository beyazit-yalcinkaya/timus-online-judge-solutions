a, b ,c ,d = map(int, raw_input().split())
pivot = 0
while True:
	if pivot % 2 == 0:
		pivot += 1
		if a < c:
			a += b
		else:
			break
	else:
		pivot += 1
		if c > a:
			c -= d
		else:
			break
if pivot % 2 == 1:
	print a
else:
	print c