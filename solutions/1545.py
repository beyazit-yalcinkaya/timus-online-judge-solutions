n = int(raw_input())
lst = [raw_input() for i in range(n)]
x = raw_input()
for i in sorted(lst):
	if i.startswith(x):
		print i