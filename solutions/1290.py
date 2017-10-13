n = int(raw_input())
lst = [int(raw_input()) for i in range(n)]
for i in sorted(lst, reverse = True):
	print i