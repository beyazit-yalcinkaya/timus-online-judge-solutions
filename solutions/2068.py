raw_input()
lst = filter(lambda x: x % 2 == 1, map(int, raw_input().split()))
pivot = 0
for i in range(len(lst)):
	pivot += lst[i] / 2
if pivot % 2 == 0:
	print 'Stannis'
else:
	print 'Daenerys'