n = int(raw_input())
prof_lst = set([raw_input() for i in range(n)])
m = int(raw_input())
out = 0
for i in range(m):
	temp = raw_input()
	if temp in prof_lst:
		out += 1
print out