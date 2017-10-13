t1, t2 = map(int, raw_input().split())
plus = sum(map(int, raw_input().split()))*20
if t1 + plus > t2:
	print 'Dirty debug :('
else:
	print 'No chance.'