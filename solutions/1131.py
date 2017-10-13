from math import log
n, k = map(int, raw_input().split())
lst = []
if n > 1:
	pivot = int(log(n, 2))
	while 2**(pivot-1) > k:
		pivot -= 1
	x = n - 1 - ((2 ** pivot) - 1)
	if x <= 0:
		print pivot
	elif x > 0:
		if x % k == 0:
			print x / k + pivot
		else:
			print x / k + 1 + pivot
else:
	print 0