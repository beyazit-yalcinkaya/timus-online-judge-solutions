n = int(raw_input())
out = 0
lst = []
for i in range(n):
	temp = raw_input()
	if temp not in lst:
		lst.append(temp)
	else:
		out += 1
print out